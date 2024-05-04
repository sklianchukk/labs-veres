import unittest
import find_min_length


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

        input_file = "input.txt"
        graph, root = lab5.read_from_input(input_file)
        length = lab5.find_min_length(graph, root)

        self.assertEqual(graph, expected_graph)
        self.assertEqual(root, expected_root)
        self.assertEqual(length, expected_length)


if __name__ == "__main__":
    unittest.main()
