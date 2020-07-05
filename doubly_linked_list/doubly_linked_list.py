"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # None (we dont need them there, set explicetly) because of the previous and next node
        new_node = ListNode(value)
        self.length += 1
        # if list is currently empty add node to that case
        if not self.head and not self.tail:  # w can also just say if self.head is None
            self.head = new_node
            self.tail = new_node
        else:  # lis already has elements in it
            # prepend -> new node's nxt value point to current had
            new_node.next = self.head  # it becomes old head
            self.head.prev = new_node
            # we need new head to know that it's pointer is the old head
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # postpend
            new_node.prev = self.tail  # it becomes old head
            self.tail.next = new_node
            # we need new head to know that it's pointer is the old head
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return
        self.add_to_head(node.value)
        self.delete(node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return
        self.add_to_tail(node.value)
        self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # scenario - list is empty -> do nothing
        # list is only one node
        # node is the HEAD node (so make sue we handle the head poiner correctly)
        # node is the TAIL node (mak sure tail is handled correctly)
        # the node is just some node in the list

        # planning
        self.length -= 1
        # this is the only node
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # its the head
        elif node is self.head:
            # reassign head
            self.head = node.next
            # update pointer
            node.delete()
        # its the tail
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # its in the middle
        else:
            # node is getting passed anyway, we can just delete it
            node.delete()  # we have afunction thatdoes that for us

    """Returns the highest value currently in the list"""

    def get_max(self):
        # how to get max
        # create max var
        current = self.head
        max = self.head.value
        # loop through nodes
        while current is not None:
            # compare value in node
            if current.value > max:
                max = current.value

            current = current.next

        # return max found
        return max


# """Each ListNode holds a reference to its previous node
# as well as its next node in the List."""


# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next

#     """Wrap the given value in a ListNode and insert it
#     after this node. Note that this node could already
#     have a next node it is point to."""

#     def insert_after(self, value):
#         current_next = self.next
#         self.next = ListNode(value, self, current_next)
#         if current_next:
#             current_next.prev = self.next

#     """Wrap the given value in a ListNode and insert it
#     before this node. Note that this node could already
#     have a previous node it is point to."""

#     def insert_before(self, value):
#         current_prev = self.prev
#         self.prev = ListNode(value, current_prev, self)
#         if current_prev:
#             current_prev.next = self.prev

#     """Rearranges this ListNode's previous and next pointers
#     accordingly, effectively deleting this ListNode."""

#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev


# """Our doubly-linked list class. It holds references to
# the list's head and tail nodes."""


# class DoublyLinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 1 if node is not None else 0

#     def __len__(self):
#         return self.length

#     """Wraps the given value in a ListNode and inserts it
#     as the new head of the list. Don't forget to handle
#     the old head node's previous pointer accordingly."""

#     def add_to_head(self, value):
#         new_node = ListNode(value)
#         self.length += 1
#         if not self.head and not self.tail:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             # prepend
#             new_node.next = self.head  # it becomes old head
#             self.head.prev = new_node
#             # we need new head to know that it's pointer is the old head
#             self.head = new_node

#     """Removes the List's current head node, making the
#     current head's next node the new head of the List.
#     Returns the value of the removed Node."""

#     def remove_from_head(self):
#         value = self.head.value
#         self.delete(self.head)
#         return value

#     """Wraps the given value in a ListNode and inserts it
#     as the new tail of the list. Don't forget to handle
#     the old tail node's next pointer accordingly."""

#     def add_to_tail(self, value):
#         new_node = ListNode(value)
#         self.length += 1
#         if not self.head and not self.tail:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             # postpend
#             new_node.prev = self.tail  # it becomes old head
#             self.tail.next = new_node
#             # we need new head to know that it's pointer is the old head
#             self.tail = new_node

#     """Removes the List's current tail node, making the
#     current tail's previous node the new tail of the List.
#     Returns the value of the removed Node."""

#     def remove_from_tail(self):
#         value = self.tail.value
#         self.delete(self.tail)
#         return value

#     """Removes the input node from its current spot in the
#     List and inserts it as the new head node of the List."""

#     def move_to_front(self, node):
#         if node is self.head:
#             return
#         self.add_to_head(node.value)
#         self.delete(node)

#     """Removes the input node from its current spot in the
#     List and inserts it as the new tail node of the List."""

#     def move_to_end(self, node):
#         if node is self.tail:
#             return
#         self.add_to_tail(node.value)
#         self.delete(node)

#     """Removes a node from the list and handles cases where
#     the node was the head or the tail"""

#     def delete(self, node):
#         # planning
#         self.length -= 1
#         # this is the only node
#         if self.head is self.tail:
#             self.head = None
#             self.tail = None
#         # its the head
#         elif node is self.head:
#             # reassign head
#             self.head = node.next
#             # update pointer
#             node.delete()
#         # its the tail
#         elif node is self.tail:
#             self.tail = node.prev
#             node.delete()
#         # its in the middle
#         else:
#             # node is getting passed anyway, we can just delete it
#             node.delete()  # we have afunction thatdoes that for us

#     """Returns the highest value currently in the list"""

#     def get_max(self):
#         # how to get max
#         # create max var
#         current = self.head
#         max = self.head.value
#         # loop through nodes
#         while current is not None:
#             # compare value in node
#             if current.value > max:
#                 max = current.value

#             current = current.next

#         # return max found
#         return max
