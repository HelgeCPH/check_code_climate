# It seems as if Code Climate counts SLOC. For this file it reports 8 lines of
# code.
#
# This code violates the seventh maintainability check `nested-control-flow`


def do_it(value):
    if value:
        if value:
            if value:
                if value:
                    if value:
                        if value:
                            print(value)


def main():
    do_it(True)


if __name__ == '__main__':
    main()
