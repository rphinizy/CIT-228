
firstBool = False
secondBool=False
answer=""

while answer !="q":

    while firstBool == False:
        firstNumber= input("Please enter your first number")
        try:
            num1=int(firstNumber)
            firstBool=True
        except ValueError:
            print("\nERROR!:")
            print("Please enter a valid number\n")
            firstBool = False

    while secondBool == False:
        secondNumber=input("Please enter your second number")
        try:
            num2=int(secondNumber)
            secondBool=True
        except ValueError:
            print("\nERROR!:")
            print("Please enter a valid number\n")
            secondBool = False

    print("Number 1 plus number 2 =", num1 + num2)
    answer=input("\nWould you like to play again? Type q to quit ")
    firstBool=False
    secondBool=False


