from Game import Game
from func import *


class Quiz(Game):
    def __init__(self):
        super().__init__(user_name="user", num_round=0)

    def start_quiz(self):
        answers = ['א', 'ג', 'ד', 'א', 'ב', 'ג', 'ג', 'ג', 'ב', 'ד']
        questions = {
            1: "\tQuestion 1\nמה השם של אשתו של בן גוריון?\nא.פולה\nב.אסתר\nג.רות\nד.לאה",
            2: "\tQuestion 2\nהשנה שבה אסור לעבוד את האדמה היא?\nא.שנת מעשר עני\nב.שנת אור\nג.שמיטה\nד.שנת חיים",
            3: "\tQuestion 3\nבאיזו מדינה שותים סאקה?\nא.ארגנטינה\nב.ברזיל\nג.הודו\nד.יפן",
            4: "\tQuestion 4\nבתנך מי בנה את בתיבה?\nא.נח\nב.משה\nג.יפת\nד.יעקב",
            5: "\tQuestion 5\nמה המציא תומס אדיסון?\nא.מחשבון\nב.נורת חשמל\nג.מכונית\nד.תנור",
            6: "\tQuestion 6\nכל כמה שנים נערכות בחירות בישראל?\nא.9\nב.6\nג.4\nד.1",
            7: "\tQuestion 7\nאיזו מדינה מייצרת הכי הרבה קפה בעולם?\nא.אתיופיה\nב.ישראל\nג.ברזיל\nד.פריז",
            8: "\tQuestion 8\nבערך כמה בלוטות טעם יש ללשון האדם הממוצעת? \nא.5000\nב.60000\nג.10000\nד.100000000",
            9: "\tQuestion 9\nכמה לבבות יש לתמנון??\nא.1\nב.3\nג.2\nד.8",
            10: "\tBonus Question 10\nלאיזה יונק אין מיתרי קול?\nא.סרטן\nב.נחש\nג.דג\nד.ג'רפה"
        }
        counter = 0
        bonus = 0
        x1 = 0
        x2 = 0
        x3 = 0
        while self.num_round != 1:
            for (qa, an) in zip(questions.values(), answers):
                print(qa)
                user_answer = input("Enter your answer: ")
                if user_answer == an:
                    beauty(1)
                    counter += 1
                    if counter <= 3:
                        x1 += 10
                        if counter == 3:
                            print("First round points: ", x1)
                    elif 3 < counter <= 6:
                        x2 += 10
                        if counter == 6:
                            print("Second round points: ", x2)
                    elif 6 < counter <= 9:
                        x3 += 10
                        if counter == 9:
                            print("Third round points: ", x3)
                    elif counter == 10:
                        bonus += 20
                    else:
                        break
                else:
                    beauty(2)
                    counter += 1
            super().setNumRound(1)
        points = x1 + x2 + x3 + bonus
        if points > 90:
            perfect(points)
        elif points < 60:
            faild(points)
        else:
            normal(points)
