# https://www.codewars.com/kata/54e6533c92449cc251001667/python
from typing import Iterable


def unique_in_order(seq):
    new_seq = ''
    for i in range(0, len(seq)):
        if not new_seq or str(seq[i]) != new_seq[-1]:
            new_seq += str(seq[i])
    if isinstance(seq[0], int):
        new_seq = list(map(int, new_seq))
    return list(new_seq)


def test():
    assert unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    assert unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
    assert unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]

if __name__ == '__main__':
    test()

