class HashTable:
    def __init__(self):
        self.size = 11 #arbitrary but use prime number to have easier time resolving collisions
        self.keys = [None] * self.size #initialise list of keys of length size and using None values
        self.values = [None] * self.size  #initialise list of values corresponding to keys of length size and using None values

    #simple remainder hash function
    def hash_function(self, key, size):
        return key & size
    
    #open addressing using linear probing technique with offset +1
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def put(self, key, value):
        hashvalue = self.hash_function(key, len(self.keys))

        if self.keys[hashvalue] == None:
            self.keys[hashvalue] = key
            self.values[hashvalue] = value
        else:
            if self.keys[hashvalue] == key:
                self.values[hashvalue] = value #if key already exists in table, replace old data with new data
            else:
                next_slot = self.rehash(hashvalue, len(self.keys))
                while self.keys[next_slot] is not None and self.keys[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.keys))

                if self.keys[next_slot] == None:
                    self.keys[next_slot] = key
                    self.values[next_slot] = value
                else:
                    self.values[next_slot] = value #replace old data with new data

    def get(self, key):
        start_slot = self.hash_function(key, len(self.keys))
        
        value = None
        stop = False
        found = False
        pos = start_slot

        while self.values[pos] is not None and not found and not stop:
            if self.keys[pos] == key:
                found = True
                value = self.values[pos]
            else:
                pos = self.rehash(pos, len(self.keys))
                if pos == start_slot:
                    stop = True
        return value

    #overloading methods to allow access using []
    def __getitem__(self, key):
        return self.get(key)

    def __putitem__(self, key, value):
        self.put(key, value)