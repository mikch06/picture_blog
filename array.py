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


        date_list.append(pic_list)
        date_list.sort(reverse=True)

        for pic in date_list:
            formatiertes_datum = pic.strftime("%d.%m.%Y")
            print(formatiertes_datum, "|", img)


        print("print array: ", image_array)            

        for miau, wuff in image_array:
            image_array[pic_list] = pic


for foo in date_list:
    formatiertes_datum = foo.strftime("%d.%m.%Y")
    print(formatiertes_datum)


# Datumsliste sortieren
# daten.sort()

# Formatierung und Ausgabe der sortierten Datumsliste
# for datum in daten:
#     formatiertes_datum = datum.strftime("%d.%m.%Y")  # Datum im gewünschten Format formatieren
#     print(formatiertes_datum)


# print("date_list block:")
# for i in date_list:
#     print(i, pic)



        # imageDate = datetime.strptime(strImageDate,"%Y:%m:%d %H:%M:%S")
        # imageDate = datetime.strftime(imageDate, dateFormat)