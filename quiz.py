class Question:
    def __init__(self,text,options,correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        
    def is_correct(self,user_answer):
        return user_answer == self.correct_answer # bool value
    
class Quiz:
    def __init__(self):
        self.questions = []  # list of questions
        self.score = 0      # total score
        pass
    def add_question(self,question):
        self.questions.append(question)
    def start(self):
        for index, Question in enumerate(self.questions, start=1):
            print(f"{index}: qst = {Question.text}")
            for i, option in enumerate(Question.options, start=1):
                print(f"\t{i}: {option}")
            while True:
                try:
                    user_answer = int(input("your answer (1 - 4) : ")) - 1
                    if 0<= user_answer < len(Question.options):
                        break
                except ValueError:
                    print("Invalid input. Please enter a number (1-4).")
                    
            if Question.is_correct(user_answer):
                print("Correct answer")
                self.score += 1
            else:
                print("Wrong answer")
                print(f"Correct answer: {Question.options[Question.correct_answer]}")
        print(f"Your final score: {self.score}/{len(self.questions)}")

quiz = Quiz()
question1 = Question("What is the capital of France?", ["Paris", "Berlin", "London", "Madrid"], 0)
question2 = Question("What is the name of the largest island in the world?", ["Greenland", "Antarctica", "Madagascar", "Iceland"], 2)
quiz.add_question(question1)
quiz.add_question(question2)
quiz.start()