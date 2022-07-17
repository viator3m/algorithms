from typing import List, Tuple


def read_input() -> Tuple[int, int, List[List[int]]]:
    row = int(input())
    col = int(input())
    matrix = [list(map(int, input().split())) for line in range(row)]
    return row, col, matrix


def transposition(row: int, col: int, matrix: List[List[int]]):
    return [[matrix[i][j] for i in range(row)] for j in range(col)]


def print_result(matrix):
    for i in range(len(matrix)):
        print(*matrix[i])


if __name__ == '__main__':
    row, col, matrix = read_input()
    new_matrix = transposition(row, col, matrix)
    print_result(new_matrix)
