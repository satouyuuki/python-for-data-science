from ft_filter import filter
print(filter.__doc__)
args = [5, 12, 17, 18, 24, 32]

def myFunc(x):
    if x < 18:
        return False
    else:
        return True

#adults = filter(None, args)
adults = filter(myFunc, args)

for x in adults:
    print(x)
