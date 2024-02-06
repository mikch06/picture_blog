from exif import Image
from pathlib import Path
import os
from datetime import datetime

# Filepath
source = 'web/images'
dest = 'web'
home = os.path.join(dest, 'index.html')

# Generate timestamp
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M")

# HTML Header
header = """
<!DOCTYPE html>
<html>
<head>
    <title>ICT Wiki</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
<style>
body, html  {
background-color: #eee;
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
<h1>Weeeeeeein</h1>

"""

# Read pictures from source folder
pics = Path(source).glob('*')

with open(home, 'w') as site:
    site.write(header)
    site.write(homepage)


for pic in pics:
    with open(pic, 'rb') as src:
        img = Image(src)
        print("----------------------------------")
        print("Handle new picutre")
        print("Picture Name: ", pic)
        print("Picture Date: ", img.get('datetime'))

        # Reformat exif timestamp
        dateFormat = "%d.%m.%Y"
        strImageDate = img.get('datetime')
        imageDate = datetime.strptime(strImageDate,"%Y:%m:%d %H:%M:%S")
        imageDate = datetime.strftime(imageDate, dateFormat)
        print("Picture New Format: ", imageDate)
        print("----------------------------------")

        # Write dynamic content to site
        with open(home, 'a') as site:
            site.write(imageDate + '<br>')
            #site.write("<a href=\"{0}\">{0}</a><br>".format(pic))

print("\n\nPicture Blog handle endup.")




footer = "\n<body>\n</html>"


# Loop articles for page index
# with open(home, 'w') as f:
#     f.write(header)
#     f.write(homepage)
#     for pic in pics:
#         newpage = os.path.splitext(page)[0]
#         newpage = newpage.replace("-", " ")
#         print("title:", newpage)
#         f.write("<a href=\"{0}\">{1}</a><br>".format(page, newpage))
#     f.write("<br><br><div id=\"stamp\">Last generated: {}</div>".format(timestamp))
#     f.write(footer)

# print("Fileconverter has finished")