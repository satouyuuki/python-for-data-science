ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# TODO
ft_list[1] = "World!"
#ft_tuple[1] = "Japan!"
tmp = list(ft_tuple)
tmp[1] = "Japan!"
ft_tuple = tuple(tmp)


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
