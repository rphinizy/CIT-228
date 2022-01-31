animals=["horse","pig", "cow", "chicken","goat", "sheep"]
moreAnimals=animals[:]
moreAnimals.append("duck")
moreAnimals.append("goose")
moreAnimals.append("pony")
moreAnimals.append("dog")



print("---Original List -----")
for animal in animals:
     print(animal)
print()

print("---New List -----")
for more in moreAnimals:
     print(more)

print()
print("The First 3 animals in the list are:",moreAnimals[:3])
print("The middle animals in the list are:",moreAnimals[4:7])
print("The last animals in the list are:",moreAnimals[-3:])

