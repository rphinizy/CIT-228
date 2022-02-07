wars ={
    "War of Roses":["Lancaster Rose","York Rose","Tudor Rose"],
    "French Revolution":"France",
    "Battle of Dunbar":"Scotland"
}

for key, value in wars.items():
    if type(value)==list:
        print(f"The {key.title()} Was fought by")
        for v in value:
            print("\t\t\t\t",v)
    else:
        print("The", key.title(), "Was fought by", (value))
