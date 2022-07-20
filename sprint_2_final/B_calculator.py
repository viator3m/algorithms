# id 69445617

from operator import add, sub, mul, floordiv


class Numbers:
    """Стек для хранения чисел."""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавляет новый элемент в стек."""
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает последний элемент стека."""
        try:
            return self.items.pop()
        except IndexError:
            return


EXPRESSIONS = {
    '+': add, '-': sub,
    '*': mul, '/': floordiv,
}


def main():
    """Основная логика программы."""
    exp = input().split()
    numbers = Numbers()

    for symb in exp:
        if symb.lstrip('-').isdigit():
            numbers.push(int(symb))
        else:
            num_2, num_1 = numbers.pop(), numbers.pop()
            temp = EXPRESSIONS[symb](num_1, num_2)
            numbers.push(temp)

    print(numbers.pop())


if __name__ == '__main__':
    main()
