class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.tail = None
        self.head = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        self.tail = Node(data, None)
        if self.head == None:
            self.head = self.tail
        else:
            foll = self.head
            while foll.next_node != None:
                foll = foll.next_node
            foll.next_node = self.tail

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head == None:
            # print("Очередь пустая.")
            return None
        else:
            rmv_data = self.head.data
            self.head = self.head.next_node
        return rmv_data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        info = ""
        if self.head != None:
            foll = self.head
            info = foll.data

            while foll.next_node != None:
                info += f"\n{foll.next_node.data}"
                foll = foll.next_node
        return f"{info}"
