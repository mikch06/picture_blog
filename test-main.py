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

        foo.append(imageDate)
        foo.sort(reverse=True)



        imageDate = datetime.strptime(strImageDate,"%Y:%m:%d %H:%M:%S")
        imageDate = datetime.strftime(imageDate, dateFormat)


# for entry in foo:
#     print(entry)



# Liste aller Bilddateien im Verzeichnis
# image_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Sortieren der Bilder nach Datum
        sorted_pics = sorted(pics, key=lambda x: imageDate)
        for pic in pics:

            print(pic, imageDate)

# Ausgabe der sortierten Bilder
        # for pic in pics:


print("finish")
