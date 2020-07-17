class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        if self.index >= len(self.storage):
            self.storage.append(item)
        else:
            self.storage[self.index] = item

        self.index += 1
        if self.index == self.capacity:
            self.index = 0

    def get(self):
        return self.storage



if __name__ == "__main__":
    ring = RingBuffer(5)
    print("Empty Ring", ring.get())
    ring.append("a")
    ring.append("b")
    ring.append("c")
    ring.append("d")
    ring.append("e")
    ring.append("f")
    ring.append("g")
    print("Ring at Capacity", ring.get())
    