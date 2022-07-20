# id 69445419

from typing import List, Optional


class OverFlowError(Exception):
    """Ошибка переполнения очереди."""
    pass


class EmptyDeque(Exception):
    """Очередь пуста."""
    pass


class Deque:
    """Класс двухсторонней очереди."""
    def __init__(self, max_length: int) -> None:
        self._queue: List[Optional[int]] = [None] * max_length
        self._max_length: int = max_length
        self._head: int = 0
        self._tail: int = 0
        self._size: int = 0

    def push_front(self, value: int) -> None:
        """Добавляет элемент в начало очереди."""
        if self._size < self._max_length:
            if self.is_empty():
                self._tail += 1
            self._queue[self._head] = value
            self._size += 1
            self._head = self.__get_new_index__(self._head, -1)
        else:
            raise OverFlowError('error')

    def push_back(self, value: int) -> None:
        """Добавляет элемент в конец очереди."""
        if self._size < self._max_length:
            if self.is_empty():
                self._head = self._max_length - 1
            self._queue[self._tail] = value
            self._size += 1
            self._tail = self.__get_new_index__(self._tail, 1)
        else:
            raise OverFlowError('error')

    def pop_front(self) -> int or str:
        """Удаляет элемент из начала очереди и возвращает его.
        Печатает 'error', если очередь пуста."""
        if self.is_empty():
            raise EmptyDeque('error')
        self._head = self.__get_new_index__(self._head, 1)
        result = self._queue[self._head]
        self._queue[self._head] = None
        self._size -= 1
        self.__reset_deque__()
        return result

    def pop_back(self) -> int or str:
        """Удаляет элемент из конца очереди и возвращает его.
        Печатает 'error', если очередь пуста."""
        if self.is_empty():
            raise EmptyDeque('error')
        self._tail = self.__get_new_index__(self._tail, -1)
        result = self._queue[self._tail]
        self._queue[self._tail] = None
        self._size -= 1
        self.__reset_deque__()
        return result

    def __get_new_index__(self, index, new):
        """Получение нового указателя, после добавления/удаления элемента."""
        return (index + new) % self._max_length

    def __reset_deque__(self):
        """Сброс стартовых индексов очереди, если она пуста."""
        if self.is_empty():
            self._head = self._tail = 0

    def is_empty(self) -> bool:
        """Возвращает булево значение.
        True - если очередь пуста. Иначе False."""
        return self._size == 0

    def __str__(self):
        return ' '.join(map(str, self._queue))


def main():
    """Основная логика программы."""
    comm = int(input())
    max_length = int(input())
    deque = Deque(max_length)

    for command in range(comm):
        command, *value = input().split()
        if value:
            try:
                getattr(deque, command)(int(*value))
            except OverFlowError as error:
                print(error)
        else:
            try:
                print(getattr(deque, command)())
            except EmptyDeque as error:
                print(error)


if __name__ == '__main__':
    main()

