import numpy as np


def _give_bmi(height, weight):
    return weight / height ** 2


def _apply_limit(bmi: int | float, limit: int) -> bool:
    return bmi > limit


def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[int | float]:
    try:
        assert height is not None and weight is not None, (
                "the arguments are NoneType")
        assert len(height) == len(weight), "the arguments are not same size"
        for x in height:
            assert isinstance(x, int) or isinstance(x, float), (
                    "the arguments are not int or float")
        for x in weight:
            assert isinstance(x, int) or isinstance(x, float), (
                    "the arguments are not int or float")
        res = np.frompyfunc(_give_bmi, 2, 1)(height, weight)
        return list(res)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        assert bmi is not None and limit is not None, (
                "the arguments are NoneType")
        for x in bmi:
            assert isinstance(x, int) or isinstance(x, float), (
                    "the bmi are not int or float")
        assert isinstance(limit, int), "the limit are not int"
        repeat_limit = [limit] * len(bmi)
        res = np.frompyfunc(_apply_limit, 2, 1)(bmi, repeat_limit)
        return list(res)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
