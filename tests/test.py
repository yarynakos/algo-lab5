import unittest

from src.main import find_min_depth


class TestTreeMethods(unittest.TestCase):
    def test_find_min_depth(self):
        find_min_depth('input1.txt', 'output1.txt')
        with open('output1.txt', 'r') as file:
            lines = file.readlines()
            result = int(lines[0].strip())
            self.assertEqual(4, result)

        find_min_depth('input2.txt', 'output2.txt')
        with open('output2.txt', 'r') as file:
            lines = file.readlines()
            result = int(lines[0].strip())
            self.assertEqual(1, result)
