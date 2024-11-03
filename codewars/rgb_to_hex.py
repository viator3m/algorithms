# https://www.codewars.com/kata/513e08acc600c94f01000001/

def rgb(r: int, g: int, b: int) -> str:
    """
    Return RGB values to HEX.
    :param r: Red
    :type r: int

    :param g: Green
    :type g: int

    :param b: Blue
    :type b: int

    :return: HEX representation
    :rtype: str

    >>> rgb(255, 255, 255)
    'FFFFFF'
    >>> rgb(1, 2, 3)
    '010203'
    >>> rgb(-20, 275, 125)
    '00FF7D'

    """
    def trunc(x): return max(0, min(255, x))
    return f'{trunc(r):02X}{trunc(g):02X}{trunc(b):02X}'


def test():
    assert rgb(255, 255, 255) == 'FFFFFF'
    assert rgb(1, 2, 3) == '010203'
    assert rgb(-20, 275, 125) == '00FF7D'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
