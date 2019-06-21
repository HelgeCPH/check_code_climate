# It seems as if Code Climate counts SLOC. For this file it reports 8 lines of
# code.
#
# This code violates the first maintainability check `argument-count`
import check_it4


def do_it0():
    print('Hej')


def do_it1():
    print('Hej')


def do_it2():
    print('Hej')


def do_it3():
    print('Hej')


def do_it4():
    print('Hej')


def do_it5():
    print('Hej')


def do_it6():
    print('Hej')


def do_it7():
    print('Hej')


def do_it8():
    print('Hej')


def do_it9():
    print('Hej')


def do_it10():
    print('Hej')


def do_it11():
    print('Hej')


def do_it12():
    print('Hej')


def do_it13():
    print('Hej')


def do_it14():
    print('Hej')


def do_it15():
    print('Hej')


def do_it16():
    print('Hej')


def do_it17():
    print('Hej')


def do_it18():
    print('Hej')


def do_it19():
    print('Hej')


def do_it20():
    print('Hej')


def main():
    for name, func in check_it4.__dict__.items():
        if name.startswith('do_it'):
            print(f'Calling {name}', end=": ")
            func()


if __name__ == '__main__':
    main()
