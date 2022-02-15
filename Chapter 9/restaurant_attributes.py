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


print("----------------------Exercise 9-4--------------------")
resturaunt = Restaurant("Del Taco", "Mexican","10") 
resturaunt.open_restaurant()
resturaunt.describe_restaurant()
#printing number served
print("The number of customers served is:",resturaunt.number_served)
resturaunt.number_served =12
print("The current number of customers served is:",resturaunt.number_served)

#using method to changed number served
served=input("How many customers have been served?")
resturaunt.set_number_served(served)
print("The current number of customers served is:",resturaunt.number_served)

#adding customers served using increment_number_served
resturaunt.increment_number_served(served)
print("The total number of customers served is:",resturaunt.number_served)
