from PIL import Image
import os


def convert_heic_to_jpg(source_folder, target_folder):
    # 确保目标文件夹存在
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 遍历源文件夹中的所有HEIC文件
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.heic'):
            # 构建完整的文件路径
            input_path = os.path.join(source_folder, filename)
            output_path = os.path.join(target_folder, os.path.splitext(filename)[0] + '.jpg')

            # 打开HEIC文件并转换为RGB模式（JPG通常为RGB）
            with Image.open(input_path) as img:
                rgb_img = img.convert('RGB')
                # 保存为JPG格式
                rgb_img.save(output_path, 'JPEG')
                print(f'Converted {filename} to {os.path.basename(output_path)}')


# 设置源文件夹和目标文件夹的路径
source_folder = r'C:\华为云盘\照片\2024 香炉山'
target_folder = r'C:\华为云盘\照片\2024 香炉山'

convert_heic_to_jpg(source_folder, target_folder)
