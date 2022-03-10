import random

class DataClass():
    def __init__(self, size):
        self.size = size
        self.sorted = list()
        self.unsorted = list()
        self.generate_data()

    def generate_data(self):
        for i in range(self.size):
            self.sorted.append(i + 1)
            
        seq = self.sorted.copy()
        while len(seq) > 0:
            pick = random.choice(seq)
            self.unsorted.append(pick)
            seq.remove(pick)

    def print_self(self):
        print(self.sorted, self.unsorted)

    
