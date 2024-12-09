import unittest
from lab4.task13.src.linked_queue import LinkedQueue

class TestLinkedQueue(unittest.TestCase):
    def test_queue_operations(self):
        # given
        queue = LinkedQueue()

        # when
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # then
        self.assertEqual(str(queue), "1 <- 2 <- 3")
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertTrue(queue.isEmpty())

    def test_dequeue_empty_queue(self):
        # given
        queue = LinkedQueue()

        # when / then
        with self.assertRaises(IndexError):
            queue.dequeue()


if __name__ == '__main__':
    unittest.main()
