class User:
        def __init__(self, first_name, last_name, user_name,password_hint1, password_hint2):
            self.first_name = first_name
            self.last_name = last_name
            self.user_name =user_name
            self.password_hint1 =password_hint1
            self.password_hint2 =password_hint2

        def describe_user(self):
            print("------------USER INFO-----------")
            print("Name:", self.first_name, self.last_name)
            print("User Name:", self.user_name)
            print("Password hints:",self.password_hint1,",",self.password_hint2)
            print("---------------------------------\n")

        def greet_user(self):
            print(f"Hello, {self.first_name} {self.last_name}. Welcome back.")