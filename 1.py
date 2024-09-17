import os
import subprocess

def convert_to_h264(input_folder):
    # 获取文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mov"):
            # 构建输入和临时输出文件路径
            input_file = os.path.join(input_folder, filename)
            temp_output_file = os.path.join(input_folder, f"temp_{filename}")
            
            # 使用 ffmpeg 进行转换
            subprocess.run([
                "ffmpeg", "-i", input_file,
                "-c:v", "libx264", "-c:a", "aac", "-strict", "experimental",
                temp_output_file
            ])
            
            # 替换原文件
            os.replace(temp_output_file, input_file)
            print(f"Converted and replaced {input_file}")

# 指定视频文件夹路径
video_folder = "/Users/czsmacbook/Desktop/html-test/3"
convert_to_h264(video_folder)
