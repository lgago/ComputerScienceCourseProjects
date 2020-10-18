'''Hashmap.py CS2420 Project 7, Luis Gago, I completed
this code without any help from other students'''
INITIAL_CAPACITY = 8

class HashMap():
    '''hashmap class'''
    def __init__(self):
        '''init function to initialize a hashmap'''
        self.buckets = [None] * INITIAL_CAPACITY
        self._size = 0
        self._capacity = INITIAL_CAPACITY

    def generate_hash(self, key):
        '''function that generates a unique has for each value'''
        if not isinstance(key, str):
            raise ValueError("Key must be a string.")
        index = 0
        for letter in key:
            index += ord(letter)
        return index % self._capacity

    def set(self, key, value):
        '''sets a hash value using the generate hash function'''
        hash_val = self.generate_hash(key)

        while(self.buckets[hash_val] is not None and key != self.buckets[hash_val][0]):
            hash_val = (hash_val + 1) % self._capacity

        if self.buckets[hash_val] is None:
            self._size += 1

        self.buckets[hash_val] = (key, value)


        if self._size / self._capacity >= .8:
            self.rehash()

    def get(self, key, default_return=None):
        '''gets the value using its hash key'''
        hash_val = self.generate_hash(key)

        if self.buckets[hash_val] is None:
            return default_return
        if self.buckets[hash_val][0] is not key:
            while(self.buckets[hash_val] is not None and key != self.buckets[hash_val][0]):
                hash_val = (hash_val + 1) % self._capacity
        if self.buckets[hash_val] is None:
            return default_return

        return self.buckets[hash_val][1]

    def size(self):
        '''returns hash map size'''
        return self._size

    def capacity(self):
        '''returns hash map capacity (how many things it could possibly hold)'''
        return self._capacity

    def rehash(self):
        '''rehash the current hash map'''
        self._capacity *= 2
        self._size = 0
        old_buckets = self.buckets
        self.buckets = [None] * self._capacity
        #go through and reset add all key value pairs from self.buckets to new HM.
        for kvp in old_buckets:
            if kvp is not None:
                self.set(kvp[0], kvp[1])

    def keys(self):
        '''return the keys of the hashmap'''
        first_tuple_elements = []

        for a_tuple in self.buckets:
            if a_tuple is not None:
                first_tuple_elements.append(a_tuple[0])
        return first_tuple_elements

    def clear(self):
        '''clear the hashmap'''
        self.buckets = [None] * INITIAL_CAPACITY
        self._capacity = INITIAL_CAPACITY
        self._size = 0
