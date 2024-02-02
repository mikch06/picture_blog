from exif import Image
from pathlib import Path

# Filepath
source = 'pics'
dest = 'web'

# Read pictures from source folder
pics = Path(source).glob('*')

for pic in pics:
    with open(pic, 'rb') as src:
        img = Image(src)
        #print(img.list_all())
        # print (src.name, img)
        print("Picture Name: ", pic)
        print("Picture Date: ", img.get('datetime'))