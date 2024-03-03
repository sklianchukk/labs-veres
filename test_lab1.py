import unittest
import lab1

class TestLab1(unittest.TestCase):
    def test_findNumber1(self):
        result = lab1.find_number([15, 7, 22, 9, 36, 2, 42, 18], 3)
        self.assertEqual(result, f"Sorted array: [2, 7, 9, 15, 18, 22, 36, 42]; \nYour number: 22; "
                                 f"\nNumber`s position in unsorted array: 2.")

    def test_findNumber2(self):
        result = lab1.find_number([15, 17, 22, 9, 26, 12, 42, 18], 2)
        self.assertEqual(result, f"Sorted array: [9, 12, 15, 17, 18, 22, 26, 42]; \nYour number: 26; "
                                 f"\nNumber`s position in unsorted array: 4.")

    def test_findNumber3(self):
        result = lab1.find_number([16, -1, 9, 22, 30, 37, 5, -9, 3, 38], 5)
        self.assertEqual(result, f"Sorted array: [-9, -1, 3, 5, 9, 16, 22, 30, 37, 38]; \nYour number: 16; "
                                 f"\nNumber`s position in unsorted array: 0.")

    def test_findNumber4(self):
        result = lab1.find_number([3, 5, 2, 15, 12, 5, 2, 5, 2, 18, 42, 4, 7], 4)
        self.assertEqual(result, f"Sorted array: [2, 2, 2, 3, 4, 5, 5, 5, 7, 12, 15, 18, 42]; \nYour number: 12; "
                                 f"\nNumber`s position in unsorted array: 4.")

if __name__ == "__main__":
    unittest.main()