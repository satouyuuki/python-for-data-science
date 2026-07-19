def count_in_list(lst: list, target: str) -> int:
    count = 0
    for x in lst:
        if x == target:
            count += 1
    return count


def main():
    print(count_in_list(["toto", "tata", "toto"], "toto"))
    print(count_in_list(["toto", "tata", "toto"], "tutu"))


if __name__ == "__main__":
    main()
