# linked list


class LinkedList:
    def __init__(self):
        self.head = None  # the first Node in the LL
        self.tail = None  # the last Node in the LL

    def add_to_tail(self, data):
        # adds 'data' to the end of the LL
        # wrap the 'data' in a node instance
        new_node = Node(data)

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

    def remove_from_head(self):  # remove and return from the head
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


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

        # node=Node(1)
    def get_value(self):
        # returns the node's data
        return self.data

    def get_next(self):
        # returns the thing pointed at by this node's 'next' reference
        return self.next

    # update new next's velue
    def set_next(self, new_next):
        # sets this node's 'next' reference to 'new_next'
        self.next = new_next

    '''1'''


node = Node(1)   # 1=>N
'''2'''
node.set_next(Node(2))    # 1 => 2=> N

# CAUTION
'''3.1'''  # ndoe.set_next(Node(3))  #1 =>3 =>N

# SOLUTION
'''3.2'''
node.get_next().set_next(Node(3))  # 1=>2=>3=>N
node.get_next().get_next().set_next(Node(4))  # 1=>2=>3=>4=>N
