class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hashtable = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def set(self, key, value):
        hash_index = self.hash_function(key)
        for item in self.hashtable[hash_index]:
            if item.value == key:
                item.value = value
                return
        self.hashtable[hash_index].append(Item(key, value))
    
    def get(self, key):
        hash_index = self.hash_function(key)
        for item in self.hashtable[hash_index]:
            if item.value == key:
                return item.value
        raise KeyError("Key not found")

    def remove(self, key):
        hash_index = self.hash_function(key)
        for index, item in enumerate(self.hashtable[hash_index]):
            if item.key == key:
                del self.hashtable[hash_index][index]
                return
        raise KeyError("Key not found")