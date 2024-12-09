import unittest
from lab4.task13.src.linked_stack import LinkedStack

class TestLinkedStack(unittest.TestCase):
    def test_stack_operations(self):
        # given
        stack = LinkedStack()

        # when
        stack.push(1)
        stack.push(2)
        stack.push(3)

        # then
        self.assertEqual(str(stack), "3 -> 2 -> 1")
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.isEmpty())

    def test_pop_empty_stack(self):
        # given
        stack = LinkedStack()

        # when / then
        with self.assertRaises(IndexError):
            stack.pop()


if __name__ == '__main__':
    unittest.main()
