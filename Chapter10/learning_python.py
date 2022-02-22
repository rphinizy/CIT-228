from cgitb import text


filename='learning_python.txt'

print("******** read() ******************")
with open(filename) as textFile:
    myText=textFile.read()
print(myText)
print("**********************************\n")

print("********loop with rstrip ************")
with open(filename) as textFile:
    for line in textFile:
        print(line.rstrip())
print("*************************************\n")

print("********Store in to list ************")
with open(filename) as textFile:
    myText=textFile.readlines()
print ("Original List=", myText)
print("\n*******Print the list with loop*******")
for line in myText:
    print(line.rstrip())
print("*************************************\n")

print("\n*******Replacing You with We*******")
with open(filename) as textFile:
    for line in textFile:
        print("Original: ", line.strip())
        print("Modified: ", line.replace("you", "we"))
print("*************************************\n")

