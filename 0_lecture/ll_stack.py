from linkedList import LinkedList
# we must use add to head, remove from head


class LLStack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return len(self.size)

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        self.size -= 1
        return self.storage.remove_from_head()

# from collections import deque


# class ArrQueue:
#     def __init__(self):
#         self.size = 0
#         self.storage = deque()

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if self.storage:
#             return self.storage.popleft()
#         else:
#             return None
