import random
import os

""" with open("guests.txt","w") as fileObject:
      fileObject.write(input("Enter a Name"))



answer=input("Enter a Name for the guest book or type q to quit")
with open("guest_book.txt","a") as fileObject:
    while answer != 'q':
        answer+="\n"
        fileObject.write(answer)
        print("Welcome to the guest list", answer)
        answer=input("Enter a Name for the guest book or type q to quit") """

filename="rooms.txt"

if os.path.exists(filename):
    os.remove(filename)
rooms=[]
with open (filename,"w") as roomsFile:
    guest = input("Please enter your name or type q to quit")
    while guest != "q":
        number=random.randint(1,50)
        while number in rooms:
            number =random.randint(1,50)
        print(f"{guest} you will be in room# {number}")
        rooms.append(number)
        guest +=", room# " + str(number) + "\n"
        roomsFile.write(guest)
        guest = input("Please enter the next Guest name or q to quit")
    
with open(filename) as roomsFile:
    print("____________________Rooms Assigned__________________")
    for line in roomsFile:
        print(line)







