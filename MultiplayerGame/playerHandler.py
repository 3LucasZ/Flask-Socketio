import json

class Player:
    def __init__(self, id):
        self.id = id
        self.x = 50
        self.y = 50
    def __str__(self):
        return self.id + " x: " + str(self.x) + " y: " + str(self.y)
    def left(self):
        self.x -= 1
    def forward(self):
        self.y += 1
    def right(self):
        self.x += 1
    def back(self):
        self.y -= 1
    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y
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
