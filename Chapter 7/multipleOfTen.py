askUser=input("Enter a number?")
askUser=int(askUser)

if askUser %10==0:
    print("Your number", askUser,"is a multiple of 10")
else:
    print("your number",askUser,"is NOT a multiple of 10")