from linkedList import LinkedList


class LLQueue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_end(value)

    def dequeue(self):
        # return self.storage.
        self.size -= 1
        return self.storage.remove_from_head()
