from user import User
from privileges import Privileges

class Admin(User):
         def __init__(self, first_name, last_name, user_name,password_hint1, password_hint2,permissions):
            super().__init__(first_name, last_name, user_name,password_hint1, password_hint2)
            self.privileges=Privileges(permissions)


         def describe_admin(self):
            print("------------USER INFO-----------")
            print("Name:", self.first_name, self.last_name)
            print("User Name:", self.user_name)
            print("Password hints:",self.password_hint1,",",self.password_hint2)
            print("---------------------------------\n")

         def greet_admin(self):
            print(f"Hello, {self.first_name} {self.last_name}. Welcome back.")