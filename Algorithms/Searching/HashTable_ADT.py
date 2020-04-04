# Abstract data type: Map, HashTable

class HashTable():
    """
    Abstract data structure for hashmap

    Instance variables:
        size: size of the hashtable
    """
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def hashfunction(self, key, size):
        return key%size
    
    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, self.size)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data   # if mapping of existing key exists replace the data
            else:
                nextslot = self.rehash(hashvalue, self.size)
                while self.slots[nextslot] != None and \
                            self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, self.size)
                
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data # replace the existing data with the same key
                
    def get(self, key):
        startslot = self.hashfunction(key, self.size)

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                            not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, self.size)
                if position == startslot:
                    stop = True
        
        return data
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        return self.put(key,data)


# def main():
#     H = HashTable(11)
#     H[54] = "cat"
#     H[26] = "dog"
#     H[93] = "lion"
#     H[17] = "tiger"
#     H[77] = "bird"
#     H[31] = "cow"
#     H[44] = "goat"
#     H[55] = "pig"
#     H[20] = "chicken"
#     print(H.slots)
#     print(H.data)
#     print(H[20])
#     print(H[17])
#     H[20] = 'duck'
#     print(H[20])
#     print(H.data)
#     print(H[99])
# main()