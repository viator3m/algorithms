def to_binary(n: int) -> str:
    binary = ''
    while n >= 1:
        res = n // 2
        binary += str(n % 2)
        n = res
    return binary[::-1]


print(to_binary(0))
