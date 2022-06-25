class Array:
    def __init__(self, arr = []):
        self.arr = arr

    def bubble_sort(self):
        n = len(self.arr)
        for i in range(0, n - 1):
            for j in range(0, n - 1 - i):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
        return self.arr
