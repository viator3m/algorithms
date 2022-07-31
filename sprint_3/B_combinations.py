KEYBOARD = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
            }


def phone_keyboard(numbers: str, combination: str = '') -> None:
    if not numbers:
        print(combination, end=' ')
        return
    for letter in KEYBOARD[numbers[0]]:
        combination += letter
        phone_keyboard(numbers[1:], combination)
        combination = combination[:-1]


if __name__ == '__main__':
    phone_keyboard(input())
