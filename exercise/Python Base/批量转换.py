import os


# 转换视频格式的函数
def convert_video(input_path, output_path):
    os.system(f'ffmpeg -i "{input_path}" -c:v libx264 -crf 20 "{output_path}"')


# 指定视频文件所在目录
videos_directory = r'C:\Users\王志强\Videos\videos'
# 指定输出目录
output_directory = r'C:\Users\王志强\Videos\converted_videos'

# 确保输出目录存在
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 遍历视频目录
for filename in os.listdir(videos_directory):
    input_path = os.path.join(videos_directory, filename)
    output_path = os.path.join(output_directory, os.path.splitext(filename)[0] + '.mp4')
    convert_video(input_path, output_path)
