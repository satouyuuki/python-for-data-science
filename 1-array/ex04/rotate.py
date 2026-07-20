import numpy as np
from load_image import ft_zoom
from matplotlib import pyplot


def print_info(img: np.ndarray):
    data = np.asarray(img)
    print(f"New shape after Transpose: {data.shape}")
    # このgrayの指定は必要
    pyplot.imshow(img, cmap=pyplot.get_cmap('gray'))
    pyplot.show()


def rotate(img: np.ndarray):
    data = np.asarray(img)
    height, weight = data.shape[0], data.shape[1]
    result = np.zeros(shape=(height, weight))
    for i in range(len(img)):
        for j in range(len(img[0])):
            result[j][i] = img[i][j][0]
    return result.astype(np.uint8)


def main():
    img = ft_zoom("animal.jpeg")
    print(img)
    rotate_img = rotate(img)
    print_info(rotate_img)
    print(rotate_img)


if __name__ == "__main__":
    main()
