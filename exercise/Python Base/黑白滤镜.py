from PIL import Image


def black_and_white_filter(image):
    # 转换为灰度图像
    gray_image = image.convert("L")

    return gray_image


image = Image.open("IMG_0013.JPG")
bw_image = black_and_white_filter(image)
bw_image.show()
