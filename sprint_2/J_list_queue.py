class ListQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def put(self, item):
        self.queue.append(item)
        self.size += 1

    def get(self):
        if self.size == 0:
            return 'error'
        self.size -= 1
        return self.queue.pop(0)


def main():
    commands = int(input())
    queue = ListQueue()
    for command in range(commands):
        command = input().split()
        if command[0] == 'get':
            print(queue.get())
        elif command[0] == 'put':
            queue.put(command[1])
        elif command[0] == 'size':
            print(queue.size)


if __name__ == '__main__':
    main()
