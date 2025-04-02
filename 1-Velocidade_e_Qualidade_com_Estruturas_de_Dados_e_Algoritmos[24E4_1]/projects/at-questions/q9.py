class HashTable:
    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, username, profile):
        index = self._hash(username)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((username, profile))

    def get(self, username):
        index = self._hash(username)
        if self.table[index] is not None:
            for key, profile in self.table[index]:
                if key == username:
                    return profile
        return None

profiles = HashTable()
profiles.insert("johndoe", {"name": "John Doe", "age": 30, "bio": "Loves coding."})
profiles.insert("janedoe", {"name": "Jane Doe", "age": 25, "bio": "Enjoys hiking."})

print(profiles.get("johndoe"))
print(profiles.get("janedoe"))
print(profiles.get("unknown"))
