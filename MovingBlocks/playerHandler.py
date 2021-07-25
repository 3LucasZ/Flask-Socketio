import json

class Player:
    def __init__(self, id):
        self.id = id
        self.x = 0
        self.y = 0
    def __str__(self):
        return self.id + " x: " + str(self.x) + " y: " + str(self.y)
    def left(self):
        self.x -= 10
    def forward(self):
        self.y -= 10
    def right(self):
        self.x += 10
    def back(self):
        self.y += 10
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
