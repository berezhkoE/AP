import numpy as np


class Matrix:
    def __init__(self, arr: np.array):
        self.row, self.col = arr.shape
        self.arr = []
        for i in range(0, self.row):
            row = []
            for j in range(0, self.col):
                row.append(arr[i][j])
            self.arr.append(row)

    def __add__(self, other):
        if other.row != self.row or other.col != self.col:
            raise ValueError()

        result = []
        for i in range(0, self.row):
            row = []
            for j in range(0, self.col):
                row.append(self.arr[i][j] + other.arr[i][j])
            result.append(row)

        return self.__class__(np.array(result))

    def __matmul__(self, other):
        if self.col != other.row:
            raise ValueError()

        result = list()
        for i in range(0, self.row):
            row = []
            for j in range(0, self.col):
                el = 0
                for k in range(0, other.row):
                    el += self.arr[i][k] * other.arr[k][j]
                row.append(el)
            result.append(row)

        return self.__class__(np.array(result))

    def __mul__(self, other):
        if other.row != self.row or other.col != self.col:
            raise ValueError()

        result = []
        for i in range(0, self.row):
            row = []
            for j in range(0, self.col):
                row.append(self.arr[i][j] * other.arr[i][j])
            result.append(row)

        return self.__class__(np.array(result))
