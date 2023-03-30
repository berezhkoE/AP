from tasks.easy import Matrix


class HashMixin:
    def __hash__(self):
        h = 0
        for i in range(self.row):
            for j in range(self.col):
                h += (i + j + 2) * self.arr[i][j]
        return int(h)


class HashMatrix(Matrix, HashMixin):
    pass
