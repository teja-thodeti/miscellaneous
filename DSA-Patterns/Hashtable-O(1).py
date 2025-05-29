class MyHashtable:
    def __init__(self, size=10):
        self.bucket = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % len(self.bucket)

    def put(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.bucket[index]):
            if k == key:
                self.bucket[index][i] = (key, value)
                return
        self.bucket[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.bucket[index]:
            if k == key:
                return v
        return None
MyHashtable()
put(123,"Teja")
get(123)
