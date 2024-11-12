import random as rnd
 
class Number_geuessingGame:
    def __init__(self, min_range, max_range):
        self.min_range = min_range
        self.max_range = max_range
        self.secret_number = rnd.randint(min_range, max_range)
        self.limit = 5
    
    def guess(self,inputUser):
        if inputUser < self.secret_number:
            return "Too low. Try again."
        elif inputUser > self.secret_number:
            return "Too high. Try again."
        else:
            return "Congratulations! You guessed the correct number."
    
    def play(self):
        print("Welcome to the Number Guessing Game!")
        print(f"Guess a number between {self.min_range} and {self.max_range}.")
        while True:
            user_guess = int(input("Enter your guess: "))
            result = self.guess(user_guess)
            print(result)
            if result == "Congratulations! You guessed the correct number.":
                break
            if self.limit == 0:
                print("Sorry, you have no more attempts left.")
                break
            self.limit -= 1
    
game = Number_geuessingGame(5, 10)
game.play()
