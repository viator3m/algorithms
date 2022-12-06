# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(l):
    return [i for i in l if isinstance(i, int)]


def test():
    assert filter_list([1, 2, 'a', 'b']) == [1, 2]


if __name__ == '__main__':
    test()
