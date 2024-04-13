import random

class Hero():
    def __init__(self, name, health = 100, attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0
class Game():
    def __init__(self, computer, player):
        self.computer = computer
        self.player = player
    def start(self):
        print("Игра началась")
        while self.computer.is_alive() and self.player.is_alive():
            print(f"{self.player.name} атакует {self.computer.name}")
            self.player.attack(self.computer)
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья")
            if not self.computer.is_alive():
                print(f"{self.player.name} побеждает")
                break

            print(f"{self.computer.name} атакует {self.player.name}")
            self.computer.attack(self.player)
            print(f"У {self.player.name} осталось {self.player.health} здоровья")
            if not self.player.is_alive():
                print(f"{self.computer.name} побеждает")
                break

player = Hero("Игрок Артем")
computer = Hero("Компьютер Вася")

game = Game(player, computer)
game.start()