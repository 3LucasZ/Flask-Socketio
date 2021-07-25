var socket = io();


socket.on("connect", () => {
    id = socket.id;
    document.getElementById("statusBar").innerText = "CONNECTED";
    console.log(id);
});

function left(){
    socket.send('left')
}
function right(){
    socket.send('right');
}
function forward(){
    socket.send('forward');
}
function back(){
    socket.send('back');
}

var leftBtn = document.getElementById('leftBtn');
var rightBtn = document.getElementById('rightBtn');
var forwardBtn = document.getElementById('forwardBtn');
var backBtn = document.getElementById('backBtn');

document.onkeydown = function (event) {
    switch (event.keyCode) {
        case 37:
            console.log("Left key is pressed.");
            leftBtn.click();
            break;
        case 38:
            console.log("Up key is pressed.");
            forwardBtn.click();
            break;
        case 39:
            console.log("Right key is pressed.");
            rightBtn.click();
            break;
        case 40:
            console.log("Down key is pressed.");
            backBtn.click();
            break;
    }
};