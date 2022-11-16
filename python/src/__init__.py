from lrucache import lru


def main():
    cache = lru.LRUCache(4)

    cache.refer(1)
    cache.refer(2)
    cache.refer(3)
    cache.refer(1)
    cache.refer(4)
    cache.refer(5)
    cache.display()


if __name__ == "__main__":
    main()
