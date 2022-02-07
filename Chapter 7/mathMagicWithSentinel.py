import random

# I'm assuming the boolean is considered a flag while the string variable is a sentinel.
# Together they make the Sentinel Flag? Is there an industry standard for this or do you just use the form that works. 
sentinelValue=""
boolFlag =True

numberCorrect=0
numberIncorrect=0

while boolFlag ==True and sentinelValue !="q":
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

    print("You have", numberCorrect," correct answers and", numberIncorrect,"incorrect answers")
    sentinelValue=input("Would you like to play again? Type q to quit")
print("************************************************************")
print("SCORE: \n\tCORRECT:",numberCorrect,"\n\tINCORRECT",numberIncorrect,)
print("\n************************************************************")
print("Thanks for playing!")