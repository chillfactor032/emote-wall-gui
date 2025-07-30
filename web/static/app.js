let progress_timer = null;
let delay_secs = 10;
let RECENT_EMOTE_MAX_SIZE = 18;
let recent_emotes = [];

function set_connected(connected){
    let icon = document.querySelector("#connected-icon");
    let ele = document.querySelector("#connected-string");
    if(connected){
        icon.name = "circle-check";
        icon.className = "connected";
        ele.innerHTML = "Websocket Connected";
    }else{
        icon.name = "circle-xmark";
        icon.className = "disconnected";
        ele.innerHTML = "Websocket Disconnected";
    }
}

function set_preview_img(src){
    let img = document.querySelector("#preview-img");
    img.src = src;
}

function add_recent_emote(emote){
    let index = recent_emotes.indexOf(emote);
    if(index !== -1){
        recent_emotes.splice(index, 1);
    }
    recent_emotes.unshift(emote);
    while(recent_emotes.length > RECENT_EMOTE_MAX_SIZE){
        recent_emotes.pop();
    }
    update_recent_emotes();
}

function update_recent_emotes(){
    let page1 = document.querySelector("#recent-emotes-carousel-page-1");
    let page2 = document.querySelector("#recent-emotes-carousel-page-2");
    page1.innerHTML = "";
    page2.innerHTML = "";

    for(let x = 0; x < recent_emotes.length; x++){
        if(x < 9){
            page1.innerHTML += `<wa-frame class="grid-emote"><img src="${recent_emotes[x]}" /></wa-frame>\n`;
        }else{
            page2.innerHTML += `<wa-frame class="grid-emote"><img src="${recent_emotes[x]}" /></wa-frame>\n`;
        }
    }
}

function progress_bar(seconds=0){
    let progress_bar_ele = document.querySelector("#progress-bar");
    progress_bar_ele.value = 0;
    clearInterval(progress_timer);

    if(seconds==0){
        return;
    }

    let tick_secs = 0.1;
    let slice = (tick_secs / seconds) * 100;
    let progress = 10;
    progress_timer = setInterval(function(){
        progress += slice;
        if(progress >= 100){
            progress = 100;
            clearInterval(progress_timer);
            console.log("Progress Stopped");
        }
        progress_bar_ele.value = progress;
    }, tick_secs * 1000);
}

function toast_success(msg){
    Toastify({
        text: msg,
        gravity: "bottom",
        position: "left",
        style: {
            background: "#00e883",
            fontWeight: "bold", 
            color: "black"},
        duration: 5000
    }).showToast();
}

function toast_error(msg){
    Toastify({
        text: msg,
        gravity: "bottom",
        position: "left",
        style: {
            background: "#5C1109",
            fontWeight: "bold", 
            color: "white"},
        duration: 5000
    }).showToast();
}

function toast_info(msg){
    Toastify({
        text: msg,
        gravity: "bottom",
        position: "left",
        style: {
            background: "#0F47CF",
            fontWeight: "bold", 
            color: "white"},
        duration: 5000
    }).showToast();
}

let timeout = null;
const socket = io("localhost");

socket.on("connect", () => {
    console.log("WS Connected"); 
    socket.emit("client_ready");
    toast_success("Websocket Connected");
    set_connected(true);
});

socket.on("disconnect", () => {
    console.log("WS Disconnected"); 
    toast_error("Websocket Disconnected");
    set_connected(false);
});

socket.on("preview", (data) => {
    console.log("Event: Preview Img Update");
    set_preview_img(data.path);
    add_recent_emote(data.path);
    toast_info("Preview Event");
    progress_bar(delay_secs);
});

socket.on("settings", (data) => {
    console.log("Event: Settings Update");
    console.log(data);
    let dm = document.querySelector("#display-mode-select");
    let ds = document.querySelector("#delay-secs-input");
    let ps = document.querySelector("#pool-size-input");
    dm.value = data.mode;
    ds.value = data.delay_secs;
    ps.value = data.pool_size;
    delay_secs = data.delay_secs;
    toast_info("Settings Refreshed");
});

async function update_settings(){
    let dm = document.querySelector("#display-mode-select");
    let ds = document.querySelector("#delay-secs-input");
    let ps = document.querySelector("#pool-size-input");
    const params = new URLSearchParams();
    params.append("mode", dm.value);
    params.append("delay_secs", ds.value);
    params.append("pool_size", ps.value);
    const response = await fetch(`edit_settings?${params}`, {method: "GET"});
}




