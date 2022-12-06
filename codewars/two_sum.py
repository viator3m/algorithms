# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

def two_sum(numbers: list[int], target: int) -> tuple[int] or None:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                numbers[i] = None
                result = (i, j)
                return result
    return None


assert two_sum([1, 2, 3], 4) == (0, 2)
assert two_sum([1234, 5678, 9012], 14690) == (1, 2)
assert two_sum([2, 2, 3], 4) == (0, 1)
