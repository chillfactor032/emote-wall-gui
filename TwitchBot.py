import asyncio
import json
import logging
import os
import argparse
import configparser
from typing import Any

import requests
import twitchio
from twitchio import authentication, eventsub
from twitchio.ext import commands

LOGGER: logging.Logger = logging.getLogger(__name__)

class Bot(commands.Bot):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.token_file = ".tio.tokens.json"
        self.wall_api_host = kwargs.get("wall_api_host","127.0.0.1")
        self.wall_api_port = kwargs.get("wall_api_port",80)

    async def setup_hook(self) -> None:
        # Create token file if it doesn't exist
        if not os.path.exists(self.token_file):
            with open(self.token_file, 'wb') as f:
                f.close()

        with open(self.token_file, "rb") as fp:
            tokens = json.load(fp)

        for user_id in tokens:
            if user_id == self.bot_id:
                continue
            chat = eventsub.ChatMessageSubscription(broadcaster_user_id=user_id, user_id=self.bot_id)
            await self.subscribe_websocket(chat)

    async def event_ready(self) -> None:
        LOGGER.info("Logged in as: %s", self.user)

    async def event_oauth_authorized(self, payload: authentication.UserTokenPayload) -> None:
        await self.add_token(payload.access_token, payload.refresh_token)
        if payload.user_id == self.bot_id:
            return
        chat = eventsub.ChatMessageSubscription(broadcaster_user_id=payload.user_id, user_id=self.bot_id)
        await self.subscribe_websocket(chat)

    async def event_message(self, payload: twitchio.ChatMessage):
        # Check to see if message has emotes
        for fragment in payload.fragments:
            if fragment.type == "emote":
                LOGGER.info(f"Emote[{fragment.emote.id}]: {fragment.text}")
                params = {"id":fragment.emote.id}
                try:
                    resp = requests.get(f"http://{self.wall_api_host}:{self.wall_api_port}/emote_add", params=params)
                    resp.raise_for_status()
                except requests.exceptions.HTTPError as e:
                    LOGGER.error("HTTP error occurred: "+str(e))
                except Exception as e:
                    LOGGER.error("A request error occurred: "+str(e))


def main() -> None:
    twitchio.utils.setup_logging(level=logging.INFO)

    parser = argparse.ArgumentParser(
        prog='Emote Wall TwitchBot',
        description='Informs the Emote Wall API of emotes coming from Twitch Chat',
        epilog='Check github for more information https://github.com/chillfactor032/emote-wall-gui')
    
    parser.add_argument("-c", "--config", help="path to the config file (required)", required=True)
    args = parser.parse_args()
    
    if not os.path.exists(args.config):
        LOGGER.error("Config file does not exist. Check the path and try again.")
        return

    config = configparser.ConfigParser()
    try:
        config.read(args.config)
        client_id = config["twitchbot"].get("client_id")
        client_secret = config["twitchbot"].get("client_secret")
        bot_id = config["twitchbot"].get("bot_id")
        owner_id = config["twitchbot"].get("owner_id", None)
        prefix = config["twitchbot"].get("prefix", "!")
        wall_api_host = config["twitchbot"].get("wall_api_host", "127.0.0.1")
        wall_api_port = config["twitchbot"].get("wall_api_port", 80)

    except Exception as e:
        LOGGER.error("Could not parse config file: \n\t" + str(e))
        return

    async def runner() -> None:
        async with Bot(client_id=client_id, 
                       client_secret=client_secret, 
                       bot_id=bot_id, 
                       owner_id=owner_id, 
                       prefix=prefix,
                       wall_api_host=wall_api_host,
                       wall_api_port=wall_api_port) as bot:
            await bot.start()

    try:
        asyncio.run(runner())
    except KeyboardInterrupt:
        LOGGER.warning("Shutting down due to KeyboardInterrupt")


if __name__ == "__main__":
    main()
