def power_of_four(n: int) -> bool:
    if n == 1 or n == 4:
        return True
    while n >= 4:
        n = n / 4
        if n == 4:
            return True
    return False


print(power_of_four(int(input())))
