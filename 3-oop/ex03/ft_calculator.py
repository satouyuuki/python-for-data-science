class calculator:
    def __init__(self, lst: list[float]):
        self.lst = lst

    def __str__(self) -> str:
        return f"{self.lst}"

    def __add__(self, object) -> None:
        self.lst = list(map(lambda x: x + object, self.lst))
        print(self.lst)

    def __mul__(self, object) -> None:
        self.lst = list(map(lambda x: x * object, self.lst))
        print(self.lst)

    def __sub__(self, object) -> None:
        self.lst = list(map(lambda x: x - object, self.lst))
        print(self.lst)

    def __truediv__(self, object) -> None:
        try:
            self.lst = list(map(lambda x: x / object, self.lst))
            print(self.lst)
        except ZeroDivisionError:
            print("Error: Attempted to divide by zero.")
