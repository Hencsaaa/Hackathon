import random
import os

#Játék beállítások
szelesseg = 60
magassag = 30
snake = "@"
kerites = "*"
ures = " "
kilepes = "meguntam"

#SnakeGame class
class SnakeGame:
    def __init__(self):
        self.snake_x = random.randint(1, szelesseg - 2)
        self.snake_y = random.randint(1, magassag - 2)
        self.irany = ""

#Játék pályájának megrajzolása
    def palya(self):
        os.system("cls")

        terulet = [[ures] * szelesseg for l in range(magassag)]
        terulet[self.snake_y][self.snake_x] = snake

#kerítés
        for l in range(magassag):
            terulet[l][0] = kerites
            terulet[l][szelesseg - 1] = kerites
        for h in range(szelesseg):
            terulet[0][h] = kerites
            terulet[magassag - 1][h] = kerites

#Pálya kiírása
        for sor in terulet:
            print("".join(sor))

#Mozgatás
    def move(self):
        if self.irany == "balra":
            self.snake_x -= 1
        elif self.irany == "jobbra":
            self.snake_x += 1
        elif self.irany == "fel":
            self.snake_y -= 1
        elif self.irany == "le":
            self.snake_y += 1

#A játék menete
    def start_game(self):
        print("Üdv a kígyós játékban!")
        self.palya()

        while True:
            command = input("Hova?")

            if command == kilepes:
                print("Most ennyi volt, szép napot!")
                break

            if command in ["balra", "jobbra", "fel", "le"]:
                self.irany = command
                self.move()
                if self.utkozes():
                    print("Game over! Elérted a kerítést, szép napot!")
                    break

            self.palya()

#Ha a kerítéshez hozzáér
    def utkozes(self):
        if (self.snake_x == 0 or self.snake_x == szelesseg - 1
                or self.snake_y == 0 or self.snake_y == magassag - 1):
            return True
        return False

def main():
    game = SnakeGame()
    game.start_game()

#Játék futtatása
if __name__ == "__main__":
    main()