from matplotlib import image, pyplot
import numpy as np
from load_image import ft_load


def rgb2gray(rgb):
    weights = np.array([0.299, 0.587, 0.114])
    return np.dot(rgb, weights)[..., np.newaxis].astype(np.uint8)


def zoom(img):
    img_cropped = img[100:500, 450:850, :]
    return img_cropped


def print_info(img):
    data = np.asarray(img)
    l_elem = len(data.shape) - 1
    rl_data = data.shape[:l_elem]
    print(f"New shape after slicing: {data.shape} or {rl_data}")


def convert_matplot(img):
    print_info(img)
    pyplot.imshow(img)
    pyplot.show()


def convert_rg_matplot(img):
    print_info(img)
    pyplot.imshow(img, cmap=pyplot.get_cmap('gray'))
    pyplot.show()


def ft_zoom(path: str) -> list:
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
        return


def main():
    print(ft_load("animal.jpeg"))
    print(ft_zoom("animal.jpeg"))


if __name__ == "__main__":
    main()
