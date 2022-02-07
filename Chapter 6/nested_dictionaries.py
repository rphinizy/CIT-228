
puppies = {
    'Breakfast': {
        'food':"breakfast",        
        'course':"eggs",        
        'side': "bacon",
        'price': 8,
        },

    'Lunch': {
        'food':"lunch",        
        'course':"BLT",        
        'side': "fries",
        'price': 12,
        },

    'Dinner': {
        'food':"dinner",        
        'course':"chicken",        
        'side': "mac and cheese",
        'price': 18,
        },       
}


for pup, info in puppies.items():
    print(f"\nMeal: {info['food']}")
    course = info['course']
    side = info['side']
    price = info['price']

    print(f"\tcourse: {course}")
    print(f"\tside: {side}")
    print(f"\tPrice: ${price}")
