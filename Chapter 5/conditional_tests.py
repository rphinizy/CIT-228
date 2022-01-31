animal="dog"
number1=50
number2=75
names=["Sally","Dave","Fred","Amy"]

print("-------------- True Statements ---------------")
print(number1,"<", number2, number1<number2)
print(number2,">", number1, number2>number1)
print(number1,"+", number2,"= 125", number1+number2==125)
print("animal equals dog", animal =="dog")
print("Sally is on the list",'Sally' in names)

print("-------------- False Statements ---------------")
print(number1,">", number2, number1>number2)
print(number2,"<", number1, number2<number1)
print(number1,"+", number2,"= 100", number1+number2==100)
print("animal equals cat", animal =="cat")
print("Becky is on the list",'Becky' in names)