# It seems as if Code Climate counts SLOC. For this file it reports 8 lines of
# code.
#
# This code violates the seventh maintainability check `nested-control-flow`


def do_it(value):
    if 0 < value < 10:
        return 'low'
    elif 11 < value < 20:
        return 'fair'
    elif 21 < value < 30:
        return 'medium'
    elif 31 < value < 40:
        return 'high'
    return 'super_high'


def main():
    print(do_it(42))


if __name__ == '__main__':
    main()
