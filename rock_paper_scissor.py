import random as rnd
# https://www.youtube.com/watch?v=JXtwfy9cHFk :iewme

class RockPaperScissors:
    def __init__(self):
        self.choices = ["Rock","Paper","Scissors"]
    
    def get_computer_choice(self):
        return rnd.choice(self.choices)


game = RockPaperScissors()