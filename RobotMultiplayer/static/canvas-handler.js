robots = document.getElementById('robots')

socket.on("json", data => {
    robots.innerHTML = ''
    for (let player in data.players) {
        newX = data.players[player].x;
        newY = data.players[player].y;
        newRotation = data.players[player].rotation;
        robots.innerHTML +=`
        <img 
        src='../static/bot.jpg' 
        style='height: 100px; 
        transform: translate(`+newX+`px, `+newY+`px) rotate(`+newRotation+`deg)`+ `'>`
    }
});
