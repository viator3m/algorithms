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


def gen_parenthesis(n, parenthesis=''):
    if n == 0:
        brackets = {'(': ')', '[': ']', '{': '}'}
        seq = Bracket()
        for bracket in parenthesis:
            if bracket in brackets.keys():
                seq.push(bracket)
            elif not seq.is_empty() and bracket == brackets[seq.peek()]:
                seq.pop()
            else:
                seq.push(bracket)
                break
        if seq.is_empty():
            print(parenthesis)
    else:
        gen_parenthesis(n - 1, parenthesis + '(')
        gen_parenthesis(n - 1, parenthesis + ')')


if __name__ == '__main__':
    gen_parenthesis(2 * 2)
