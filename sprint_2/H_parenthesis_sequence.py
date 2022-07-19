class Bracket:
    def __init__(self):
        self.brackets = []

    def push(self, bracket):
        self.brackets.append(bracket)

    def pop(self):
        self.brackets.pop()

    def peek(self):
        return self.brackets[-1]

    def is_empty(self):
        return self.brackets == []


def main():
    brackets_input = input()
    brackets = {'(': ')', '[': ']', '{': '}'}
    seq = Bracket()
    for bracket in brackets_input:
        if bracket in brackets.keys():
            seq.push(bracket)
        elif not seq.is_empty() and bracket == brackets[seq.peek()]:
            seq.pop()
        else:
            seq.push(bracket)
            break
    print(seq.is_empty())


if __name__ == '__main__':
    main()
