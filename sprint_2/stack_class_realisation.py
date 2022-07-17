class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return '\n'.join(self.items[::-1])


fruits = Stack()

fruits.push('orange')
fruits.push('banana')
fruits.push('apple')


print(fruits)
