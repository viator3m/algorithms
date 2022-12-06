# https://www.codewars.com/kata/57814d79a56c88e3e0000786/

def decrypt(encrypted_text: str, n: int) -> str:
    if not encrypted_text:
        return encrypted_text
    length = len(encrypted_text)
    temp = [''] * length
    while n > 0:
        nxt = 0
        for ind in range(0, length, 2):
            temp[ind] = encrypted_text[length // 2 + nxt]
            nxt += 1
        nxt = 0
        for ind in range(1, length, 2):
            temp[ind] = encrypted_text[nxt]
            nxt += 1
        n -= 1
        encrypted_text = ''.join(temp)

    return ''.join(encrypted_text)


def encrypt(text: str, n: int) -> str:
    if not text:
        return text
    temp = ''
    new_text = text
    while n > 0:
        for ind in range(1, len(new_text), 2):
            temp += new_text[ind]
        for ind in range(0, len(new_text), 2):
            temp += new_text[ind]
        new_text = temp
        temp = ''
        n -= 1

    return new_text


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
