"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestQueue(unittest.TestCase):

    def test_node(self):
        n1 = Node(5, None)
        n2 = Node([1, 2, 3], n1)

        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)
        self.assertEqual(n2.data, [1, 2, 3])
        self.assertEqual(n2.next_node, n1)
        self.assertEqual(n2.next_node.data, 5)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')

        self.assertEqual(queue.head, queue.tail)
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node, None)

        queue.enqueue('data2')

        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.next_node, None)
        self.assertEqual(queue.tail.data, 'data2')

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.head.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertEqual(queue.head, None)

    def test_queue_str(self):
        queue = Queue()

        self.assertEqual(str(queue), '')

        queue.enqueue('data1')

        self.assertEqual(str(queue), 'data1')

        queue.enqueue('data2')

        self.assertEqual(str(queue), 'data1\ndata2')
