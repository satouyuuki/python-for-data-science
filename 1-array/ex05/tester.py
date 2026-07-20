from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import numpy as np


def brightness(image: np.ndarray, factor: float):
    data = np.asarray(image)
    if factor < 0:
        raise NameError('only positive values for factor')
    i = data.copy()
    print(f"before: {i}")
    i = i * factor
    print(f"after: {i}")
    print(f"i > 1: {i > 1}")
    print(f"i[i > 1]: {i[i > 1]}")
    i[i > 1] = 1
    return i


def test(array: np.ndarray) -> np.ndarray:
    # 左右反転
    # return array[:, ::-1, :]
    # 上下反転
    return array[::-1, :, :]


array = ft_load("landscape.jpg")
# convert_matplot(test(array))
# convert_matplot(brightness(array, 1.5))
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)

print(ft_invert.__doc__)
