# https://www.codewars.com/kata/520b9d2ad5c005041100000f
import re


def pig_it(text: str) -> str:
    text = re.findall(r"\w+|[.,!?;]", text)
    for ind, word in enumerate(text):
        if word.isalpha():
            text[ind] = word[1:] + word[0] + 'ay'
    return ' '.join(text)


if __name__ == '__main__':
    print(pig_it('hello world !'))
