# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/python


def zeros(n):
    if n < 5:
        return 0
    return n // 5 + zeros(n // 5)


def test():
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7


if __name__ == '__main__':
    test()
