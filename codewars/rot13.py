import string


def rot13(message: str) -> str:
    alphabet = {letter: '' for letter in string.ascii_letters}
    lower = string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
    upper = string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
    shift_alphabet = lower + upper
    for ind, letter in enumerate(alphabet):
        alphabet[letter] = shift_alphabet[ind]

    result = ''

    for ind, symb in enumerate(message):
        if symb.isalpha():
            result += alphabet[symb]
        else:
            result += symb

    return result


def test() -> None:
    assert rot13('test') == 'grfg'
    assert rot13('Test') == 'Grfg'
    assert rot13('aA bB zZ 1234 *!?%') == 'nN oO mM 1234 *!?%'


if __name__ == '__main__':
    test()
