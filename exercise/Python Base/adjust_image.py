from PIL import Image, ImageEnhance
from pathlib import Path


def adjust_image(image_path, contrast=1.0, brightness=1.0, saturation=1.0, hue_shift=0.0):
    # 打开图像
    image = Image.open(image_path)

    # 调整对比度
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)
    # 调整亮度
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)

    # 调整饱和度
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(saturation)

    # 调整色调（Pillow不直接支持色调调整，需要使用HSV转换）
    hsv_image = image.convert('HSV')
    h, s, v = hsv_image.split()

    # 调整色调
    h = [(h + hue_shift) % 256 for h in h.getdata()]
    h = Image.frombytes('L', (image.width, image.height), bytes(h))
    hsv_image = Image.merge('HSV', (h, s, v))

    # 转换回RGB
    final_image = hsv_image.convert('RGB')

    return final_image


# 使用示例
image_path = 'IMG_0013.JPG'
adjusted_image = adjust_image(image_path, contrast=1.1, brightness=1.1, saturation=1.8, hue_shift=10)
# adjusted_image.show()
adjusted_image.save(Path(image_path).stem + '_adjusted' + Path(image_path).suffix)
