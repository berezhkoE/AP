import numbers

import numpy as np


class MatrixAsNp(np.lib.mixins.NDArrayOperatorsMixin):
    _types = (np.ndarray, numbers.Number)

    def __init__(self, value):
        self._arr = np.asarray(value)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get("out", ())
        for x in inputs + out:
            if not isinstance(x, self._types + (MatrixAsNp,)):
                return NotImplemented

        inputs = tuple(x._arr if isinstance(x, MatrixAsNp) else x for x in inputs)

        if out:
            kwargs["out"] = tuple(x._arr if isinstance(x, MatrixAsNp) else x for x in out)

        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        if method == "at":
            return None
        return type(self)(result)

    @property
    def arr(self):
        return self._arr

    @arr.setter
    def arr(self, value):
        self._arr = value


class AdditionalOp:
    def __repr__(self):
        return f"{type(self).__name__}({self._arr})"

    def __str__(self):
        return str(self._arr)

    def write_to_file(self, file: str):
        with open(file, 'w') as file:
            file.writelines('\t'.join(str(j) for j in i) + '\n' for i in self._arr)


class Matrix(MatrixAsNp, AdditionalOp):
    pass
