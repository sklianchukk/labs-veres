import unittest
from src.wchain import find_longest_chain, read_file_from_input, result_file


class TestFindTheLongestChain(unittest.TestCase):
    def test_case1(self):
        words = read_file_from_input('../src/wchain_input.txt')
        result = find_longest_chain(words)
        result_file('../src/wchain_output.txt', result)
        self.assertEqual(result, 6)

    def test_case2(self):
        words = read_file_from_input('../src/wchain_input2.txt')
        result = find_longest_chain(words)
        result_file('../src/wchain_output2.txt', result)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
