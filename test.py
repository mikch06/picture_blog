from exif import Image
from pathlib import Path
import os
from datetime import datetime

# Filepath
source = 'images'
dest = '.'
home = 'index.html'

# Generate timestamp
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M")

pic_list = []

# Read pictures from source folder
pics = Path(source).glob('*')

for pic in pics:
    with open(pic, 'rb') as src:
        img = Image(src)
        # print("Picture handle:")
        # print("Picture Path: ", pic)
        # print("Picture Date: ", img.get('datetime'))
        pic_list = img.get('datetime')
        pic_list = datetime.strptime(pic_list,"%Y:%m:%d %H:%M:%S")

        pic_list.sort(key=lambda date: datetime.strptime(date, "%Y:%m:%d %H:%M:%S"))




        print(ntime)
