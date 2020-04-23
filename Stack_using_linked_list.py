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

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.limit = limit
        self.size = 0

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow")
        else:
            current_node = self.top_item
            self.top_item = current_node.get_next()
            self.size -= 1
            return current_node.get_data()

    def push(self, new_data):
        if self.has_space():
            new_node = Node(new_data)
            new_node.set_next(self.top_item)
            self.top_item = new_node
            self.size += 1
        else:
            raise Exception("Stack overflow")

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top_item.get_data()

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.limit > self.size