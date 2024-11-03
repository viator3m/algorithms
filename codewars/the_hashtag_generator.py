# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

def generate_hashtag(text: str) -> str:
    text = text.strip().split()
    text = list(map(str.capitalize, text))
    return ''.join(['#'] + text) if 0 < sum((len(i) for i in text)) <= 140 else False


if __name__ == '__main__':
    assert generate_hashtag(' Hello there thanks for trying my Kata') == ('HelloThereThanksForTryingMyKata')
