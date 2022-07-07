def even_odd(a: int, b: int, c: int) -> str:
    all_even = (a % 2 == 0 and b % 2 == 0 and c % 2 == 0)
    all_odd = (a % 2 != 0 and b % 2 != 0 and c % 2 != 0)
    if all_even or all_odd:
        return 'WIN'
    return 'FAIL'


a, b, c = map(int, input().strip().split())
result = even_odd(a, b, c)
print(result)


