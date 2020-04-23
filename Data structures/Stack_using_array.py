class Stack:
    def __init__(self, limit=None):
        self.stack = []
        self.limit = limit

    def push(self, data):
        if len(self.stack) >= self.limit:
            raise Exception("Stack overflow")
        else:
            self.stack.append(data)
            
    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow")
        else:
            self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def print(self):
        print(" ".join(str(i) for i in self.stack))

    def size(self):
        return len(self.stack)