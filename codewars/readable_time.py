# https://www.codewars.com/kata/52685f7382004e774f0001f7

def make_readable(seconds: int) -> str:
    hh, seconds = seconds // 3600, seconds % 3600
    mm, seconds = seconds // 60, seconds % 60
    ss = seconds % 60
    return f'{hh:02d}:{mm:02d}:{ss:02d}'


def test():
    assert make_readable(120) == '00:02:00'
    assert make_readable(86399) == '23:59:59'
    assert make_readable(359999) == '99:59:59'


if __name__ == '__main__':
    test()
