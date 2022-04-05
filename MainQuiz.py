from Quizz import Quiz
from func import *
class Main(Quiz):
    def quiz(self):
        super().setUserName(input("Enter username: "))
        open(super().getUserName())
        print("First Round !")
        super().start_quiz()
