# linked list
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

        # node=Node(1)
    def get_value(self):
        # returns the node's value
        return self.value

    def get_next(self):
        # returns the thing pointed at by this node's 'next' reference
        return self.next

    # update new next's velue
    def set_next(self, new_next):
        # sets this node's 'next' reference to 'new_next'
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None  # the first Node in the LL
        self.tail = None  # the last Node in the LL

    def add_to_tail(self, value):
        # adds 'value' to the end of the LL
        # wrap the 'value' in a node instance
        new_node = Node(value)

        # when case is empty (head and tail are None)
        if not self.head and not self.tail:
            #list is empty
            # update both head and tail to point to he new node
            self.head = new_node
            self.tail = new_node

        else:
            # call set_next with the new_node on the current tail node
            self.tail.set_next(new_node)
            # update self.tail to point to the new last Node in the linked list
            self.tail = new_node

    def contains(self):
        if self.head is None:
            return None

    def get_max(self):
        current = self.head
        max = self.head.value
        while current is not None:
            if current.value > max:
                max = current.value
            current = current.next

        return max

    # def remove_head(self):
    #     value = self.head.value
    #     self.

    def remove_head(self):  # remove and return from the head
        # both head and tail refer to he same Node
        # there's only one Node in the linked list

        if self.head is None:
            return None

        # save the head Node's data
        data = self.head.get_data()

        # both head and ttail refer to he same Node
        # there's only one Node in the linked list
        if self.head is self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        else:
            '''if we have more than one Node in the linked list'''
            # delete the head Node
            # update 'self.head' to refer to the Node after the Node we just deleted
            self.head = self.head.get_next()
        return data
