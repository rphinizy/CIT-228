users=["Data", "Worf", "Diana", "Jordi", "admin"]

print("-----------Exercise 5-8 where list has users------------")
for user in users:
    if user =="admin":
        print("Welcome", user," You are logged in with administrative powers")
    else:print ("Hello", user, " You are now logged in")
print("-----------Exercise 5-9 where list is empty------------")

del users[0:5]
if users:
   for user in users:
    if user =="admin":
        print("Welcome", user," You are logged in with administrative powers")
    else:print ("Hello", user, " You are now logged in")
else: print("We need to get some users!")