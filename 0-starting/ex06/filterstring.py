import sys
from ft_filter import filter


def toint(s, d):
    try:
        return int(s)
    except ValueError:
        return d


def main(argv):
    argc = len(argv)
    try:
        assert argc == 3, "the arguments are bad"
        s = str(argv[1])
        n = toint(argv[2], 0)
        assert n != 0 or argv[2] == "0", "the arguments are bad"
        words = s.split(" ")
        filtered_words = list(filter(lambda x: len(x) >= n, words))
        print(filtered_words)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main(sys.argv)
