import json

def menu():
    bool = False
    while bool == False:
        try:
            selection = int(input("1-create file, 2-read file, 3-add to file, 4-quit  "))
            bool=True
        except ValueError:
            print("\nERROR!:")
            print("Please enter a valid number\n")
            bool = False
    while selection!=1 and selection!=2 and selection!=3 and selection!=4:
        print("You made an invalid selection, please try again")
        selection = int(input("1-create file, 2-read file, 3-add to file, 4-quit  "))
    return selection

def create(object):
    overwrite = input("You are about to create a new file, existing data will be overwritten (q to quit, any key to continue) ")
    if overwrite !="q":
        with open("glossary.json", "w") as write_file:
            json.dump(object, write_file, indent=4, sort_keys=True)
            print("glossary.json has been created")

def append(new_item):
    with open("glossary.json", "r+") as add_file:
        termDictionary = json.load(add_file)
        termDictionary.update(new_item)
        add_file.seek(0)
        json.dump(termDictionary, add_file, indent=4, sort_keys=True)
        print("Data has been added to numbers.json")

def read():
    try:
        with open("glossary.json") as read_file:
            termDictionary = json.load(read_file)
    except FileNotFoundError:
        print("The file doesn't exist or cannot be found.")
        print("Please make a different menu selection")      
    else: 
        for key, value in termDictionary.items():
            print(key.title(), "  Defined as: ", value)       
        
def get_key():
    term=input("Enter the new Python Term")
    newTerm=term.split()[0]
    newTerm=newTerm.lower()
    return newTerm

def get_value():
    termDef=(input("Enter the term definition"))
    return termDef

# starting values for dictionary
glossaryItems={
    "list":"A collection of items in a particular order.",
    "string":"A series of charachters.",
    "pop":"Removes the last item in a list.",
    "sort":"Arranges a list in order.",
    "slice":"A specified group of items in a list."
}

choice=menu()
while choice != 4:
    if choice == 1:
        create(glossaryItems)
    elif choice == 2:
        print("\n_________Current Terms in Glossary __________\n")
        read()
        print("\n_____________________________________________\n")
    elif choice == 3:
        terminology=get_key()
        definition=get_value()
        new_dictionary_entry={terminology:definition}
        append(new_dictionary_entry)
    else:
        print("The option you selected is not available, please try again")        
    choice=menu()