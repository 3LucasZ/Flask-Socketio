var socket = io();

socket.on("connect", () => {
    id = socket.id;
    console.log(id);
});


function left(){
    socket.send('left');
}
function right(){
    socket.send('right');
}
function forward(){
    socket.send('forward');
}
function backward(){
    socket.send('back');
}

var leftBtn = document.getElementById('leftBtn');
var forwardBtn = document.getElementById('forwardBtn');
var rightBtn = document.getElementById('rightBtn');
var backwardBtn = document.getElementById('backwardBtn');
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
            backwardBtn.click();
            break;
    }
};