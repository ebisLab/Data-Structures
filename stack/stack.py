"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import sys
sys.path.insert(1, '../singly_linked_list/singly_linked_list.py')
# from singly_linked_list import LinkedList
print(sys)


class Stack:
    def __init__(self, storage):
        self.size = 0
        # self.data = data
        # self.head = None
        # self.tail = None
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        # new_node = Node(data)

        # if self.size == 0:
        #     self.head = new_node
        #     self.tail = new_node
        # else:
        #     self.push(new_node)
        #     self.tail = new_node

    def pop(self):
        return self.storage.pop()
    #     if self.head is None:
    #         return None

    # data = self.head.get_data()

    # if self.head is self.tail:
    #     self.head = None
    #     self.tail = None
    # else:
    #     self.head = self.head.pop()
    # return data
