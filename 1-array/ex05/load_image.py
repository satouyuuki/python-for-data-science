from matplotlib import image, pyplot
import numpy as np


def print_info(img: np.ndarray):
    data = np.asarray(img)
    print(f"The shape of image is: {data.shape}")
    print(data)


def convert_matplot(img: np.ndarray):
    print_info(img)
    pyplot.imshow(img)
    pyplot.show()


def ft_load(path: str) -> np.ndarray:
    try:
        assert path is not None and isinstance(path, str), (
                "the path are not str")
        img = image.imread(path)
        convert_matplot(img)
        return img
    except (OSError, AssertionError) as e:
        print(f"{type(e).__name__}: {e}")
        return np.asarray(None)


def main():
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
