class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class ListQueue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def put(self, item):
        item = Node(item)
        if self.size == 0:
            self.head = self.tail = item

        else:
            self.tail.next = item
            self.tail.next.next = self.head
            self.tail = self.tail.next

        self.size += 1

    def get(self):
        if self.size == 0:
            return 'error'

        result = self.head
        if self.size == 1:
            self.tail = self.head = None
        else:
            self.head = self.tail.next.next
            self.tail.next = self.head
        self.size -= 1
        return result

    def printed_linked(self):
        if self.size == 0:
            return None
        node = self.head
        for i in range(self.size):
            print(node.value, end=' -> ')
            node = node.next
        print('again')


def main():
    list_queue = ListQueue()
    commands = int(input())
    for command in range(commands):
        command = input().split()
        if command[0] == 'put':
            list_queue.put(command[1])
        elif command[0] == 'get':
            print(list_queue.get())
        elif command[0] == 'size':
            print(list_queue.size)


if __name__ == '__main__':
    main()