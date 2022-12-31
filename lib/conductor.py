import win32com.client as client

class Conductor:

    def __init__(self, teleport: str, heal_hp: str, heal_mp: str):
        self.client = client.Dispatch("WScript.Shell")
        self.teleport_btn = teleport
        self.heal_hp_btn = heal_hp
        self.heal_mp_btn = heal_mp

    def conductor(self, data):
        print(data)
        hp_percent = int(data["current_hp"]) / int(data["max_hp"]) * 100
        if hp_percent < 80:
            self.client.AppActivate("RotMGExalt") 
            self.client.SendKeys(self.teleport_btn)
            return