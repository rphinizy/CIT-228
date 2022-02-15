from random import choice
from random import randint

lottery_picks=["1","7","8","16","24","36","42","65","67","99","A","Q","R","Z","X"]
winners=[]
print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
print("$$$$$$$$$$     LOTTERY TIME!     $$$$$$$$$$\n")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
input("Pres any key to see Today's Winning numbers!\n")

playAgain=""
while playAgain !="q":
    #use rantint to choose the prize for the round
   
    num=randint(1,3)
    if(num==1):
        prize="A new Car!"
    elif(num==2):
        prize="ZONK!"
    else:
        prize="$500!"
    

    #choose first number
    first_number =choice(lottery_picks)
    winners.append(first_number)

    #choose second number
    second_number=choice(lottery_picks)

    #choose a different number if duplicate
    while(second_number == first_number):
        second_number=choice(lottery_picks)
    winners.append(second_number)

    #choose third number
    third_number=choice(lottery_picks)

    #choose a different number if duplicate
    while (third_number == first_number or third_number == second_number):
        third_number=choice(lottery_picks)
    winners.append(third_number)

    #choose fourth number
    fourth_number=choice(lottery_picks)

    #choose a different number if duplicate
    while (fourth_number == first_number or fourth_number == second_number or fourth_number==third_number):
        fourth_number=choice(lottery_picks)
    winners.append(fourth_number)

    print("\n!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!")
    print("*******************************************\n")
    print("WINNING NUMBERS ARE:",winners,"\n")
    print("Today's prize:", prize)
    print("*******************************************")
    print("!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!\n")
    winners.clear()
    first_number=""
    second_number=""
    third_number=""
    fourth_number=""
    playAgain=input("press ay key to play again or q to quit")
