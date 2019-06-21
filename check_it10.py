# It seems as if Code Climate counts SLOC. For this file it reports 8 lines of
# code.
#
# This code violates the tenth maintainability check `identical-code`
from random import randint


def do_it(value):
    result = 0
    if 0 <= value < 10:
        a = value + randint(1, 10)
        result = a
    elif 11 <= value < 20:
        a = value + randint(1, 10)
        result = a
    elif 21 <= value < 30:
        a = value + randint(1, 10)
        result = a
    elif 31 <= value < 40:
        a = value + randint(1, 10)
        result = a
    return result


def main():
    print(do_it(21))


if __name__ == '__main__':
    main()
