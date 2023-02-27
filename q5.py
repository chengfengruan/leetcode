import queue


class AnimalShelf:

    def __init__(self):
        self.cat = queue.Queue(20000)
        self.dog = queue.Queue(20000)

    def enqueue(self, animal: list[int]) -> None:
        if animal[1] == 0:
            self.cat.put(animal[0])
        else:
            self.dog.put(animal[0])

    def dequeueAny(self) -> list[int]:
        if len(self.cat) == 0 and len(self.dog) == 0:
            return [-1, -1]
        elif len(self.cat) > 0 and len(self.dog) > 0:
            if self.cat[0][0] > self.dog[0][0]:
                return [self.cat.get(), 0]
            else:
                return [self.dog.get(), 1]
        elif len(self.cat) == 0:
            return [self.dog.get(), 1]
        else:
            return [self.cat.get(), 0]

    def dequeueDog(self) -> list[int]:
        if len(self.dog) == 0:
            return [-1, -1]
        return [self.dog.get(), 1]

    def dequeueCat(self) -> list[int]:
        if len(self.cat) == 0:
            return [-1, -1]
        return [self.cat.get(), 0]


# Your AnimalShelf object will be instantiated and called as such:
obj = AnimalShelf()
obj.enqueue(animal)
param_2 = obj.dequeueAny()
param_3 = obj.dequeueDog()
param_4 = obj.dequeueCat()
