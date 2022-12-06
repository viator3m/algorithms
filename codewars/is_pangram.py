# https://www.codewars.com/kata/545cedaa9943f7fe7b000048


import string


def is_pangram(s):
    alphabet = string.ascii_lowercase
    s = s.lower().replace(' ', '')
    for letter in s:
        alphabet = alphabet.replace(letter, '')
    return False if alphabet else True


def test():
    phrase = 'The quick brown fox jumps over the lazy dog'
    phrase_2 = 'hello world'
    phrase_3 = 'Pack my box with five dozen liquor jugs'
    assert is_pangram(phrase) is True
    assert is_pangram(phrase_2) is False
    assert is_pangram(phrase_3) is True
    assert is_pangram('') is False


if __name__ == '__main__':
    test()
