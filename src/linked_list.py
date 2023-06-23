class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is None and self.tail is None:
            self.head = self.tail = Node(data, None)
        else:
            self.head = Node(data, self.head)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.head is None and self.tail is None:
            self.head = self.tail = Node(data, None)
        else:
            node = Node(data, None)
            self.tail.next_node = node
            self.tail = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        _list = []
        _node = self.head
        if _node is None:
            return None
        else:
            while _node is not None:
                _list.append(_node.data)
                _node = _node.next_node
            return _list

    def get_data_by_id(self, id):
        _list = self.to_list()

        for el in _list:
            try:
                if id == el['id']:
                    return el
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')
