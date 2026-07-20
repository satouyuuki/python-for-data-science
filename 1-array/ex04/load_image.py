from matplotlib import image, pyplot
import numpy as np


def rgb2gray(rgb: np.ndarray) -> np.ndarray:
    weights = np.array([0.299, 0.587, 0.114])
    return np.dot(rgb, weights)[..., np.newaxis].astype(np.uint8)


def zoom(img: np.ndarray) -> np.ndarray:
    img_cropped = img[100:500, 450:850, :]
    return img_cropped


def print_info(img: np.ndarray):
    data = np.asarray(img)
    l_elem = len(data.shape) - 1
    rl_data = data.shape[:l_elem]
    print(f"The shape of image is: {data.shape} or {rl_data}")


def convert_rg_matplot(img: np.ndarray):
    print_info(img)
    pyplot.imshow(img, cmap=pyplot.get_cmap('gray'))
    pyplot.show()


def ft_zoom(path: str) -> np.ndarray:
    try:
        assert path is not None and isinstance(path, str), (
                "the path are not str")
        img_rgb = image.imread('animal.jpeg')
        img_gray = rgb2gray(img_rgb)
        zoom_img_gray = zoom(img_gray)
        convert_rg_matplot(zoom_img_gray)
        return zoom_img_gray
    except (OSError, AssertionError) as e:
        print(f"{type(e).__name__}: {e}")
        return np.empty(0)


def main():
    print(ft_zoom("animal.jpeg"))


if __name__ == "__main__":
    main()
