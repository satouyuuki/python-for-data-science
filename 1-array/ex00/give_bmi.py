# import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    res = list()
    res.append(weight[0] / height[0] ** 2)
    res.append(weight[1] / height[1] ** 2)
    return res


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    res = list()
    res.append(bmi[0] > limit)
    res.append(bmi[1] > limit)
    return res
