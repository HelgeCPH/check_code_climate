# It seems as if Code Climate counts SLOC. For this file it reports 8 lines of
# code.
#
# This code violates the first maintainability check `argument-count`
import inspect


class LongClass:
    def do_it0(self):
        print('Hej')

    def do_it1(self):
        print('Hej')

    def do_it2(self):
        print('Hej')

    def do_it3(self):
        print('Hej')

    def do_it4(self):
        print('Hej')

    def do_it5(self):
        print('Hej')

    def do_it6(self):
        print('Hej')

    def do_it7(self):
        print('Hej')

    def do_it8(self):
        print('Hej')

    def do_it9(self):
        print('Hej')

    def do_it10(self):
        print('Hej')

    def do_it11(self):
        print('Hej')

    def do_it12(self):
        print('Hej')

    def do_it13(self):
        print('Hej')

    def do_it14(self):
        print('Hej')

    def do_it15(self):
        print('Hej')

    def do_it16(self):
        print('Hej')

    def do_it17(self):
        print('Hej')

    def do_it18(self):
        print('Hej')

    def do_it19(self):
        print('Hej')

    def do_it20(self):
        print('Hej')


def main():
    c = LongClass()
    for name, func in inspect.getmembers(c, predicate=inspect.ismethod):
        if name.startswith('do_it'):
            print(f'Calling {name}', end=": ")
            func()


if __name__ == '__main__':
    main()
