# https://www.codewars.com/kata/583203e6eb35d7980400002a/python

def gen_smile() -> list:
    smiles = []
    parts = {
        'eyes': [':', ';'],
        'noses': ['', '-', '~'],
        'mouths': [')', 'D'],
    }
    for eye in parts['eyes']:
        for nose in parts['noses']:
            for mouth in parts['mouths']:
                smiles.append(eye + nose + mouth)
    return smiles


def count_smileys(arr: list) -> int:
    result = 0
    smiles = gen_smile()
    for smile in arr:
        if smile in smiles:
            result += 1
    return result


def test():
    assert count_smileys([]) == 0
    assert count_smileys([':D', ':~)', ';~D', ':)']) == 4
    assert count_smileys([':)', ':(', ':D', ':O', ':;']) == 2
    assert count_smileys([';]', ':[', ';*', ':$', ';-D']) == 1

    assert count_smileys_re([':D', ':~)', ';~D', ':)']) == 4


def count_smileys_re(arr):
    from re import findall
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))


if __name__ == '__main__':
    test()
