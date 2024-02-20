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

# Write homepage
with open(home, 'w') as site:
    site.write("<div id=\"stamp\">Last generated: {}</div><br>".format(timestamp))

foo = []
minilist =  []
master_list = []

for pic in pics:
    with open(pic, 'rb') as src:
        img = Image(src)


        # Reformat exif timestamp
        dateFormat = "%d.%m.%Y"
        strImageDate = img.get('datetime')
        imageDate = datetime.strptime(strImageDate,"%Y:%m:%d %H:%M:%S")
        imageDate = datetime.strftime(imageDate, dateFormat)

        foo.append(imageDate)
        foo.sort(reverse=True)

        minilist.append(imageDate)
        minilist.append(pic)
        # print("minilist: ", minilist)


master_list.append(minilist)
master_list.sort(reverse=True)
print("masterlist: ", master_list)

for entry in foo:
    print(entry)

