# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/

def snail(snail_map):
    length = len(snail_map)
    x = y = 0
    pivot = 0
    k = 0
    dx, dy = 0, 1
    result = list()
    for _ in range(1, length * length + 1):
        result.append(snail_map[x][y])
        snail_map[x][y] = None
        if not (
                0 <= x + dx < length
                and 0 <= y + dy < length
        ) or snail_map[x + dx][y + dy] is None:
            pivot += 1
            dx, dy = dy, -dx
        x += dx
        y += dy

    return result


print(snail([
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]
]))
print(snail([
    [1, 2, 3, 4, ],
    [12, 13, 14, 5, ],
    [11, 16, 15, 6, ],
    [10, 9, 8, 7, ],
]))
