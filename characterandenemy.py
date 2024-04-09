import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = {"Złoto": 10, "Mikstura leczenia": 0, "Miecz": 0, "Zbroja": 0, "Flaszki":0 }

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def display_status(self):
        print(f"{self.name} (hp: {self.health}, Atak: {self.attack}, Obrona: {self.defense})")
        print("Inventory:", self.inventory)

class Enemy(Character):
    def __init__(self, name, health, attack, defense, experience, loot):
        super().__init__(name, health, attack, defense)
        self.experience = experience
        self.loot = loot

    def drop_loot(self):
        loot_item = random.choice(self.loot)
        print(f"{self.name} upuszczono {loot_item}!")
        if loot_item not in self.inventory:
            self.inventory[loot_item] = 1
        else:
            self.inventory[loot_item] += 1
