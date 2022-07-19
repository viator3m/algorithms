def get_fibonacci_number(n):
    if n == 0 or n == 1:
        return 1
    return get_fibonacci_number(n - 1) + get_fibonacci_number(n - 2)


def main():
    number = int(input())
    result = get_fibonacci_number(number)
    print(result)


if __name__ == '__main__':
    main()
