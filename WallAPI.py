import argparse
import configparser
import os
import sys
import re
import logging
import asyncio
import time
import random
from enum import Enum
import socketio
import requests
from aiohttp import web
from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(level=logging.INFO)
logging.getLogger('apscheduler.executors.default').propagate = False
LOGGER: logging.Logger = logging.getLogger(__name__)

class DisplayMode(Enum):
    AUTO = 1
    MANUAL = 2
    LAST = 3


class Emote():
    def __init__(self, name, chatter_name="", chatter_color=""):
        self.name = name
        self.timestamp = time.time()
        self.chatter_name = chatter_name
        self.chatter_color = chatter_color


# Command line args 
parser = argparse.ArgumentParser(
    prog='Emote Wall API',
    description='Controls the behavior of the Emote Wall LED Matrix and exposes API endpoints',
    epilog='Check github for more information https://github.com/chillfactor032/emote-wall-gui')
    
parser.add_argument("-c", "--config", help="path to the config file (required)", required=True)
args = parser.parse_args()

if not os.path.exists(args.config):
    LOGGER.error("Config file does not exist. Check the path and try again.")
    sys.exit(1)

# Parse the config file
config = configparser.ConfigParser()
try:
    config.read(args.config)
    emote_dir = "web/static/emotes"
    host = config["wallapi"].get("http_host", "0.0.0.0")
    port = int(config["wallapi"].get("http_port", 8080))
except ValueError as e:
    LOGGER.error("Port should be an int")
    LOGGER.error(str(e))
    sys.exit(2)
except Exception as e:
    LOGGER.error("Could not parse config file: \n\t" + str(e))
    sys.exit(2)

# Create emotes directory if it doesnt exist
if not os.path.exists(emote_dir):
    try:
        os.makedirs(emote_dir)
    except Exception as e:
        LOGGER.error(f"Could not make emote directory: {emote_dir}")
        LOGGER.error(str(e))
        sys.exit(2)
else:
    if not os.path.isdir(emote_dir):
        LOGGER.error("Emotes directory is a file. Please specify a directory")
        sys.exit(2)

#Settings
emote_dir = "web/static/emotes"
emote_web_dir = "static/emotes"
display_mode = DisplayMode.AUTO

if config["wallapi"].get("display_mode", "AUTO").upper() in DisplayMode.__members__:
    display_mode = DisplayMode[config["wallapi"].get("display_mode", "AUTO").upper()]

try:
    delay_secs = int(config["wallapi"].get("delay_secs", "10"))
except Exception:
    delay_secs = 10

try:
    pool_size = int(config["wallapi"].get("pool_size", "10"))
except Exception:
    pool_size = 10

emote_pool = []

scheduler = AsyncIOScheduler()
sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

async def index(request):
    with open('web/index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

# Add an emote to the rotation
# download it if its new
async def emote_add(request: web.Request):
    emote_id = request.query.get("id", None)
    if emote_id is None:
        return web.Response(text="Missing emote id query parameter: 'id'", status=400, content_type='text/html')
    LOGGER.info(f"New emote: [{emote_id}]")
    emote_id = filter_safe(emote_id)
    emote_url = f"https://static-cdn.jtvnw.net/emoticons/v2/{emote_id}/default/dark/3.0"
    try:
        r = requests.get(emote_url)
        r.raise_for_status()
    except Exception as e:
        LOGGER.error(f"Exception when downloading emote {emote_url}")
        LOGGER.error(str(e))
        return web.Response(text="Problem downloading emote", status=500, content_type='text/html')
    filename = ""
    if r.headers["Content-Type"] == "image/png":
        filename = emote_id+".png"
        print("PNG Emote")
    elif r.headers["Content-Type"] == "image/gif":
        filename = emote_id+".gif"
        print("Gif Emote")
    else:
        return web.Response(text=f"Invalid emote content type {r.headers['Content-Type']}", status=500, content_type='text/html')
    if not os.path.exists(os.path.join(emote_dir, filename)):
        with open(os.path.join(emote_dir, filename).replace("\\", "/"), 'wb') as f:
            f.write(r.content)
    add_emote_pool(filename)
    return web.Response(text=f"Adding emote with id {emote_id} to pool", status=200, content_type='text/html')

def add_emote_pool(emote_name):
    global emote_pool
    if emote_name in emote_pool:
        emote_pool.remove(emote_name)
    emote_pool.append(emote_name)

    while len(emote_pool) > pool_size:
        # Remove oldest Emote
        emote_pool.pop(0)

# Set Settings
async def edit_settings(request: web.Request):
    global display_mode, delay_secs, pool_size
    _secs = request.query.get("delay_secs", 1)
    _mode = request.query.get("mode", "").strip()
    _pool_size = request.query.get("pool_size", 1)
    _mode = request.query.get("mode", "").strip().lower()

    if _mode == "auto":
        display_mode = DisplayMode.AUTO
    elif _mode == "manual":
        display_mode = DisplayMode.MANUAL
    elif _mode == "last":
        display_mode = DisplayMode.LAST
    else:
        pass

    try:
        _secs = int(_secs)
        if _secs > 0:
            delay_secs = _secs
    except ValueError:
        pass
    try:
        _pool_size = int(_pool_size)
        if _pool_size > 0:
            pool_size = _pool_size
    except ValueError:
        pass
    await send_settings()
    save_config()
    LOGGER.info(f"Settings Updated - mode:{display_mode} delay_secs:{delay_secs} pool_size:{pool_size}")
    return web.Response(text="OK", status=200, content_type='text/html')

def save_config():
    global display_mode, delay_secs, pool_size
    config["wallapi"]["display_mode"] = display_mode.name.lower()
    config["wallapi"]["delay_secs"] = str(delay_secs)
    config["wallapi"]["pool_size"] = str(pool_size)
    with open(args.config, 'w') as config_file:
        config.write(config_file)

async def send_cur_emote(filename):
    await sio.emit('preview', {'path': os.path.join(emote_web_dir,filename)})

async def send_emote_pool():
    await sio.emit("emote_pool", {
        "emotes": emote_pool
    })

async def send_settings():
    await sio.emit("settings", {
        "mode": display_mode.name.lower(),
        "delay_secs": delay_secs,
        "pool_size": pool_size
    })

@sio.event
async def ping_from_client(sid):
    await sio.emit('pong_from_server', room=sid)

@sio.event
async def client_ready(sid):
    await send_settings()

# Define routes
app.router.add_static('/static', 'web/static')
app.router.add_get('/', index)
app.router.add_get('/emote_add', emote_add)
app.router.add_get('/edit_settings', edit_settings)

# Strip bad chars characters from string
filter_pattern = re.compile("[^a-zA-Z0-9_]")
def filter_safe(value):
    return filter_pattern.sub("", value)

# Get Random Emote from pool
# thats not current emote unless its the only option
def get_random_emote(cur_emote):
    global emote_pool
    if len(emote_pool) == 1:
        return emote_pool[0]
    emote = cur_emote
    while emote == cur_emote:
        emote = random.choice(emote_pool)
    return emote

tick_cnt = 0
current_emote = None

async def tick():
    global emote_pool, tick_cnt
    print(f"Tick: {tick_cnt}")
    if len(emote_pool) == 0:
        return
    
    tick_cnt += 1
    if tick_cnt < delay_secs:
        return

    emote = None
    if display_mode == DisplayMode.AUTO:
        emote = get_random_emote(current_emote)
    elif display_mode == DisplayMode.LAST:
        emote = emote_pool.pop()

    print(f"Picking New Emote: {emote}")

    if emote is not None:
        await send_cur_emote(emote)
    tick_cnt = 0

async def main():
    scheduler.add_job(tick, "interval", seconds=1)
    scheduler.start()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
