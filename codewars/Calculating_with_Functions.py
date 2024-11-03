# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
def zero(f=None): return 0 if f is None else int(f(0))
def one(f=None): return 1 if f is None else int(f(1))
def two(f=None): return 2 if f is None else int(f(2))
def three(f=None): return 3 if f is None else int(f(3))
def four(f=None): return 4 if f is None else int(f(4))
def five(f=None): return 5 if f is None else int(f(5))
def six(f=None): return 6 if f is None else int(f(6))
def seven(f=None): return 7 if f is None else int(f(7))
def eight(f=None): return 8 if f is None else int(f(8))
def nine(f=None): return 9 if f is None else int(f(9))


def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x / y
