class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key):
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)
    
    def contains(self, key):
        index = self._hash(key)
        return key in self.table[index]

def has_duplicates(arr):
    hash_table = HashTable(size=len(arr))
    for element in arr:
        if hash_table.contains(element):
            return True
        hash_table.insert(element)
    return False

sample_list = [10, 20, 30, 40, 50]
duplicate_list = [10, 20, 30, 10]

print("Lista sem duplicatas:", has_duplicates(sample_list))
print("Lista com duplicatas:", has_duplicates(duplicate_list))
