from math import sqrt
from typing import List


def factorize(n: int) -> List[int]:
    result = []
    for i in range(2, int(sqrt(n))+1):
        while n % i == 0:
            result.append(i)
            n = n // i
            if n == 1:
                break

    if n > 1:
        result.append(n)
    return result


result = factorize(int(input()))
print(' '.join(map(str, result)))
