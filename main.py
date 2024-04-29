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
timestamp = now.strftime("%d.%m.%Y, %H:%M")

# Read pictures from source folder
pics = Path(source).glob('*')

image_dict = {}

for pic in pics:
    with open(pic, 'rb') as src:
        img = Image(src)
        print("-")
        print("Picture Path: ", pic)
        print("Picture Date: ", img.get('datetime'))

        pic_list = img.get('datetime')
        pic_list = datetime.strptime(pic_list,"%Y:%m:%d %H:%M:%S")

        # Add entries to dictionary
        image_dict[pic_list] = pic

        sorted_data = sorted(image_dict.items(), reverse=True)

# HTML Header
header = """
<!DOCTYPE html>
<html>
<head>
    <title>🍷 WineBlog 🍷</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
<style>
body, html  {
background-color: #ddd;
margin: 10px;
}

h1  {
font-size: 26px;
}

a   {
text-decoration: none;
}
#stamp  {
font-size: 10px;
}

.responsive {
  width: 100%;
  max-width: 500px;
  height: auto;
}

.card-body  {
    background-color: black;
    color: white;
    width: 50%;
}
</style>
</head>
<body class="p-3 m-0 border-0 bd-example m-0 border-0 bd-example-row">
"""

# Homepage Top
homepage = """
<h1>🍷 WineBlog 🍷</h1>
"""

collapse = """
  <button class="btn btn-secondary btn-sm" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
    Info
  </button>
  <br><br>
<div class="collapse" id="collapseExample">
  <div class="card card-body">
    This page is not just to show up wines - but rather to improve python programming skills with a page generator and image handler.
  </div>
</div>
"""

# Write homepage
with open(home, 'w') as site:
    site.write(header)
    site.write(homepage)
    site.write("<div id=\"stamp\">Last generated: {}</div><br>".format(timestamp))
    site.write("Click for bigger images!<br><br>")
    site.write(collapse)
    site.write("<div class=\"row g-0 text-center\">")

# Write article (wine) elements
with open(home, 'a') as site:

    for datum, pic in sorted_data:
            datum = datum.strftime("%d.%m.%Y")
            site.write("<div class=\"col-sm-6 col-md-4\"><h3>{0}</h3><a href=\"{1}\" target=\"_blank\"><img src=\"{1}\" class=\"responsive\"></a><br><br></div>".format(datum, pic))

# Footer
footer = """
</div>\n<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>\n</body>\n</html>
"""


# Write Footer
with open(home, 'a') as site:
    site.write(footer)
