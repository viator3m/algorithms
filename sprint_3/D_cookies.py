from typing import List


def read_input():
    _ = int(input())
    greed = [int(i) for i in input().split()]
    _ = int(input())
    cookies = [int(i) for i in input().split()]
    return greed, cookies


def how_happy(greed: List[int], cookies: List[int]):
    greed.sort(reverse=True), cookies.sort(reverse=True)
    result = 0
    i = 0
    for child in greed:
        if i < len(cookies) and child <= cookies[i]:
            i += 1
            result += 1
    return result


def main():
    children, cookies = read_input()
    print(how_happy(children, cookies))


if __name__ == '__main__':
    main()
