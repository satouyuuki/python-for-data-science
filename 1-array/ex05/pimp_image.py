import numpy as np
from load_image import convert_matplot


def ft_invert(array: np.ndarray) -> np.ndarray:
    invert_component = array.copy()
    invert_component = 255 - invert_component
    convert_matplot(invert_component)
    return invert_component


def ft_red(array: np.ndarray) -> np.ndarray:
    red_component = array.copy()
    red_component[::, ::, 1:3] = 0
    convert_matplot(red_component)
    return red_component


def ft_green(array: np.ndarray) -> np.ndarray:
    green_component = array.copy()
    green_component[::, ::, ::2] = 0
    convert_matplot(green_component)
    return green_component


def ft_blue(array: np.ndarray) -> np.ndarray:
    blue_component = array.copy()
    blue_component[::, ::, 0:2] = 0
    convert_matplot(blue_component)
    return blue_component


def ft_grey(array: np.ndarray) -> np.ndarray:
    grey_component = array.copy()
    grey_component = grey_component[::, ::, 1]
    convert_matplot(grey_component, True)
    return grey_component
