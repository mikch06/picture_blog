from exif import Image
from pathlib import Path
import time
from datetime import datetime

# Filepath
source = 'pics'
dest = 'web'

# Read pictures from source folder
pics = Path(source).glob('*')

for pic in pics:
    with open(pic, 'rb') as src:
        img = Image(src)
        print("\nHandle new picutre")
        print("Picture Name: ", pic)
        print("Picture Date: ", img.get('datetime'))
        print("----------------------------------")

        # Reformat exif timestamp
        dateFormat = "%Y-%m-%d-%M"
        strImageDate = img.get('datetime')
        imageDate = datetime.strptime(strImageDate,"%Y:%m:%d %H:%M:%S")
        imageDate = datetime.strftime(imageDate, dateFormat)
        print("Picture New Format: ", imageDate)




print("\n\nPicture Blog handle endup.")
