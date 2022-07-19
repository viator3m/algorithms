# id 69436333

from typing import List, Optional


class Deque:
    """Класс двухсторонней очереди."""
    def __init__(self, max_length: int) -> None:
        self.queue: List[Optional[int]] = [None] * max_length
        self.max_length: int = max_length
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0

    def push_front(self, value: int) -> None:
        """Добавляет элемент в начало очереди."""
        if self.size < self.max_length:
            if self.is_empty():
                self.tail += 1
            self.queue[self.head] = value
            self.size += 1
            self.head = (self.head - 1) % self.max_length
        else:
            print('error')

    def push_back(self, value: int) -> None:
        """Добавляет элемент в конец очереди."""
        if self.size < self.max_length:
            if self.is_empty():
                self.head = self.max_length - 1
            self.queue[self.tail] = value
            self.size += 1
            self.tail = (self.tail + 1) % self.max_length
        else:
            print('error')

    def pop_front(self) -> int or str:
        """Удаляет элемент из начала очереди и возвращает его.
        Печатает 'error', если очередь пуста."""
        if self.is_empty():
            return 'error'
        self.head = (self.head + 1) % self.max_length
        result = self.queue[self.head]
        self.queue[self.head] = None
        self.size -= 1
        if self.is_empty():
            self.head = self.tail = 0
        return result

    def pop_back(self) -> int or str:
        """Удаляет элемент из конца очереди и возвращает его.
        Печатает 'error', если очередь пуста."""
        if self.is_empty():
            return 'error'
        self.tail = (self.tail - 1) % self.max_length
        result = self.queue[self.tail]
        self.queue[self.tail] = None
        self.size -= 1
        if self.is_empty():
            self.head = self.tail = 0
        return result

    def is_empty(self) -> bool:
        """Возвращает булево значение.
        True - если очередь пуста. Иначе False."""
        return self.size == 0

    def __str__(self):
        return ' '.join(map(str, self.queue))


def main():
    """Основная логика программы."""
    comm = int(input())
    max_length = int(input())
    deque = Deque(max_length)

    for command in range(comm):
        command, *value = input().split()
        if value:
            getattr(deque, command)(int(*value))
        else:
            print(getattr(deque, command)())


if __name__ == '__main__':
    main()

