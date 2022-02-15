class User:
        def __init__(self, first_name, last_name, user_name,password_hint1, password_hint2, login_atttempts):
            self.first_name = first_name
            self.last_name = last_name
            self.user_name =user_name
            self.password_hint1 =password_hint1
            self.password_hint2 =password_hint2
            self.login_attempts= login_atttempts

        def describe_user(self):
            print("------------USER INFO-----------")
            print("Name:", self.first_name, self.last_name)
            print("User Name:", self.user_name)
            print("Password hints:",self.password_hint1,",",self.password_hint2)
            print("---------------------------------\n")

        def greet_user(self):
            print(f"Hello, {self.first_name} {self.last_name}. Welcome back.")
        
        def increment_login_attempts(self):
            self.login_attempts =int(self.login_attempts)+1
        
        def reset_login_attempts(self):
            self.login_attempts =0
            print("*******************************")
            print("LOGIN COUNTER RESET")
            print("*******************************")



user = User("Jon","Doe","A.Guy","animal","sports team","0")
user.greet_user()
user.describe_user()

user =User("Jane","Doe","A.Gal","nature","color", "0")
user.greet_user()
user.describe_user()

user =User("Frank","Smith","fSmith72","birthday","year","0")
user.greet_user()
user.describe_user()

user =User("Betty","White","bwforever","golden","girls","0")
user.greet_user()
user.describe_user()
print("Login Attempts:",user.login_attempts)
user.increment_login_attempts()
print("Login Attempts:",user.login_attempts)
user.increment_login_attempts()
print("Login Attempts:",user.login_attempts)
user.increment_login_attempts()
print("Login Attempts:",user.login_attempts)
user.increment_login_attempts()
print("Login Attempts:",user.login_attempts)
print("------RESETTING LOGIN ATTEMPTS-----")
user.reset_login_attempts()
print("Login Attempts:",user.login_attempts)