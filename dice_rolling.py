#  lancer du de

import random as rnd

class Dice:
    def __init__(self,sides=6):
        self.sides = sides
    
    def rool(self):
        return rnd.randint(1,self.sides)
    
    def play(self):
        while True:
            res = self.rool()
            print(f"you rooled {res}")

            choice = input("Roll again :(yes/no) :").lower()
            if choice == "no":
                print("thanks for playing !!")
                break
            elif choice!= "yes":
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue


# exemple d'utilisation
d = Dice()
d.play()