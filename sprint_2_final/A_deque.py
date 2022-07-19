class Queue:
    def __init__(self, max_length):
        self.queue = [None] * max_length
        self.max_length = max_length
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_front(self, item):
        if self.size < self.max_length:
            if self.is_empty():
                self.tail += 1
            self.queue[self.head] = item
            self.size += 1
            self.head = (self.head - 1) % self.max_length
        else:
            print('error')

    def push_back(self, item):
        if self.size < self.max_length:
            if self.is_empty():
                self.head = self.max_length - 1
            self.queue[self.tail] = item
            self.size += 1
            self.tail = (self.tail + 1) % self.max_length
        else:
            print('error')

    def pop_front(self):
        if self.is_empty():
            return 'error'
        self.head = (self.head + 1) % self.max_length
        result = self.queue[self.head]
        self.queue[self.head] = None
        self.size -= 1
        if self.is_empty():
            self.head = self.tail = 0
        return result

    def pop_back(self):
        if self.is_empty():
            return 'error'
        self.tail = (self.tail - 1) % self.max_length
        result = self.queue[self.tail]
        self.queue[self.tail] = None
        self.size -= 1
        if self.is_empty():
            self.head = self.tail = 0
        return result

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        return ' '.join(map(str, self.queue))


def main():
    commands = int(input())
    max_length = int(input())
    queue = Queue(max_length)
    for command in range(commands):
        command = input().split()
        if command[0] == 'push_front':
            queue.push_front(command[1])
        elif command[0] == 'push_back':
            queue.push_back(command[1])
        elif command[0] == 'pop_front':
            print(queue.pop_front())
        elif command[0] == 'pop_back':
            print(queue.pop_back())


if __name__ == '__main__':
    main()
