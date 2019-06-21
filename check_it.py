# It seems as if Code Climate counts SLOC. For this file it reports 8 lines of
# code.
#
# This code violates the first maintainability check `argument-count`


def print_it(a, b, c, d, e, f, g):
    # Code Climate supports Python 2 only atm.
    print(a, b, c, d, e, f, g)


def main():
    msg = "Hej Code Climate, please check this code."
    a, b, c, d, e, f, g = msg.split()
    print_it(a, b, c, d, e, f, g)


if __name__ == '__main__':
    main()
