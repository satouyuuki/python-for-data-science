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
                print(value)
            else:
                print("ERROR")
