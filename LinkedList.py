class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

    def get_data(self):
        return self.data

class LinkedList:
    def __init__(self, data=None):
        self.head = Node(data)
    
    def insert_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.get_next() is not None:  #Think why it is .get_next not just current_node
            current_node = current_node.get_next()
        current_node.set_next(new_node)

    def insert_specific(self, specific, new_data):
        if self.head is None:
            raise Exception("Empty list, cannot insert at location")
        else:
            current_node = self.head
            new_node = Node(new_data)
            while current_node.get_data() != specific:
                current_node = current_node.get_next()
            new_node.set_next(current_node.get_next())
            current_node.set_next(new_node)
    
    def delete(self, delete_data):
        if self.head is None:
            raise Exception("Empty list")
        current_node = self.head
        if current_node.get_data() == delete_data:
            self.head = current_node.get_next()
        else:
            while current_node is not None:
                next_node = current_node.get_next()
                if next_node.get_data() == delete_data:
                    current_node.set_next(next_node.get_next())
                    current_node = None
                else:
                    current_node = next_node
            return ("Not found in list")

    def traverse(self):
        stringify_list = ""
        if self.head is None:
            return stringify_list
        else:
            current_node = self.head
            while current_node is not None:
                stringify_list += str(current_node.get_data()) + " -> "
                current_node = current_node.get_next()
            print(stringify_list)

    def search(self, search_data):
        current_node = self.head
        while current_node is not None:
            if current_node.get_data() == search_data:
                return True
            else:
                current_node = current_node.get_next()
        return False