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

# HTML Header
header = """
<!DOCTYPE html>
<html>
<head>
    <title>🍷🍷🍷 WineBlog 🍷🍷🍷</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
<style>
body, html  {
background-color: #ddd;
margin: 10px;
}

pre {
  display: block;
  color: white;
  background-color: black;
  max-width: 800px;
  min-width: 100px;
  padding: 10px;
  border-radius: 5px;
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

#search {
max-width: 50%;
}
</style>
</head>
<body>
"""

homepage = """
<h1>🍷🍷🍷 WineBlog 🍷🍷🍷</h1>
"""

# Read pictures from source folder
pics = Path(source).glob('*')

# Write homepage
with open(home, 'w') as site:
    site.write(header)
    site.write(homepage)
    site.write("<div id=\"stamp\">Last generated: {}</div><br>".format(timestamp))

for pic in pics:
    with open(pic, 'rb') as src:
        img = Image(src)
        print("Picture handle:")
        print("Picture Path: ", pic)
        print("Picture Date: ", img.get('datetime'))

        # Reformat exif timestamp
        dateFormat = "%d.%m.%Y"
        strImageDate = img.get('datetime')

        foo = []

        foo.append(strImageDate)
        foo.sort(reverse=True)
        
        imageDate = datetime.strptime(strImageDate,"%Y:%m:%d %H:%M:%S")
        imageDate = datetime.strftime(imageDate, dateFormat)
        print("Picture New Format: ", imageDate)
        print("----------------------------------")



        # Write dynamic content to site
        with open(home, 'a') as site:
            site.write("<h3>{0}</h3>".format(imageDate))
            site.write("<a href=\"{0}\" target=\"_blank\">📷</a><br>".format(pic))
            site.write("<img src=\"{0}\" width=\"400\"><br>".format(pic))
            site.write("<br><br>")

            #  Link to pic
            # site.write("<a href=\"{0}\">{0}</a><br>".format(pic))

print("\nPicture Blog handle endup.\n")


# Footer
footer = "\n</body>\n</html>"

with open(home, 'a') as site:
    site.write(footer)