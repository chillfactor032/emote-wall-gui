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

function toast_success(msg){
    Toastify({
        text: msg,
        gravity: "bottom",
        position: "left",
        backgroundColor: "#00e883",
        style: {fontWeight: "bold", color: "black"},
        duration: 5000
    }).showToast();
}

function toast_error(msg){
    Toastify({
        text: msg,
        gravity: "bottom",
        position: "left",
        backgroundColor: "#5C1109",
        style: {fontWeight: "bold", color: "white"},
        duration: 5000
    }).showToast();
}

function toast_info(msg){
    Toastify({
        text: msg,
        gravity: "bottom",
        position: "left",
        backgroundColor: "#0F47CF",
        style: {fontWeight: "bold", color: "white"},
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
    toast_info("Preview Event");
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




