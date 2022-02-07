glossary={
    "list":"A collection of items in a particular order.",
    "string":"A series of charachters.",
    "pop":"Removes the last item in a list.",
    "sort":"Arranges a list in order.",
    "slice":"A specified group of items in a list."
}

glossary2={
    "list":"A collection of items in a particular order.",
    "string":"A series of charachters.",
    "pop":"Removes the last item in a list.",
    "sort":"Arranges a list in order.",
    "slice":"A specified group of items in a list.",
    "dictionary":"A collection of key-value pairs",
    "conditional test":"An expression that results in True of False",
    "tuple":"An immutable list",
    "nesting dictionary":"a list of items inside a dictionary",
    "method":"An action that Python can perform on a piece of data"
}

print("*************************Exercise 6-3 *****************************")
print("List:")
print("\t", glossary["list"])

print("String:")
print("\t", glossary["string"])

print("Pop:")
print("\t", glossary["pop"])

print("Sort:")
print("\t", glossary["sort"])

print("Slice:")
print("\t", glossary["slice"])

print("*************************Exercise 6-4 *****************************")

print("The following is a list of Python terms")
for term, definition in glossary2.items():
    print(term.title())
    print("\t",definition.title())

