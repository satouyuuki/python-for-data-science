import sys

def print_info(txt):
    upper = 0
    lower = 0
    punct = 0
    space = 0
    digit = 0
    for char in txt:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in "'.,;:?!-\"":
            punct += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            digit += 1
    print(f"The text contains {len(txt)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")

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
