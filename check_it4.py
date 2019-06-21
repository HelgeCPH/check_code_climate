# It seems as if Code Climate counts SLOC. For this file it reports 8 lines of
# code.
#
# This code violates the fourth maintainability check `method-complexity`


def do_it(value):
    val2 = not(not(value))
    val3 = value and val2
    val4 = val2 and val3
    val5 = val3 and val4
    val6 = val4 and val5
    if value:
        if val2:
            if val3:
                if val4:
                    if val5:
                        if val6:
                            print(value)


def main():
    do_it(True)


if __name__ == '__main__':
    main()
