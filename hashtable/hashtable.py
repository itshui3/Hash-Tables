class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value): # Value is 
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        # I may need a reference to the SLL (or list)
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        h = 5381
        for l in key:
            h = (( h << 5) + h) + ord(l)
        return h & 0xffffffff

    def myHashFn(self, key):
        # assuming key is the thing I need to convert into a value
        total = 0
        for l in key:
            total += ord(l)
        return total % self.capacity

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        h = self.djb2(key)
        index = h % self.capacity
        return index

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)

        cur = self.storage[index]

        if cur is None:
            self.storage[index] = HashTableEntry(key, value)
            loadFactor = self.getSize() / self.capacity
            if loadFactor > 0.7:
                self.resize()
            return

        if cur.key == key:
            cur.value = value
            return

        while cur.next is not None:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        
        cur.next = HashTableEntry(key, value)

        loadFactor = self.getSize() / self.capacity
        if loadFactor > 0.7:
            self.resize()

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        cur = self.storage[self.hash_index(key)]
        
        while cur.key != key:
            if cur.next is None:
                return False
            cur = cur.next

        curvalue = None
        if cur.key == key:
            curvalue = cur.value
            cur.value = None

        loadFactor = self.getSize() / self.capacity
        if loadFactor > 0.7:
            self.resize()

        return curvalue

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        cur = self.storage[index]

        if cur is None:
            return False
        while cur.key != key:
            if cur.next is None:
                return False
            cur = cur.next

        return cur.value
    
    def getSize(self):
        size = 0
        for i in self.storage:
            r = i
            while r is not None:
                size += 1
                if r.next is None:
                    break
                else:
                    r = r.next
        return size

    def resize(self, capacity=None):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        if capacity is not None:
            self.capacity = capacity
        else:
            self.capacity = self.capacity * 2
        tempStor = self.storage

        self.storage = [None] * self.capacity

        for i in tempStor:
            r = i

            while r is not None:
                prev = r
                r = prev.next
                prev.next = None

                self.put(prev.key, prev.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
