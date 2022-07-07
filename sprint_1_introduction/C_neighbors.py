from typing import List, Tuple


def read_matrix() -> List[List[int]]:
    n = int(input())
    m = int(input())
    matrix = [list(map(int, input().split())) for line in range(n)]
    return matrix


def read_position() -> Tuple[int, int]:
    row = int(input())
    col = int(input())
    return row, col


def find_neighbor(matrix: List[List[int]], row: int, col: int) -> str:
    neighbor = list()
    neighbor.append(matrix[row - 1][col]) if row - 1 >= 0 else None
    neighbor.append(matrix[row][col - 1]) if col - 1 >= 0 else None
    try:
        neighbor.append(matrix[row + 1][col])
    except IndexError:
        pass
    try:
        neighbor.append(matrix[row][col + 1])
    except IndexError:
        pass
    neighbor.sort()
    return ' '.join(map(str, neighbor))


def main():
    matrix = read_matrix()
    row, col = read_position()

    print(find_neighbor(matrix, row, col))


if __name__ == '__main__':
    main()
