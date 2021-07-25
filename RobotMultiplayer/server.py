from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import playerHandler as ph
import json


app = Flask(__name__)
socketio = SocketIO(app)
players = ph.Players()


@app.route("/")
def home():
    return render_template('client.html')


@socketio.on('connect')
def connect():
    sid = request.sid
    print("New client: ", sid)
    player = ph.Player(sid)
    players.add_player(player)
    #print(players)
    send(players.to_dict(), json=True, broadcast=True)
    

@socketio.on('disconnect')
def disconnect():
    sid = request.sid
    print("Lost client: ", sid)
    player = players.find_player(sid)
    players.remove_player(player)
    #print(players)
    send(players.to_dict(), json=True, broadcast=True)


@socketio.on('message')
def handle_message(data):
    sid = request.sid
    player = players.find_player(request.sid)
    if (data) == 'forward':
        print(sid, " forward")
        player.forward()
    elif (data) == 'right':
        print(sid, " right")
        player.right()
    send(players.to_dict(), json=True, broadcast=True)



if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')