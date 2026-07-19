from PIL import Image
from numpy import asarray


def ft_load(path: str) -> list:
    image = Image.open(path)
    data = asarray(image)
    print(f"The shape of image is: {data.shape}")
    return data
