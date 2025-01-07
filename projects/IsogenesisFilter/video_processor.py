import os
import hashlib


def get_video_hash(video_path):
    # 打开视频文件
    with open(video_path, 'rb') as f:
        # 读取视频文件的前10MB作为哈希计算的依据
        data = f.read(10 * 1024 * 1024)
    # 计算MD5散列值
    md5 = hashlib.md5(data)
    # 返回散列值的十六进制字符串
    return md5.hexdigest()


def find_duplicate_videos(directory):
    duplicates = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and file_path.lower().endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv')):
            video_hash_value = get_video_hash(file_path)
            if video_hash_value in duplicates:
                duplicates[video_hash_value].append(file_path)
            else:
                duplicates[video_hash_value] = [file_path]
    return {k: v for k, v in duplicates.items() if len(v) > 1}


# 使用示例
if __name__ == '__main__':
    directory = r'C:\华为云盘\视频'
    duplicates = find_duplicate_videos(directory)
    for hash_value, files in duplicates.items():
        print(f'Duplicate videos with hash {hash_value}:')
        for file in files:
            print(file)
