import unittest
import search_pattern

class TestSearchPattern(unittest.TestCase):
    def test_search_pattern(self):
        result = search_pattern.search_pattern("КУКАРАЧІКУРВАМАЧ", "КА")
        self.assertEqual(result, "Last pattern was found at 2 and were done 18 comparisons")

    def test_search_pattern2(self):
        result = search_pattern.search_pattern("ККРАКАМАКАКУКА", "КА")
        self.assertEqual(result, "Last pattern was found at 12 and were done 19 comparisons")

    def test_search_pattern3(self):
        result = search_pattern.search_pattern("ОПТІМУСПРАЙМ", "РО")
        self.assertEqual(result, "Pattern not found")
if __name__ == "__main__":
    unittest.main()
