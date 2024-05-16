import unittest
from src.heap_based_priority_queue import HeapQueue, Node

class TestHeapBasedPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.heap = HeapQueue()

    def test_insert(self):
        heap = HeapQueue()
        heap.insert(3, 3)
        heap.insert(5, 2)
        heap.insert(4, 1)

        self.assertEqual(heap.queue[0].priority, 3)
        self.assertEqual(heap.queue[1].priority, 2)
        self.assertEqual(heap.queue[2].priority, 1)

    def test_delete(self):
        heap = HeapQueue()
        heap.insert(3, 3)
        heap.insert(5, 2)
        heap.insert(4, 1)

        heap.delete()
        self.assertEqual(len(heap.queue), 2)

        heap.delete()
        heap.delete()
        self.assertEqual(len(heap.queue), 0)

if __name__ == "__main__":
    unittest.main()
