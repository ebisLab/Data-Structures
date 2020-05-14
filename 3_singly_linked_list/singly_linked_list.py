class Node:
    def __init__(self, value=None, next_node=None):
        # val at this linked list node

        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None
        # last node in the linked list
        self.tail = None

        # we dont have access to the end of the linked list
        # when we want to add to the end, we need to traverse the whole list to the end

    def add_to_tail(self, value):
        # regardless of if the list is empy or not, we need to wrap the value in a Node

        # value is actual value, and hasnt been wrapped in a node yet

        new_node = Node(value)
        # what if the list is empty?
        if not self.head and not self.tail:  # this is a way to write empty arrays
            # set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # what if the list isnt empty
        else:
            # set the current tail's next to the new node
            self.tail.set_next(new_node)

            # set self.tail to the new node (alter self tail and where it points to)
            self.tail = new_node

# we already have access to the head of the linked list

    def remove_head(self):
        # what if the list is empty?
        if not self.head:
            return None
            # what if it isnt empty?
        else:
            # we want to return the value at the current head
            value = self.head.get_value()  # want to over write the head

            # we want to remove the value at the head
            # update self head ---> it nees to refer the next element next in line
            self.head = self.head.get_next()
            return value


# li = Node(1)
# li_2 = Node(2)
# li_3 = Node(3)
# li_4 = Node(4)
# li.set_next(li_2)
# li_2.set_next(li_3)
# li_3.set_next(li_4)
