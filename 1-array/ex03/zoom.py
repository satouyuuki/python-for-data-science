from matplotlib import image, pyplot
# from PIL import Image
import numpy as np


def rgb2gray(rgb):
    # return np.dot(rgb[..., :3], [0.299, 0.587, 0.144])
    weights = np.array([0.299, 0.587, 0.114])
    return np.dot(rgb, weights)[..., np.newaxis].astype(np.uint8)


def print_info(img):
    data = np.asarray(img)
    print(f"The shape of image is: {data.shape}")
    print(f"{data}")


def convert_matplot(img):
    print_info(img)
    pyplot.imshow(img)
    pyplot.show()


def convert_rg_matplot(img):
    print_info(img)
    pyplot.imshow(img, cmap=pyplot.get_cmap('gray'))
    pyplot.show()


img_rgb = image.imread('animal.jpeg')
convert_matplot(img_rgb)
convert_rg_matplot(rgb2gray(img_rgb))

# img = Image.open('animal.jpeg').convert('L')
# img.show()
# im = np.array(img)
# print(type(im))
# print(im)
# gr_im= Image.fromarray(im).save('gr_kolala.png')
