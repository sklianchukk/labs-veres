import unittest
from lab6 import find_min_beers

class TestBeerSelection(unittest.TestCase):
    def test_find_min_beers1(self):
        result = find_min_beers(2, 2, "YN NY")
        self.assertEqual(result, 2)

    def test_find_min_beers2(self):
        result = find_min_beers(3, 2, "YN YN YN")
        self.assertEqual(result, 1)

    def test_find_min_beers3(self):
        result = find_min_beers(2, 2, "NN NN")
        self.assertEqual(result, 0)

    def test_find_min_beers4(self):
        result = find_min_beers(3, 2, ["NN", "YY", "NY"])
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
