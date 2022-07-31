def gen_parenthesis(length: int, open_br: int = 0, close_br: int = 0,
                    parenthesis: str = '') -> None:
    if length * 2 == len(parenthesis):
        print(parenthesis)
    if open_br < length:
        gen_parenthesis(length, open_br + 1, close_br, parenthesis + '(')
    if close_br < open_br:
        gen_parenthesis(length, open_br, close_br + 1, parenthesis + ')')


def main():
    gen_parenthesis(int(input()))


if __name__ == '__main__':
    main()
