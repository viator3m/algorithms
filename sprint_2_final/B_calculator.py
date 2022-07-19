class Numbers:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def calc(sign: str, num_2: int, num_1: int) -> str:
    signs = {
        '+': 'num_1 + num_2',
        '-': 'num_1 - num_2',
        '*': 'num_1 * num_2',
        '/': 'num_1 // num_2',
    }
    return f'{signs.get(sign)}'


def main():
    exp = input().split()
    numbers = Numbers()

    for symb in exp:
        if symb.lstrip('-').isdigit():
            numbers.push(int(symb))
        else:
            num_2, num_1 = numbers.pop(), numbers.pop()
            temp = eval(calc(symb, num_2, num_1))
            numbers.push(temp)

    print(numbers.pop())


if __name__ == '__main__':
    main()
