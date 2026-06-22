from random import choice
class RandomizedSet:

    def __init__(self):
        self.secretHashmap = {}
        self.secretList = []
        

    def insert(self, val: int) -> bool:
        if val not in self.secretHashmap:
            self.secretHashmap[val] = len(self.secretList)
            self.secretList.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.secretHashmap:
            valindex = self.secretHashmap[val]
            lastval = self.secretList[-1]

            self.secretList[valindex] = lastval
            self.secretHashmap[lastval] = valindex

            del self.secretHashmap[val]
            self.secretList.pop()
            return True
        else:
            return False

#             Save the index of val.
# Save the last value in the list.
# Move that last value into the removed index.
# Set that moved value’s hashmap entry to the removed index.
# Delete val and pop the list.
        

    def getRandom(self) -> int:
        return choice(self.secretList)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()