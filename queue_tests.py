import unittest
from queue import PriorityQueue

class PriorityQueue_Tests(unittest.TestCase):

    def setUp(self):
        self.queue = PriorityQueue()

    def test_Queue_can_be_created(self):
        self.assertNotEqual(self.queue, None)

    def test_queue_priority_means_something(self):
        self.queue.insert("cat", 4)
        self.queue.insert("dog", 9)
        self.assertEqual(self.queue.pop(), "cat")
        self.assertEqual(self.queue.pop(), "dog")
        self.assertEqual(self.queue.isEmpty(), True)

    def test_queue_is_fifo_for_elements_with_same_priority(self):
        self.queue.insert("cheeta", 4)
        self.queue.insert("jaguar", 4)
        self.queue.insert("dog", 9)
        self.assertEqual(self.queue.pop(), "cheeta")
        self.assertEqual(self.queue.pop(), "jaguar")
        self.assertEqual(self.queue.pop(), "dog")
        self.assertEqual(self.queue.isEmpty(), True)