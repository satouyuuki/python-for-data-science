from PIL import Image
from numpy import asarray


def ft_load(path: str) -> list:
    try:
        assert path is not None and isinstance(path, str), (
                "the path are not str")
        image = Image.open(path)
        # print(type(image.format))
        data = asarray(image)
        print(f"The shape of image is: {data.shape}")
        return data
    # FileNotFoundError, PIL.UnidentifiedImageError
    except (OSError, AssertionError) as e:
        print(f"{type(e).__name__}: {e}")
        return
