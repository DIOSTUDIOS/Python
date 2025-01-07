from PIL import Image


def vintage_filter(image):
    # 创建一个新的空图片，用于存放处理后的结果
    new_image = Image.new("RGB", image.size)

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            # 调整RGB值，模拟复古效果
            new_r = int(0.393 * r + 0.769 * g + 0.189 * b)
            new_g = int(0.349 * r + 0.686 * g + 0.168 * b)
            new_b = int(0.272 * r + 0.534 * g + 0.131 * b)
            # 限制RGB值在0-255之间
            new_r = min(max(new_r, 0), 255)
            new_g = min(max(new_g, 0), 255)
            new_b = min(max(new_b, 0), 255)
            new_image.putpixel((x, y), (new_r, new_g, new_b))

    return new_image


# 打开图片
image = Image.open("IMG_0013.JPG")
vintage_image = vintage_filter(image)
vintage_image.show()
