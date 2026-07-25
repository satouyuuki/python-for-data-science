def mean(tpl) -> float:
    return sum(tpl) / len(tpl)


def median(tpl) -> int:
    lst = list(tpl)
    n = len(lst)
    median_pos = (n + 1) / 2
    lst.sort()
    if median_pos != int(median_pos):
        return (lst[int(median_pos) - 1] + lst[int(median_pos)]) / 2
    else:
        return lst[int(median_pos) - 1]


def quartile(tpl, q: float) -> int:
    lst = list(tpl)
    n = len(lst)
    pos = 1 + (n - 1) * q
    lst.sort()
    left = lst[int(pos) - 1]
    if pos != int(pos):
        diff = lst[int(pos)] - left
        decimal = pos - int(pos)
        return left + (diff * decimal)
    else:
        return left * 1.0


def var(tpl) -> float:
    m = mean(tpl)
    lst = list(tpl)
    total = sum([(lst[i] - m) ** 2 for i in range(len(lst))])
    return total / len(lst)


def std(tpl) -> float:
    variance = var(tpl)
    return variance ** 0.5


def ft_statistics(*args, **kwargs) -> None:
    keywards = dict(
        toto="mean",
        tutu="median",
        tata="quartile",
        hello="std",
        world="var"
    )
    for key, value in kwargs.items():
        if keywards.get(key) == value:
            if (len(args)):
                if value == "mean":
                    print(f"{value} : {mean(args)}")
                elif value == "median":
                    print(f"{value} : {median(args)}")
                elif value == "quartile":
                    qt = [quartile(args, 0.25), quartile(args, 0.75)]
                    print(f"{value} : {qt}")
                elif value == "std":
                    print(f"{value} : {std(args)}")
                elif value == "var":
                    print(f"{value} : {var(args)}")
                else:
                    print(f"{value} : ")
            else:
                print("ERROR")
