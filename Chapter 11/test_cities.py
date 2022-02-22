import unittest
from city_functions import get_formatted_city

""" print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease enter a city: ")
    if city == 'q':
        break
    country = input("Please enter a country: ")
    if country == 'q':
        break
    formatted_city = get_formatted_city(city,country)
    print(f"\tFormatted City Information: {formatted_city}.") """

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_location = get_formatted_city('Rome', 'Italy')
        self.assertEqual(formatted_location, 'Rome, Italy')
    
    def test_city_country_population(self):
        formatted_location = get_formatted_city('Santiago', 'Chile', '5000000')
        self.assertEqual(formatted_location, 'Santiago, Chile Population: 5000000')

if __name__=='__main__':
    unittest.main()

