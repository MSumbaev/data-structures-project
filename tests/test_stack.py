"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):

    def test_node(self):
        n1 = Node(5, None)
        n2 = Node([1, 2, 3], n1)

        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)
        self.assertEqual(n2.data, [1, 2, 3])
        self.assertEqual(n2.next_node, n1)
        self.assertEqual(n2.next_node.data, 5)

    def test_stack_push(self):

        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')

        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')
        self.assertEqual(stack.top.next_node.next_node.next_node, None)

        with self.assertRaises(AttributeError):
            stack.top.next_node.next_node.next_node.data

    def test_stack_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        stack.pop()

        self.assertEqual(stack.top.data, 'data2')

    def test_str(self):
        stack = Stack()
        self.assertEqual(str(stack), '')
        stack.push('data1')
        self.assertEqual(str(stack), 'data1')
        stack.push('data2')
        self.assertEqual(str(stack), 'data2\ndata1')
        stack.pop()
        self.assertEqual(str(stack), 'data1')
