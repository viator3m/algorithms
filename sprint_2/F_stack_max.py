class StackMax:
    def __init__(self):
        self.numbers = []

    def push(self, number):
        self.numbers.append(number)

    def pop(self):
        if self.numbers:
            return self.numbers.pop()
        print('error')

    def get_max(self):
        print(max(self.numbers) if self.numbers else None)


def read_input():
    _ = int(input())
    commands = [list(map(str, input().split())) for line in range(_)]
    return commands


def main():
    commands = read_input()
    stack = StackMax()
    for command in commands:
        try:
            eval(f'stack.{command[0]}({int(command[1])})')
        except IndexError:
            eval(f'stack.{command[0]}()')


if __name__ == '__main__':
    main()
