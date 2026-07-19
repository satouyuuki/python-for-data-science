import numpy as np


def _give_bmi(height, weight):
    return weight / height ** 2


def _apply_limit(bmi: int | float, limit: int) -> bool:
    return bmi > limit


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    res = np.frompyfunc(_give_bmi, 2, 1)(height, weight)
    return list(res)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    repeat_limit = [limit] * len(bmi)
    res = np.frompyfunc(_apply_limit, 2, 1)(bmi, repeat_limit)
    return list(res)
