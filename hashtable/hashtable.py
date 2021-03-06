class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            capacity = 8
        self.table = [None] * capacity
        self.capacity = capacity
        self.occupiedSlots = 0

    def __repr__(self):
        print()
        for l in self.table:
            if l:
                current = l
                str_ = ""
                while current:
                    print(f"({current.key}: {current.value}) -> ")
                    current = current.next
            else:
                print("(Empty)")
        return ""

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.occupiedSlots / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        hash = offset_basis
        for char in key:
            hash *= FNV_prime
            hash ^= ord(char)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hash_index = self.hash_index(key)
        entry = HashTableEntry(key, value)
        current = self.table[hash_index]

        if current:
            while current.next and current.key != key:
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = entry
                self.occupiedSlots += 1
        else:
            self.table[hash_index] = entry
            self.occupiedSlots += 1

        # Resize the hash table if needed
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hash_index = self.hash_index(key)
        current = self.table[hash_index]

        if current:
            if current.key == key:
                self.table[hash_index] = current.next
                self.occupiedSlots -= 1
            else:
                prev = current
                current = current.next

                while current:
                    if current.key == key:
                        prev.next = current.next
                        self.occupiedSlots -= 1
                        break
                    prev = current
                    current = current.next

            if self.get_load_factor() < 0.2 and self.get_num_slots() > MIN_CAPACITY:
                self.resize(self.capacity // 2)

            if current:
                return current

        print("\n*** WARNING!!! SPECIFIED VALUE DOES NOT EXISTS ***\n")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hash_index = self.hash_index(key)
        if self.table[hash_index]:
            current = self.table[hash_index]
            while current:
                if current.key == key:
                    return current.value
                current = current.next

    def reset_attrs(self, new_capacity):
        self.capacity = new_capacity
        self.table = [None] * new_capacity
        self.occupiedSlots = 0

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        prev_table = self.table
        self.reset_attrs(new_capacity)

        for l_list in prev_table:
            if l_list:
                while l_list:
                    self.put(l_list.key, l_list.value)
                    l_list = l_list.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
