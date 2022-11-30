import unittest
import solution


class TestBasic(unittest.TestCase):

    def test_pass(self):
        with open("input.txt") as f:
            data = solution.parse(f.readlines())
            answer = solution.solve(data)
            self.assertEqual(580, answer)

    def test_pass_part_two(self):
        with open("input.txt") as f:
            data = solution.parse(f.readlines())
        answer = solution.repeat(data)
        self.assertEqual(81972, answer)

    def test_basic_parse(self):
        data = solution.parse('''+1
    +3
    +2'''.split())
        self.assertEqual([1, 3, 2], data)

    def test_basic_solve(self):
        data = [1, 1, -2]
        self.assertEqual(0, solution.solve(data))

    def test_basic_part_two(self):
        data = solution.parse('''+1
    -2
    +3
    +1'''.split())
        self.assertEqual(2, solution.repeat(data))


if __name__ == "__main__":
    unittest.main()
