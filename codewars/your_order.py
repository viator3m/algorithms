# https://www.codewars.com/kata/55c45be3b2079eccff00010f/

def order(sentence: str) -> str:
    words = []
    for word in sentence.split():
        for char in word:
            if char.isdigit():
                words.append([word, int(char)])
    words.sort(key=lambda x: x[1])
    return ' '.join(i[0] for i in words)


def test():
    assert order('is2 Thi1s T4est 3a') == 'Thi1s is2 3a T4est'
    assert (order('4of Fo1r pe6ople g3ood th5e the2')
            == 'Fo1r the2 g3ood 4of th5e pe6ople')


if __name__ == '__main__':
    test()

