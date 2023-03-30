import numpy as np

from tasks.easy import Matrix
from tasks.hard import HashMatrix
from tasks.medium import Matrix as Matrix_medium

add_file_name = "matrix+.txt"
mul_file_name = "matrix*.txt"
mat_mul_file_name = "matrix@.txt"


def write_to_file(file: str, m: Matrix):
    with open(file, 'w') as file:
        file.writelines('\t'.join(str(j) for j in i) + '\n' for i in m.arr)


def task1():
    np_a = np.random.randint(0, 10, (10, 10))
    np_b = np.random.randint(0, 10, (10, 10))

    A = Matrix(np_a)
    B = Matrix(np_b)

    easy_path = "artifacts/easy"
    write_to_file(f"{easy_path}/{add_file_name}", A + B)
    write_to_file(f"{easy_path}/{mul_file_name}", A * B)
    write_to_file(f"{easy_path}/{mat_mul_file_name}", A @ B)


def task2():
    np_a = np.random.randint(0, 10, (10, 10))

    A = Matrix_medium(np_a)
    B = np.random.randint(0, 10, (10, 10))

    medium_path = "artifacts/medium"
    (A + B).write_to_file(f"{medium_path}/{add_file_name}")
    (A * B).write_to_file(f"{medium_path}/{mul_file_name}")
    (A @ B).write_to_file(f"{medium_path}/{mat_mul_file_name}")


def task3():
    hard_path = "artifacts/hard"
    lists = []
    for file_name in ["A.txt", "B.txt", "C.txt", "D.txt"]:
        with open(f"{hard_path}/{file_name}", 'r') as f:
            lists.append([[int(num) for num in line.split(' ')] for line in f])

    ms = []
    for lst in lists:
        ms.append(HashMatrix(np.array(lst)))

    A, B, C, D = ms

    A_B = A @ B
    C_D = C @ D

    write_to_file(f"{hard_path}/AB.txt", A_B)
    write_to_file(f"{hard_path}/CD.txt", C_D)

    with open(f"{hard_path}/hash.txt", 'w') as file_name:
        file_name.write(str(hash(A_B)))
        file_name.write('\n')
        file_name.write(str(hash(C_D)))


if __name__ == '__main__':
    task1()
    task2()
    task3()
