def sum_binary(x: str, y: str) -> str:
    x = list(map(int, x[::-1]))
    y = list(map(int, y[::-1]))
    for array in (x, y):
        for i in range(len(array)):
            array[i] = array[i] * (2 ** i)
    summ = sum(x) + sum(y)

    binary = ''
    while summ >= 1:
        res = summ // 2
        binary += str(summ % 2)
        summ = res

    return binary[::-1]


print(sum_binary(str(input()), str(input())))
