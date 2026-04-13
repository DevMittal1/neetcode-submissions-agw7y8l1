class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.hasset= [[] for i in range(self.size)]
    def add(self, key: int) -> None:
        index = key%10000
        if key not in self.hasset[index]:
            self.hasset[index].append(key)

    def remove(self, key: int) -> None:
        index = key%10000
        if key in self.hasset[index]:
            self.hasset[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key%10000
        return key in self.hasset[index]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)