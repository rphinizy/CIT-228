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
                
class Privileges:
        def __init__(self,privileges):
            self.privileges=privileges
        def show_privileges(self):
            print(f"User has the following permissions: ")
            print("***************************")
            for p in self.privileges:
                print(p.title())
            print("***************************")

#Get new user info
fn= input("Enter the FIRST name for new administrator account\n")
ln= input("Enter the LAST name for new administrator account\n")
un= input("Enter the USERNAME for new administrator account\n")
hint1= input("Enter a PASSWORD HINT\n")
hint2= input("Enter a second PASSWORD HINT\n")
number=input("How many permisisons would you like to add?\n")

number=int(number)
counter=0
permissionList=[]
#loop for permissions
while counter<number:
    perm=input("Enter a permission\n")
    permissionList.append(perm)
    counter +=1

#instanciate a new Admin user
new_user=Admin(fn,ln,un,hint1,hint2, permissionList)

#display new user information
print("User Permiisons for:",{new_user.user_name})
new_user.greet_admin()
new_user.describe_admin()
new_user.privileges.show_privileges()

