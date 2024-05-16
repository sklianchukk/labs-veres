import unittest
from src.find_min_length import find_min_length, read_from_input


class TestMinLength(unittest.TestCase):

    def test_read_from_input(self):
        expected_graph = {
            "1": ["2", "3"],
            "2": ["4", "5"],
            "3": ["6", "7"],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
        }

        expected_root = "1"
        expected_length = 3

        input_file = "../src/input.txt"
        graph, root = read_from_input(input_file)
        length = find_min_length(graph, root)

        self.assertEqual(graph, expected_graph)
        self.assertEqual(root, expected_root)
        self.assertEqual(length, expected_length)


if __name__ == "__main__":
    unittest.main()
