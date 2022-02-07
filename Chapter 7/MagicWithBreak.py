import random
print("Answer the following math questions. There are 10")
problems = 10
counter=0
numberCorrect=0
numberIncorrect=0
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
        numberIncorrect+=1
        if numberIncorrect ==5:
            counter=10

    counter +=1
    print("You have", numberCorrect," correct answers and", numberIncorrect,"incorrect answers")
print("************************************************************")
print("SCORE: \n\tCORRECT:",numberCorrect,"\n\tINCORRECT",numberIncorrect,)
print("\n************************************************************")
print("Thanks for playing!")