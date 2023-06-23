"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


class TestQueue(unittest.TestCase):

    def test_node(self):
        n1 = Node(5, None)
        n2 = Node([1, 2, 3], n1)

        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)
        self.assertEqual(n2.data, [1, 2, 3])
        self.assertEqual(n2.next_node, n1)
        self.assertEqual(n2.next_node.data, 5)

    def test_init(self):
        ll = LinkedList()

        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})

        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.head.next_node, None)

        ll.insert_beginning({'id': 0})

        self.assertEqual(ll.head.data, {'id': 0})
        self.assertEqual(ll.head.next_node.data, {'id': 1})
        self.assertEqual(ll.head.next_node.next_node, None)

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})

        self.assertEqual(ll.head, ll.tail)
        self.assertEqual(ll.tail.data, {'id': 2})
        self.assertEqual(ll.tail.next_node, None)

        ll.insert_at_end({'id': 3})

        self.assertEqual(ll.tail.data, {'id': 3})
        self.assertEqual(ll.tail.next_node, None)
        self.assertEqual(ll.head.next_node, ll.tail)

    def test_str(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})

        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_to_list(self):
        ll = LinkedList()

        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        lst = ll.to_list()
        self.assertEqual(lst[0], {'id': 0, 'username': 'serebro'})
        self.assertEqual(lst[2], {'id': 2, 'username': 'mik.roz'})

    def test_get_data_by_id(self):
        ll = LinkedList()

        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        data_id1 = ll.get_data_by_id(1)
        data_id2 = ll.get_data_by_id(2)

        self.assertEqual(data_id1, {'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(data_id2, {'id': 2, 'username': 'mosh_s'})
