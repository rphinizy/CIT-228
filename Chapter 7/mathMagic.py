import random

problems = int(input("How many math problems would you like to practice?"))
counter=0
numberCorrect=0
while counter < problems:
    randNumber1 = random.randrange(1,1000)
    randNumber2 = random.randrange(1,1000)
    correctAnswer = int(randNumber1 + randNumber2)
    yourAnswer = int(input(f"What is the integer value of {randNumber1} + {randNumber2}?"))
    if correctAnswer==yourAnswer:
        print("Great job, you answered correctly!")
        numberCorrect +=1
    else:
        print("oops, the correct answer is", correctAnswer)
    counter +=1

print("You answered", numberCorrect, "questions correctly!")
print("Thanks for playing!")