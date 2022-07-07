import sys


def read_input() -> int:
    return int(sys.stdin.readline().strip())


def is_prime(n: int) -> bool:
    if n == 1:
        return True
    i = 2
    while i * i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def print_result(result) -> None:
    result = str(result)
    sys.stdout.write(result)


def main() -> None:
    n = read_input()
    result = is_prime(n)
    print_result(result)


if __name__ == '__main__':
    main()
