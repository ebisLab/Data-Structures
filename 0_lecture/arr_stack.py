class ArrStack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop()

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
