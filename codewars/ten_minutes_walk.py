# https://www.codewars.com/kata/54da539698b8a2ad76000228/


def is_valid_walk(walk: list) -> bool:
    if len(walk) != 10:
        return False
    return (walk.count('n') == walk.count('s') and
            walk.count('w') == walk.count('e'))


def test():
    assert is_valid_walk(['n', 's', 'w', 'e']) is False
    assert is_valid_walk(['n', 's', 'w']) is False
    assert is_valid_walk(
        ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']) is True
    assert is_valid_walk(
        ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']) is False
    assert is_valid_walk(
        ['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']) is False


if __name__ == '__main__':
    test()
