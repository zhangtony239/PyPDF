#将此文件复制到PDF同目录使用！
import os
from tqdm import tqdm

# 获取当前工作目录
path = "." 
files = os.listdir(path)

for file in tqdm(files):
    if file.endswith(".pdf"):
        filename = file.split(".")[0]
        if len(filename.split(' - ')[2:]) == 1:
            new_filename = ''.join(filename.split(' - ')[2:]) + ".pdf"
            os.rename(file, new_filename)