class StackMax:
    def __init__(self):
        self.numbers = []
        self.max_numbers = []

    def push(self, number):
        self.numbers.append(number)
        if self.max_numbers:
            max_n = number if number > self.max_numbers[-1]\
                else self.max_numbers[-1]
        else:
            max_n = number
        self.max_numbers.append(max_n)

    def pop(self):
        if self.numbers:
            self.max_numbers.pop()
            return self.numbers.pop()
        print('error')

    def get_max(self):
        print(self.max_numbers[-1] if self.max_numbers else None)


def main():
    commands = int(input())
    stack = StackMax()
    for command in range(commands):
        command = input().split()
        if command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'pop':
            stack.pop()
        elif command[0] == 'get_max':
            stack.get_max()


if __name__ == '__main__':
    main()
