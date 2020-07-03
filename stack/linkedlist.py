# linked list
class IsEmptyError(Exception):
    pass


class LinkedList:
    class Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, element):
        self.head = self.Node(element, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IsEmptyError('This stack is empty ')
        result = self.head.element
        self.head = self.head.next
        self.size -= 1
        return result

    def top(self):
        if self.is_empty():
            raise IsEmptyError('Stack is empty')
        return self.head.element
