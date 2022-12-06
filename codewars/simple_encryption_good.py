# https://www.codewars.com/kata/57814d79a56c88e3e0000786/
from simple_encryption import test_decrypt, test_encrypt


def decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text


def test_encrypt():
    assert encrypt("012345", 1) == "135024"
    assert encrypt("012345", 2) == "304152"
    assert encrypt("012345", 3) == "012345"

    assert encrypt("01234", 1) == "13024"
    assert encrypt("01234", 2) == "32104"
    assert encrypt("01234", 3) == "20314"

    assert encrypt("01234", -1) == "01234"
    assert encrypt('', 2) == ''


def test_decrypt():
    assert decrypt('135024', 1) == '012345'
    assert decrypt("304152", 2) == '012345'


if __name__ == '__main__':
    test_encrypt()
    test_decrypt()
