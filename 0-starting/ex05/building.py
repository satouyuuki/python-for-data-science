import sys


def count_upper(txt):
    upper = 0
    for char in txt:
        if char.isupper():
            upper += 1
    return upper


def count_lower(txt):
    lower = 0
    for char in txt:
        if char.islower():
            lower += 1
    return lower


def count_space(txt):
    space = 0
    for char in txt:
        if char.isspace():
            space += 1
    return space


def count_digit(txt):
    digit = 0
    for char in txt:
        if char.isdigit():
            digit += 1
    return digit


def count_punct(txt):
    punct = 0
    for char in txt:
        if char in "'.,;:?!-\"":
            punct += 1
    return punct


def print_info(txt):
    print(f"""The text contains {len(txt)} characters:
{count_upper(txt)} upper letters
{count_lower(txt)} lower letters
{count_punct(txt)} punctuation marks
{count_space(txt)} spaces
{count_digit(txt)} digits""")


def main(argv):
    argc = len(argv)
    try:
        assert argc <= 2, "more than one argument are provided"
        if argc == 1:
            txt = input("What is the text to count?\n")
            print_info(txt + "\n")
        elif argc == 2:
            print_info(argv[1])
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main(sys.argv)
