

def print_it(a, b, c, d, e, f, g):
    # Code Climate supports Python 2 only atm.
    print(a, b, c, d, e, f, g)


def main():
    msg = "Hej Code Climate, please check this code."
    a, b, c, d, e, f, g = msg.split()
    print(a, b, c, d, e, f, g)


if __name__ == '__main__':
    main()
