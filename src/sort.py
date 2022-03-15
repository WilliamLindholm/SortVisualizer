class Sort():
    def __init__(self, unsorted):
        self.set_data(unsorted)

    def set_data(self, unsorted):
        self.data = unsorted.copy()
        self.size = len(unsorted)
        self.steps = [self.data.copy()]

    def swap(self, i, j):
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp
        

class Bubble(Sort):
    def __init__(self, unsorted):
        super().__init__(unsorted)
    
    def sort(self):
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.data[j] > self.data[j + 1]:
                    self.swap(j, j + 1)
                    self.steps.append(self.data.copy())

class Insertion(Sort):
    def __init__(self, unsorted):
        super().__init__(unsorted)
    
    def sort(self):
        for i in range(self.size):
            j = i
            while j > 0 and self.data[j - 1] > self.data[j]:
                self.swap(j, j - 1)
                self.steps.append(self.data.copy())
                j -= 1
            i += 1

class Selection(Sort):
    def __init__(self, unsorted):
        super().__init__(unsorted)

    def sort(self):
        for i in range(self.size - 1):
            jMin = i
            for j in range(i + 1, self.size):
                if self.data[j] < self.data[jMin]:
                    jMin = j
            if jMin != i:
                self.swap(i, jMin)
                self.steps.append(self.data.copy())


class Quick(Sort):
    def __init__(self, unsorted):
        super().__init__(unsorted)

    def partition(self, lo, hi):
        pivot = self.data[hi]

        i = lo - 1

        for j in range(lo, hi):
            if self.data[j] <= pivot:
                i += 1
                self.swap(i, j)
                self.steps.append(self.data.copy())
        
        i += 1
        self.swap(i, hi)
        self.steps.append(self.data.copy())
        return i


    def sort(self, lo, hi):
        if lo >= hi or lo < 0:
            return
        p = self.partition(lo, hi)

        self.sort(lo, p - 1)
        self.sort(p + 1, hi)

