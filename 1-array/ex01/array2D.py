import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert family is not None and isinstance(family, list), (
                "the family are not list")
        assert isinstance(start, int) or isinstance(end, int), (
                "the start or end are not int")
        prev_len = 0
        for x in family:
            if prev_len == 0:
                prev_len = len(x)
            assert prev_len == len(x), "the arguments are not same size"
        shape = np.array(family)
        print(f"My shape is : {shape.shape}")
        new_family = family[start:end]
        new_shape = np.array(new_family)
        print(f"My new shape is : {new_shape.shape}")
        return new_family
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        return []
