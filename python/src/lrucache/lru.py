class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.lru = {}

    def refer(self, key):
        # not present in cache
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                itemToRemove = self.cache[-1]
                self.cache.remove(itemToRemove)
                del self.lru[itemToRemove]

        # present in cache
        else:
            self.cache.remove(key)

        # update reference
        # prepend key
        self.cache.insert(0,key)
        self.lru[key] = len(self.cache) - 1

    def display(self):
        for i in self.cache:
            print(i,end=' ')
        print('')
