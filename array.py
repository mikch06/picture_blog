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


# Read pictures from source folder
pics = Path(source).glob('*')

date_list = []
image_array = {}

for pic in pics:
    with open(pic, 'rb') as src:
        img = Image(src)
        # print("Picture handle:")
        # print("Picture Path: ", pic)
        # print("Picture Date: ", img.get('datetime'))

        pic_list = img.get('datetime')
        pic_list = datetime.strptime(pic_list,"%Y:%m:%d %H:%M:%S")


        image_array[pic_list] = pic

        sortierte_daten = sorted(image_array.items())

        sortiertes_dict = {}


          

        for datum, pic in sortierte_daten:
            datum = datum.strftime("%d.%m.%Y")
            sortiertes_dict[datum] = pic


print("OUT Sortiertes dict: ", sortiertes_dict)

for datum, pic in sortierte_daten:
        datum = datum.strftime("%d.%m.%Y")
        print(datum, pic)
