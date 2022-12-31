import win32com.client as client
from time import sleep

class Conductor:

    def __init__(self, teleport: str, heal_hp: str, heal_mp: str):
        self.client = client.Dispatch("WScript.Shell")
        self.teleport_btn = teleport
        self.heal_hp_btn = heal_hp
        self.heal_mp_btn = heal_mp

    def conductor(self, data):
        if isinstance(data["current_hp"], int) and isinstance(data["max_hp"], int):
            hp_percent = int(data["current_hp"]) / int(data["max_hp"]) * 100
            if hp_percent < 80:
                self.client.AppActivate("RotMGExalt") 
                self.client.SendKeys(self.teleport_btn)
                sleep(5)                
                return
        else:
            print ("{} or {} not int".format(data["current_hp"], data["max_hp"]))