from user import User
from privileges import Privileges
from admin import Admin

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