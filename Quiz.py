def beauty(x):
  correct = "תשובה נכונה!"
  discorrect = "אתה טועה!"
  if x == 1:
    print("************", correct, "************", sep="\n")
  else:
    print("^^^^^^^^^",discorrect,"^^^^^^^^^" ,sep="\n")


def Quiz():
 name = input("Enter your name: ")
 print(name,"welcome To The Quiz!\nסבב ראשון !")

 x1 = 0
 x2 = 0
 x3 = 0
 y = 0
 while y < 3:
  print("\tQuestion 1\nמה השם של אשתו של בן גוריון?\nא.פולה\nב.אסתר\nג.רות\nד.לאה")
  A1 = input("התשובה שלך:")
  if A1 == 'א':
   beauty(1)
   x1 += 10
  else:
    beauty(2)
  print("\tQuestion 2\nהשנה שבה אסור לעבוד את האדמה היא?\nא.שנת מעשר עני\nב.שנת אור\nג.שמיטה\nד.שנת חיים")
  A2 = input("התשובה שלך:")
  if A2 == "ג":
    beauty(1)
    x1 += 10
  else:
    beauty(2)
  print("\tQuestion 3\nבאיזו מדינה שותים סאקה?\nא.ארגנטינה\nב.ברזיל\nג.הודו\nד.יפן")
  a3 = input("תשובה שלך :")
  if a3 == "ד":
      beauty(1)
      x1 += 10
  else:
      beauty(2)
  print("ניקוד סבב ראשון :",x1)
  y += 1

  print("סבב שני !")
  print("\tQuestion 4\nבתנך מי בנה את בתיבה?\nא.נח\nב.משה\nג.יפת\nד.יעקב")
  A1 = input("התשובה שלך:")
  if A1 == 'א':
   beauty(1)
   x2 += 10
  else:
    beauty(2)
  print("\tQuestion 5\nמה המציא תומס אדיסון?\nא.מחשבון\nב.נורת חשמל\nג.מכונית\nד.תנור")
  A2 = input("התשובה שלך:")
  if A2 == "ב":
    beauty(1)
    x2 += 10
  else:
    beauty(2)
  print("\tQuestion 6\nכל כמה שנים נערכות בחירות בישראל?\nא.9\nב.6\nג.4\nד.1")
  A1 = input("התשובה שלך:")
  if A1 == 'ג':
   beauty(1)
   x2 += 10
  else:
    beauty(2)
  print("ניקוד סבב שני :",x2)
  y += 1

  print("סבב שלישי ואחרון !")
  print("\tQuestion 7\nאיזו מדינה מייצרת הכי הרבה קפה בעולם?\nא.אתיופיה\nב.ישראל\nג.ברזיל\nד.פריז")
  A2 = input("התשובה שלך:")
  if A2 == "ג":
    beauty(1)
    x3 += 10
  else:
    beauty(2)
  print("\tQuestion 8\nבערך כמה בלוטות טעם יש ללשון האדם הממוצעת? \nא.5000\nב.60000\nג.10000\nד.100000000")
  A2 = input("התשובה שלך:")
  if A2 == "ג":
    beauty(1)
    x3 += 10
  else:
    beauty(2)
  print("\tQuestion 9\nכמה לבבות יש לתמנון??\nא.1\nב.3\nג.2\nד.8")
  A2 = input("התשובה שלך:")
  if A2 == "ב":
    beauty(1)
    x3 += 10
  else:
    beauty(2)
  print("\tBonus Question 10\nלאיזה יונק אין מיתרי קול?\nא.סרטן\nב.נחש\nג.דג\nד.ג'רפה")
  A2 = input("התשובה שלך:")
  if A2 == "ד":
     beauty(1)
     x3 += 20
  else:
        beauty(2)
  y += 1
 sum_of = x1+x2+x3
 if sum_of > 90:
    print("מושלם !!!",name)
    print("סהכ נקודות :",sum_of)
 elif sum_of < 60:
    print("סהכ נקודות :", sum_of,"נסה שוב")
 else:
    print("סהכ נקודות :", sum_of)


Quiz()