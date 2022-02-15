from icecream import IceCreamStand
from restauraunt import Restaurant

print("----------------------Exercise 9-6--------------------")
storeList=[]
addFlavor =True

print("\n\nMake a database entry\n")
name = input("Enter the name of the Ice Cream Stand\n")

tempFlavors=[]

while addFlavor ==True:
   
    answer = input("Would you like to add a flavor? Type Y or N\n")

    if answer =="Y":
         flavor = input("Enter a flavor on the menu:\n") 
         tempFlavors.append(flavor)
    
    elif answer =="N":
        addFlavor =False

    else:
       print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
       print("\nERROR:Please type Y or N for your answer:\n")
       print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    
iceCreamStand=IceCreamStand(name,"dessert","10",tempFlavors)
iceCreamStand.open_restaurant()
iceCreamStand.describe_restaurant()
iceCreamStand.displayflavors()