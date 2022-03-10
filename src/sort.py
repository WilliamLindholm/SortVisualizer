class Sort():
    def __init__(self, unsorted):
        self.set_data(unsorted)

    def set_data(self, unsorted):
        self.data = unsorted.copy()
        self.size = len(unsorted)
        self.steps = [self.data.copy()]

class Bubble(Sort):
    def __init__(self, unsorted):
        super().__init__(unsorted)
    
    def sort(self):
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.data[j] > self.data[j + 1]:
                    temp = self.data[j]
                    self.data[j] = self.data[j + 1]
                    self.data[j + 1] = temp
                    self.steps.append(self.data.copy())
