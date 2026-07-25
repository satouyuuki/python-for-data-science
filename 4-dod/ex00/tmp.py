# def some_function(*args):
#     # print(f'Arguments passed: {args} as {type(args)}')
#     for a in args:
#         print(a)

# def some_function(**kwargs):
#     # print(f'keywards: {kwargs} as {type(kwargs)}')
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')

def some_function(key, **kwargs):
    print(kwargs.get(key))


# some_function('arg1', 'arg2', 'arg3')
# some_function(key1='arg1', key2='arg2', key3='arg3')
some_function('key3', key1='arg1', key2='arg2', key3='arg3')
