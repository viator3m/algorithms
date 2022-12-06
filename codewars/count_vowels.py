def solution(sentence):
    vowels = {'a': 0,
              'u': 0,
              'i': 0,
              'o': 0,
              'e': 0,}
    for letter in sentence:
        if letter in vowels:
            vowels[letter] += 1
    return sum(vowels.values())

print(solution('abracadabra'))