import sys

def toint(s, d):
    try:
        return int(s)
    except ValueError:
        return d

def main(argv):
    argc = len(argv)
    try:
        assert argc <= 2, "more than one argument are provided"
        if argc == 2:
            arg = argv[1]
            i = toint(arg, 0)
            assert i != 0 or arg == "0", "argument is not an integer"
            if i % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")

if __name__ == "__main__":
    main(sys.argv)
