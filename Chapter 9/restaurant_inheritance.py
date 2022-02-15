class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, number_served):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.number_served= number_served

        def describe_restaurant(self):
            print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

        def open_restaurant(self):
            print(f"{self.restaurant_name} is open")
        
        def set_number_served(self, served):
            self.number_served=int(served)

        def increment_number_served(self, served):
            self.number_served+=int(served)


class IceCreamStand(Restaurant):
     def __init__(self, restaurant_name, cuisine_type, number_served, flavor_name):
          super().__init__(restaurant_name, cuisine_type, number_served)
          self.flavor_name=flavor_name

     def displayflavors(self):
         print("\n*******************")
         print("Todays flavors:")
         print("~*~*~*~*~*~*~*~*~*~*~*~*~\n")
         for f in self.flavor_name:
             print(f.title())  
         print("\n~*~*~*~*~*~*~*~*~*~*~*~*~")

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