# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/

import itertools


def permutations(s: str):
    s = list(itertools.permutations(s))
    return sorted(list(set([''.join(s[i]) for i in range(len(s))])))


def test():
    assert permutations('aabb') == ['aabb', 'abab', 'abba', 'baab', 'baba',
                                    'bbaa']
    assert permutations('a') == ['a']


if __name__ == '__main__':
    test()
