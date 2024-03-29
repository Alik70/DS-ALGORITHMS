# we use dict for hashtables.
class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.re_hash(hash_value, len(self.slots))

                while self.slots[next_slot] is not None and self.slots[next_slot] is not key:
                    next_slot = self.re_hash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    # try other hash funcs
    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def re_hash(old_hash, size):
        return (old_hash + 1) % size

    # not sure if its the best implementation.
    def get(self, key):

        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stopped = False
        found = False
        position = start_slot

        while self.slots[position] is not None and not found and not stopped:
            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.re_hash(position, len(self.slots))
                if position == start_slot:
                    stopped = True

        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)
