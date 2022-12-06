# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

def solution(text: str):
    if len(text) % 2 != 0:
        text += '_'
    result = []
    for i in range(0, len(text) - 1, 2):
        result.append(f'{text[i]}' + f'{text[i + 1]}')
    return result


tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

text = 'asdfasd'
text += '_' if len(text) % 2 else text
text_format = [str(text[i] + text[i + 1]) for i in range(0, len(text), 2)]

for text, expected in tests:
    assert solution(text) == expected
    print(f'test "{text}" passed')

