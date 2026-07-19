from ft_filter import filter
print(filter.__doc__)
args = [5, 12, 17, 18, 24, 32]


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


# adults = filter(None, args)
# adults = filter(myFunc, args)
# iteratorを作るのがrange
adults = filter(myFunc, range(20))
print(type(adults))
for x in adults:
    # print(type(x))
    print(x)
