def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwds):
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
            else:
                function()
        return limit_function
    return callLimiter
