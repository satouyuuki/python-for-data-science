import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    shape = np.array(family)
    new_family = family[start:end]
    new_shape = np.array(new_family)
    print(f"My shape is : {shape.shape}")
    print(f"My new shape is : {new_shape.shape}")
    return new_family
