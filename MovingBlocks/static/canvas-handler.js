var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");

socket.on("json", data => {
    ctx.clearRect(0, 0, c.width, c.height);
    for (let player in data.players) {
        newX = data.players[player].x;
        newY = data.players[player].y;
        ctx.fillRect(newX, newY, 50, 50);
    }
});
