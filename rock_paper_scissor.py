import random as rnd
# https://www.youtube.com/watch?v=JXtwfy9cHFk :iewme

class RockPaperScissors:
    def __init__(self):
        self.choices = ["Rock","Paper","Scissors"]
    
    def get_computer_choice(self):
        return rnd.choice(self.choices)

    def winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "it's a tie"
        elif    (player_choice == self.choices[0] and computer_choice == self.choices[2]) or \
                (player_choice == self.choices[1] and computer_choice == self.choices[0]) or \
                (player_choice == self.choices[2] and computer_choice == self.choices[1]):
            return " you win"
        else: return " you lose"
    
    def play(self):
        # player_choice = input("Enter a Rock, Paper, Scissors, (q to exit) ").lower()
        print("Playing ....")
        # while True:
            # if player_choice == 'q':
            #     print("Thanks for playing")
            #     break
            # if player_choice not in self.choices:
            #     print(f'{player_choice}')
            #     print("Invalid choice: try again")
            #     # player_choice = input("Enter a Rock, Paper, Scissors, (q to exit) ")
                
            # computer_choice = self.get_computer_choice()
            # print("Computer choice: " + computer_choice)

            # res = self.winner(player_choice, computer_choice)
            # print("winner: " + res)
            
    


game = RockPaperScissors()
game.play()