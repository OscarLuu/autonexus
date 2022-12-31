

class Conductor:

    def __init__(self, teleport: str, heal_hp: str, heal_mp: str):
        self.teleport = teleport
        self.heal_hp = heal_hp
        self.heal_mp = heal_mp

    def conductor(self, data):
        print (data)