# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/python

def max_sequence(arr: list[int]):
    try:
        temp_sum = arr[0]
    except ValueError:
        return 0
    max_sum = temp_sum
    for item in arr[1:]:
        temp_sum = max(temp_sum + item, item)
        max_sum = max(temp_sum, max_sum)
    return max(max_sum, 0)


var = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]
sequence = max_sequence(var)
assert sequence == 155
