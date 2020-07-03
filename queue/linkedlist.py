# linked list
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
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
        if not self.head:
            # list is empty
            # update both head and tail to point to he new node
            self.head = new_node
            # self.tail = new_node

        else:
            # call set_next with the new_node on the current tail node
            current = self.head  # start at the head
            # whil there is a next node in line keep going
            while current.get_next() is not None:
                # update current to be next node in line until next_node==NONE
                current = current.get_next()

            # we are at the end of the linked list
            # current is now the last node in the list so we need to set the new node to be current next node
            current.set_next(new_node)

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            # new_node should point to current head
            new_node.next = self.head
            # move head to new node
            self.head = new_node

    def remove_head(self):  # remove and return from the head
        # both head and tail refer to he same Node
        # there's only one Node in the linked list

        if self.head is None:
            return None
        else:
            # we want to return the value at the current head
            value = self.head.get_value()
            # replace the value at the head
            # update self.head
            self.head = self.head.get_next()
            return value

    def remove_tail(self):
        # if its empty
        if not self.head:
            return None
        else:
            # temporary variable to sore our head
            temp_data = self.head

            # loop through entire list until we reach the end (None)
            while temp_data is not None:
                # create new variable for our previous node
                prev = temp_data
                temp_data = temp_data.get_next()

            # once we have reached the end of the list update prev.next to be none, which should remove our original last node
            prev.next = None
