def eratosthenes(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for number in numbers:
        if numbers[number]:
            for j in range(number * number, n + 1, number):
                numbers[j] = False
    return numbers


print(eratosthenes(15))
