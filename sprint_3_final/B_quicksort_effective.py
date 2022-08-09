# id 69619774

import random
from typing import List, Dict, Tuple


def first_is_winner(player1: Dict, player2: Dict) -> bool:
    """Сравнивает двух участников соревнования.
    Возвращает True, если первый участник выиграл у второго.
    Иначе False."""
    if player1['solved'] == player2['solved']:
        if player1['penalty'] == player2['penalty']:
            return player1['name'] < player2['name']
        return player1['penalty'] < player2['penalty']
    return player1['solved'] > player2['solved']


def partition(array: List[Dict], pivot: Dict, left: int, right: int)\
        -> Tuple[int, int]:
    """Условно делит массив на две части относительно опорного элемента.
    Слева – элементы меньше. Справа – больше.
    Возвращает индексы конца левой и начала правой части.
    """
    while left <= right:
        while first_is_winner(array[left], pivot):
            left += 1
        while first_is_winner(pivot, array[right]):
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left, right


def quicksort(array: List[Dict], start: int = 0, end: int = None):
    """Быстрая сортировка in-place. Опорный элемент рандомный."""
    if end is None:
        end = len(array) - 1
    if start >= end:
        return

    pivot = array[random.randint(start, end)]

    left, right = partition(array, pivot, start, end)
    quicksort(array, start, right)
    quicksort(array, left, end)


def read_input() -> List[Dict]:
    """Считывает входные данные из стандартного ввода.
     Преобразует их в список словарей и возвращает его."""
    lines = int(input())
    players = []
    for line in range(lines):
        input_data = input().split()
        player = {'name': input_data[0],
                  'solved': int(input_data[1]),
                  'penalty': int(input_data[2])}
        players.append(player)
    return players


def main() -> None:
    """Основная логика программы."""
    players = read_input()
    quicksort(players)
    [print(i['name']) for i in players]


def test1():
    players = [
        {'name': 'za', 'solved': 0, 'penalty': 0},
        {'name': 'b', 'solved': 0, 'penalty': 0}
    ]
    quicksort(players)
    assert players[0]['name'] == 'b'
    assert players[1]['name'] == 'za'


def test2():
    players = [
        {'name': 'alla', 'solved': 4, 'penalty': 100},
        {'name': 'gena', 'solved': 6, 'penalty': 1000},
        {'name': 'gosha', 'solved': 2, 'penalty': 90},
        {'name': 'rita', 'solved': 2, 'penalty': 90},
        {'name': 'timofey', 'solved': 4, 'penalty': 80}
    ]
    quicksort(players)
    assert players[0]['name'] == 'gena'
    assert players[1]['name'] == 'timofey'
    assert players[2]['name'] == 'alla'
    assert players[3]['name'] == 'gosha'
    assert players[4]['name'] == 'rita'


if __name__ == '__main__':
    main()
