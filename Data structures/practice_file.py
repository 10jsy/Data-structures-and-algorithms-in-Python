class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next
    
    def get_data(self):
        return self.data

    def set_next(self, next_node):
        self.next = next_node

class Queue:
    def __init__(self, max_limit=None):
        self.head = None
        self.tail = None
        self.max_limit = max_limit
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.tail)
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Stack underflow")
        else:
            current_node = self.head
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next()
            self.size -= 1
            return current_node.get_data()