class RandomizedSet:

    def __init__(self):
        self.num_count = {}

    def insert(self, val: int) -> bool:
        if val not in self.num_count:
            self.num_count[val] = 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.num_count:
            del self.num_count[val]
            return True
        return False

    def getRandom(self) -> int:
        present = list(self.num_count.keys())
        return random.choice(present)