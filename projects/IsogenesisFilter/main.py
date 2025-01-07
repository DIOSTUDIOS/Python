import image_processor
import shutil

from recorder import logRecorder


if __name__ == '__main__':
    duplicateImages = image_processor.get_duplicate_images(r'C:\华为云盘\照片')

    for imageHashValue, images in duplicateImages.items():
        logRecorder.info(f'重复的图像哈希值【{imageHashValue}】')
        if len(images) > 1:
            for i in range(1, len(images)):
                logRecorder.info(f'移动重复的图像 {images[i]} 至目录UnnormalImages！')
                shutil.move(images[i], './UnnormalImages')
