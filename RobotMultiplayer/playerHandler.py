import json
import math


def toRadians (degree):
    return degree * (math.pi / 180)

class Player:
    def __init__(self, id):
        self.id = id
        self.x = 0
        self.y = 0
        self.rotation = 0
    def __str__(self):
        return self.id + " x: " + str(self.x) + " y: " + str(self.y)
    def left(self):
        self.rotation -= 5
    def right(self):
        self.rotation += 5
    def forward(self):
        self.x += (10 * math.cos(toRadians(90-self.rotation)))
        self.y += (-10 * math.sin(toRadians(90-self.rotation)))
    def back(self):
        self.x -= (10 * math.cos(toRadians(90-self.rotation)))
        self.y -= (-10 * math.sin(toRadians(90-self.rotation)))
    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "rotation": self.rotation
        }

class Players:
    def __init__(self):
        self.playerList = []
    def __str__(self):
        return str([str(player) for player in self.playerList])
    def add_player(self, player):
        self.playerList.append(player)
    def find_player(self, id):
        for player in self.playerList:
            if player.id == id:
                return player
        return "sid does not exist"
    def remove_player(self, player):
        self.playerList.remove(player)
    def to_dict(self):
        return {"players":[player.to_dict() for player in self.playerList]}
