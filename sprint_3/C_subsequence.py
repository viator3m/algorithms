def is_subsequence(s: str, t: str) -> bool:
    index = -1
    for letter in s:
        index = t.find(letter, index + 1)
        if index == -1:
            return False
    return True


def main():
    s = input()
    t = input()
    print(is_subsequence(s, t))


if __name__ == '__main__':
    main()
