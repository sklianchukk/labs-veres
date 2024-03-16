import unittest
import find_speed_of_eating

class TestLab2(unittest.TestCase):
    def test_find_speed_of_eating(self):
        result = find_speed_of_eating.find_speed_of_eating([3, 6, 7, 11, 6, 4, 33], 10)
        self.assertEqual(result, "The monkey will eat all piles at speed of 11 bananas per hour")

    def test_find_speed_of_eating2(self):
        result = find_speed_of_eating.find_speed_of_eating([3, 6, 7, 11, 6, 4], 8)
        self.assertEqual(result, "The monkey will eat all piles at speed of 6 bananas per hour")

    def test_find_speed_of_eating3(self):
        result = find_speed_of_eating.find_speed_of_eating([3, 6, 7, 11, 6, 4, 3], 7)
        self.assertEqual(result, "The monkey will eat all piles at speed of 11 bananas per hour")

    def test_find_speed_of_eating4(self):
        result = find_speed_of_eating.find_speed_of_eating([3, 6, 7, 11, 12, 4, 18], 9)
        self.assertEqual(result, "The monkey will eat all piles at speed of 11 bananas per hour")


if __name__ == "__main__":
    unittest.main()