def eratosthenes(n):
    numbers = list(range(n))
    numbers[0] = numbers[1] = False
    for number in numbers:
        if numbers[number]:
            for j in range(number * number, n, number):
                numbers[j] = False
    return [i for i in numbers if i]


print(eratosthenes(15))
