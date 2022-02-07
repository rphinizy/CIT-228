rivers={
    "Nile":["Egypt","Tanzania","Kenya","Sudan", "Ethiopia", "Rwanda","Brundi","Democratic Republic"],
    "Snake":"United States",
    "Rio Grand":["United States","Mexico"]
}

print("*****Rivers and Countries*****")
for key, value in rivers.items():
    print("The", key.title(), "river is in", (value))

print("*****Rivers*****")
for key in rivers.keys():
    print(key.title())

print("*****Countries*****")
for value in rivers.values():
    print(value)