import sys

NESTED_MORSE = { " ": "/ ",
                "A": ".- ",
                "B": "-... ",
                "C": "-.-. ",
                "D": "-.. ",
                "E": ". ",
                "F": "..-. ",
                "G": "--. ",
                "H": ".... ",
                "I": ".. ",
                "J": ".--- ",
                "K": "-.- ",
                "L": ".-.. ",
                "M": "-- ",
                "N": "-. ",
                "O": "--- ",
                "P": ".--. ",
                "Q": "--.- ",
                "R": ".-. ",
                "S": "... ",
                "T": "- ",
                "U": ".-- ",
                "V": "...- ",
                "W": ".-- ",
                "X": "-..- ",
                "Y": "-.-- ",
                "Z": "--.. ",
                "1": ".---- ",
                "2": "..--- ",
                "3": "...-- ",
                "4": "....- ",
                "5": "..... ",
                "6": "-.... ",
                "7": "--... ",
                "8": "---.. ",
                "9": "----. ",
                "0": "----- ",
                }

def main(argv):
    argc = len(argv)
    try:
        assert argc == 2, "the arguments are bad"
        s = argv[1].upper()
        for x in s:
            assert x.isalnum() or x.isspace(), "the arguments are bad"
        res = ""
        for x in s:
            res += NESTED_MORSE[x]
        print(res[:-1])
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")

if __name__ == "__main__":
    main(sys.argv)
