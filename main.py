from random import randint
a = randint(1,100)
b = randint(1,100)
userAnswer = input("What is " + str(a) + " + " + str(b) + "\n")
if int(userAnswer) == a+b:
  print("\nCorrect!\n")
else:
  print("\nIncorrect, the answer is " + str(a+b) + ".\n")
