import json


class Mods:
    def __init__(self, name, description, icon, rewards, tips, recipe):
        self.name = name
        self.icon = icon
        self.rewards = rewards
        self.tips = tips
        self.description = description
        self.recipe = recipe
    image = ""


def load_mods():

    f = open("Data\\Mods.json", "r")
    mods = json.loads(f.read(), object_hook=lambda d: Mods(**d))
    print(mods[0].rewards)


def load_rewards():
    f = open("Data\\rewards.json", "r")

