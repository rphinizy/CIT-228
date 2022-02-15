class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

        def open_restaurant(self):
            print(f"{self.restaurant_name} is open")

    
print("----------------------Exercise 9-1--------------------")

resturaunt = Restaurant("Red Robin", "American")
print("The resturaunt name is", resturaunt.restaurant_name)
print("The resturaunt cuisine is", resturaunt.cuisine_type)

resturaunt.open_restaurant()
resturaunt.describe_restaurant()

print("----------------------Exercise 9-1--------------------")

resturaunt = Restaurant("P.F. Changs", "Asain") 
resturaunt.describe_restaurant()
resturaunt = Restaurant("Del Taco", "Mexican") 
resturaunt.describe_restaurant()
resturaunt = Restaurant("Pearl's New Orleans Kichen", "Cajun") 
resturaunt.describe_restaurant()
