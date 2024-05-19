import unittest
from prim_find_min_path import prim_find_min_path, read_matrix_from_csv


class TestPrimAlgorithm(unittest.TestCase):
    """
    Test prim_find_min_path.py
    """

    def test_full_connected_graph(self):
        file_path = "islands.csv"
        matrix = read_matrix_from_csv(file_path)
        self.assertEqual(prim_find_min_path(matrix), 11)

    def test_not_connected_graph(self):
        file_path = "disconnected_islands.csv"
        matrix = read_matrix_from_csv(file_path)
        self.assertEqual(
            prim_find_min_path(matrix),
            "Not all vertices are connected, check your graph",
        )


if __name__ == "__main__":
    unittest.main()
