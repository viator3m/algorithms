def is_palindrome(text: str) -> bool:
    text = ''.join(filter(str.isalpha, text.lower()))
    reversed_text = text[::-1]
    return text == reversed_text


def main() -> None:
    print(is_palindrome(input()))


if __name__ == '__main__':
    main()