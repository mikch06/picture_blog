""" import os
import pathlib
import shutil
from pathlib import Path
import markdown
from datetime import datetime """
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS

# Filepath
source = 'pics'
dest = 'web'

pics = Path(source).glob('*')

for pic in pics:

    # open the image
    image = Image.open(pic)

    # extracting the exif metadata
    exifdata = image.getexif()

    # looping through all the tags present in exifdata
    for tagid in exifdata:
        
        # getting the tag name instead of tag id
        tagname = TAGS.get(tagid, tagid)

        # passing the tagid to get its respective value
        value = exifdata.get(tagid)

        # printing the final result
        print(f"{tagname:25}: {value}")




# # Generate timestamp
# now = datetime.now()
# stamp = now.strftime("%Y-%m-%d %H:%M")
