import unittest
from restauraunt import Restaurant

class TestRestaurant(unittest.TestCase):
    """Unit Tests for the Restaurant class """
    
    def setUp(self):
        restaurant_name="Red Robin"
        cuisine_type="American"
        number_served=15000
        self.restaurant = Restaurant(restaurant_name, cuisine_type,number_served)

    def test_set_number_served_int(self):
        served=100000
        self.restaurant.set_number_served(served)
        self.assertEqual(self.restaurant.number_served,100000)

    def test_set_number_served_string(self):
        served="100000"
        self.restaurant.set_number_served(served)
        self.assertEqual(self.restaurant.number_served,100000)

    def test_increment_number_served_int(self):
        served=200
        self.restaurant.increment_number_served(served)
        self.assertEqual(self.restaurant.number_served,15200)  

    def test_increment_daily_sales_string(self):
        served="100"
        self.restaurant.increment_number_served(served)
        self.assertEqual(self.restaurant.number_served,15100)

if __name__ == '__main__':
    unittest.main()
