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
    def __init__(self, max_limit=1000):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_limit=max_limit

    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, new_data):
        new_node = Node(new_data)
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
        elif self.size == 1:
            current_node = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return current_node.get_data()
        else:
            current_node = self.tail
            current_node.set_next(None)
            self.size -= 1
            return current_node.get_data()