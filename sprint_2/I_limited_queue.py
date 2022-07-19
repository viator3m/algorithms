class Queue:
    def __init__(self, max_length):
        self.queue = [None] * max_length
        self.max_length = max_length
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, item):
        if self.size < self.max_length:
            self.queue[self.tail] = item
            self.size += 1
            self.tail = (self.tail + 1) % self.max_length
        else:
            print('error')

    def is_empty(self):
        return self.size == 0

    def pop(self):
        if self.is_empty():
            return None
        result = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_length
        self.size -= 1
        return result

    def peek(self):
        return self.queue[self.head]

    def __str__(self):
        return ' '.join(map(str, self.queue))


def main():
    commands = int(input())
    max_length = int(input())
    queue = Queue(max_length)
    for command in range(commands):
        command = input().split()
        if command[0] == 'push':
            queue.push(command[1])
        elif command[0] == 'pop':
            print(queue.pop())
        elif command[0] == 'peek':
            print(queue.peek())
        elif command[0] == 'size':
            print(queue.size)


if __name__ == '__main__':
    main()

