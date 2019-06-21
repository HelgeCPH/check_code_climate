# It seems as if Code Climate counts SLOC. For this file it reports 8 lines of
# code.
#
# This code violates the seventh maintainability check `nested-control-flow`
from random import randint


def do_it(value):
    result = 0
    if 0 <= value < 10:
        a = value + randint(1, 10)
        result = a
    elif 11 <= value < 20:
        b = value + randint(10, 20)
        result = b
    elif 21 <= value < 30:
        c = value + randint(20, 30)
        result = c
    elif 31 <= value < 40:
        d = value + randint(30, 40)
        result = d
    return result


def main():
    print(do_it(21))


if __name__ == '__main__':
    main()
