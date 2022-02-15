from restauraunt import Restaurant

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
