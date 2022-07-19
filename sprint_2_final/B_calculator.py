# id 69435682

class Numbers:
    """Стек для хранения чисел."""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавляет новый элемент в стек."""
        self.items.append(item)

    def pop(self):
        """Удаялет и возрващает последний элемент стека."""
        return self.items.pop()


def calc(sign: str) -> str:
    """Возвращает строковое выражение в зависимости от оператора."""
    signs = {
        '+': 'num_1 + num_2',
        '-': 'num_1 - num_2',
        '*': 'num_1 * num_2',
        '/': 'num_1 // num_2',
    }
    return f'{signs.get(sign)}'


def main():
    """Основная логика программы."""
    exp = input().split()
    numbers = Numbers()

    for symb in exp:
        if symb.lstrip('-').isdigit():
            numbers.push(int(symb))
        else:
            num_2, num_1 = numbers.pop(), numbers.pop()
            temp = eval(calc(symb))
            numbers.push(temp)

    print(numbers.pop())


if __name__ == '__main__':
    main()
