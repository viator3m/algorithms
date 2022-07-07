# import sys
#
# j = sys.stdin.readline().strip()
# s = sys.stdin.readline().strip()
#
# result = 0
# for ch in s:
#     if ch in j:
#         result += 1
#
# print(result)

# a, b = (int(input()) for _ in range(2))
# print(a + b)


def double(num: int):
    return num * 2


numbers = (1, 2, 4, 5, 10)
double_numbers = tuple(map(double, numbers))

print(f'Input: {numbers}\n'
      f'Output: {double_numbers}')
