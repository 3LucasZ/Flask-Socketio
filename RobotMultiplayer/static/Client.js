var socket = io();


socket.on("connect", () => {
    id = socket.id;
    document.getElementById("statusBar").innerText = "CONNECTED";
    console.log(id);
});


function right(){
    socket.send('right');
}
function forward(){
    socket.send('forward');
}

var forwardBtn = document.getElementById('forwardBtn');
var rightBtn = document.getElementById('rightBtn');

document.onkeydown = function (event) {
    switch (event.keyCode) {
        case 38:
            console.log("Up key is pressed.");
            forwardBtn.click();
            break;
        case 39:
            console.log("Right key is pressed.");
            rightBtn.click();
            break;
    }
};