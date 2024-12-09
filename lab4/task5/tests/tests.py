import unittest
from lab4.task5.src.max_stack import MaxStack

class TestMaxStack(unittest.TestCase):
    def test_operations(self):
        # given
        stack = MaxStack()

        # when
        stack.push(2)
        stack.push(1)
        max1 = stack.max()
        stack.pop()
        max2 = stack.max()
        stack.push(7)
        max3 = stack.max()

        # then
        self.assertEqual(max1, 2)
        self.assertEqual(max2, 2)
        self.assertEqual(max3, 7)

    def test_empty_stack(self):
        # given
        stack = MaxStack()

        # when
        max_value = stack.max()

        # then
        self.assertIsNone(max_value)


if __name__ == '__main__':
    unittest.main()
