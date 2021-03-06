# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        index = self._hash_mod(key)
        #checks if bucket is empty
        if self.storage[index] is not None: #bucket is not empty
            node = self.storage[index]
            while node.next is not None: #next node is not empty
                if node.key == key: #if the keys match though, overwrite the value
                    node.value = value
                    return
                node = node.next #if the keys dont match then goes to next node and repeats
            if node.key == key:
                node.value = value
            else:
                node.next = LinkedPair(key, value) #executed when the next node is None
            return
        else:
            self.storage[index] = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        #checks if the nodes keys match
        if self.storage[index].key is not key:
            node = self.storage[index]
            while node is not None:
                if node.key == key:
                    prev = node
                    prev.next = node.next
                    node = None
                    return
                node = node.next
        else:
            self.storage[index] = None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        #checks if bucket is emtpy
        if self.storage[index] is not None: #bucket has something in it
            node = self.storage[index]
            while node is not None: #goes through LL as long as node != None
                if node.key == key:
                    return node.value
                node = node.next
            print('could not find node with that key')

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        #copy over prev hash to variable
        old = self.storage.copy()
        #double capcity
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity
        #iterate through the hash
        for item in old:
            node = item
            if node is not None: #the bucket was not empty
                while node is not None:
                    self.insert(node.key, node.value)
                    node = node.next

            else:
                print('it was none')


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
