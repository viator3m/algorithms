def get_fibonacci_number(number, k):
    num_1, num_2 = 1, 1
    if number <= 1:
        return 1
    else:
        for _ in range(number - 1):
            num_1, num_2 = num_2, (num_2 + num_1) % 10 ** k
        return num_2


def main():
    number, k = map(int, input().split())
    result = get_fibonacci_number(number, k)
    print(result)


if __name__ == '__main__':
    main()
