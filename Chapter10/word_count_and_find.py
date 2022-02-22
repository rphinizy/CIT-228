
from re import search


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def find_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.lower().split()
        num_words = words.count(searchWord)
        print(f"The file {filename} has the word '{searchWord}' {num_words} times.")




filenames = ['hitch_hikers_guide_to_the_galaxy.txt', 'LOTR.txt', 'red_shirts.txt']
print("___________HOW MANY WORDS IN A FILE_________")
print("********************************************")
for filename in filenames:
    count_words(filename)
print("********************************************\n")

searchWord=input("Enter the word you would like to count").lower()

print(f"___________COUNT THE WORD '{searchWord}'_________")
print("********************************************")
for filename in filenames:
    find_words(filename)
print("********************************************")