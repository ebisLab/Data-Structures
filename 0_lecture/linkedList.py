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


# li = Node(1)
# li.set_next(Node(2))
# li.next_node.next_node = Node(3)
# li.next_node.next_node.next_node = Node(4)

class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None
        # last node in the linked list
        self.tail = None

        # we dont have access to the end of the linked list
        # when we want to add to the end, we need to traverse the whole list to the end

    # its easier to start from the head
    # no traversals had to happen, we had direct access to our head and new node

    # O(1)

    def add_to_head(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:  # if list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def add_to_end(self, value):
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

            # what node do we want to add the new node to?
            # The last node in the list
            # HOW: We can get to the last node in the list by traversing it
            # current = self.head  # name the reference (current) and update i
            # while current.get_next() is not None:
            #     current = current.get_next()  # keep going
            # # we are a the end of the linked list
            # current.set_next(new_node)

# we already have access to the head of the linked list

    def remove_from_head(self):
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

    # itirate over our linked list and print each value in it i
    def print_ll_elements(self):
        current = self.head

        while current is not None:
            print(current.value)
            # update reference
            current = current.get_next()
            # or
            #current = current.next_node


ll = LinkedList()
ll.add_to_head(3)
ll.add_to_head(5)
ll.add_to_head(9)
ll.add_to_head(11)
ll.print_ll_elements()
# li = Node(1)
# li_2 = Node(2)
# li_3 = Node(3)
# li_4 = Node(4)
# li.set_next(li_2)
# li_2.set_next(li_3)
# li_3.set_next(li_4)
