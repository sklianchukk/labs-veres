import unittest
import prim_find_min_path

graph1 = [
    [0, 2, None, None, None],
    [None, 0, 3, 4, 5],
    [None, None, 0, 1, None],
    [None, 4, None, 0, None],
    [None, None, None, None, 0],
]

graph2 = [
    [0, 3, None, None, None],
    [None, 0, 2, 6, 4],
    [None, None, 0, 1, None],
    [None, 7, None, 0, None],
    [None, None, None, None, 0],
]

graph3 = [
    [0, 3, None, None, None, 5, None, None],
    [None, 0, 4, 7, None, None, 2, None],
    [None, None, 0, 1, None, None, None, None],
    [None, None, None, 0, 6, None, None, 8],
    [None, None, None, None, 0, 2, None, None],
    [None, None, None, None, None, 0, 4, 1],
    [None, None, None, None, 3, None, 0, None],
    [None, None, None, None, None, None, None, 0],
]


class TestPrimFindMinPath(unittest.TestCase):
    """
    Class for testing func prim_find_min_path
    """

    def test_search_pattern(self):
        result = prim_find_min_path.prim_find_min_path(graph1)
        self.assertEqual(result, 11)

    def test_search_pattern2(self):
        result = prim_find_min_path.prim_find_min_path(graph2)
        self.assertEqual(result, 10)

    def test_search_pattern3(self):
        result = prim_find_min_path.prim_find_min_path(graph3)
        self.assertEqual(result, 16)


if __name__ == "__main__":
    unittest.main()
