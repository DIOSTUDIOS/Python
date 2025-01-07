import os, shutil
import hashlib

from recorder import logRecorder
from PIL import Image


def get_images(baseDirectory):
    images = []

    for root, directories, images in os.walk(baseDirectory):
        for image in images:
            try:
                Image.open(os.path.join(root, image))
                images.append(os.path.join(root, image))
            except Exception as e:
                logRecorder.error(f'图片 {os.path.join(root, image)} 无法打开，错误信息: {e}！已移动至目录 UnnormalImages！')
                # send2trash(os.path.join(root, file))
                if os.path.exists(f'./UnnormalImages/{image}'):
                    os.rename(image, f'{os.path.join(root, image)}')
                    shutil.move(os.path.join(root, image), './UnnormalImages')
                shutil.move(os.path.join(root, image), './UnnormalImages')

    return sorted(images)


def get_image_hash(image):
    picture = Image.open(image).convert('L').resize((16, 16))
    pictureBytes = picture.tobytes()
    pictureMD5 = hashlib.md5(pictureBytes).hexdigest()

    return pictureMD5


def get_duplicate_images(baseDirectory):
    duplicateImages = {}

    images = get_images(baseDirectory)

    for image in images:
        if os.path.isfile(image) and image.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            imageHashValue = get_image_hash(image)
            logRecorder.info(f'图像 {image} 的哈希值为 {imageHashValue}！')

            if imageHashValue in duplicateImages:
                duplicateImages[imageHashValue].append(image)
            else:
                duplicateImages[imageHashValue] = [image]

    return {imageHashValue: images for imageHashValue, images in duplicateImages.items() if len(images) > 1}


if __name__ == '__main__':
    filePath = os.path.dirname(os.path.abspath('./BeTreatedImages/IMG_0002.jpg'))
    print(filePath)
    print(type(filePath))

    if not os.path.exists(filePath):
        print(f'./UnnormalImages/{filePath}')
        # os.mkdir(f'./UnnormalImages/{filePath}')
    pass
