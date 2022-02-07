def make_sandwich(*toppings):
    """Print the list of toppings that have been requested."""
    print("****SANDWICH ORDER*****\n")
    print(toppings)
    print("\n***********************\n")

make_sandwich('lettus','tomato')
make_sandwich('turkey', 'cheese', 'tomato')
make_sandwich('turkey', 'cheese', 'tomato','pickles')