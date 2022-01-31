usersCurrent=["Data", "Worf", "Diana", "Jordi", "admin"]
usersNew=["Barkley", "Worf", "Diana", "Riker", "Picard"]

lower_usersCurrent=[]
for user in usersCurrent:
    lower_usersCurrent.append(user.lower())

lower_usersNew=[]
for userNew in usersNew:
    lower_usersNew.append(userNew.lower())

print("Current user List:",lower_usersCurrent)
print("New User List:", lower_usersNew)

for user in lower_usersNew:
    if user in lower_usersCurrent:
        print("User name", user,"has been taken")
    if user not in lower_usersCurrent:
        print("Welcome new user", user)
