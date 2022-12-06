def sum_positive(array: list):
    return sum([i for i in array if i > 0])


test = [1, -4, 5, 12]
assert sum_positive(test) == 18