class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.lru = {}

    def refer(self, key):
        # not present in cache

        # present in cache

        # update reference

    def display(self):
        for i in self.cache:
            print(i,end=' ')
        print('')
