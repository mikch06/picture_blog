import os
import pathlib
import shutil
from pathlib import Path
import markdown
from datetime import datetime

# Filepath
source = 'pages'
dest = 'web'

# Generate timestamp
now = datetime.now()
stamp = now.strftime("%Y-%m-%d %H:%M")

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
back = "<a href=\"index.html\">Back</a>"

footer = "\n<body>\n</html>"

# Web directory remove and creation
if pathlib.Path(dest).exists():
    print("exist")
    shutil.rmtree(dest)
else:
    print("NOT exist")
    os.mkdir(dest)

if not pathlib.Path(dest).exists():
    os.mkdir(dest)

# Generate html files from markdown files
mdowns = Path(source).glob('*')
for file in mdowns:
    with open(file, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
        print("read", file)

        newfile = os.path.split(file)[1]
        newfile = os.path.splitext(newfile)[0]
        newfile = newfile + ".html"
        newfile = os.path.join(dest, newfile)
        with open(newfile, 'w') as f:
            print("write", newfile)
            f.write(header)
            f.write(back)
            f.write(html)
            f.write(footer)
            f.close()

# Generate File-index / Homepage
print("Generate index.html")
home = os.path.join(dest, "index.html")
path = sorted(os.listdir(dest))

homepage = """
<h1>ICT wiki</h1>
<link href="pagefind/pagefind-ui.css" rel="stylesheet">
<script src="pagefind/pagefind-ui.js"></script>
<div id="search"></div>
<script>
    window.addEventListener('DOMContentLoaded', (event) => {
        new PagefindUI({ element: "#search", showSubResults: true });
    });
</script>
"""

# Loop articles for page index
with open(home, 'w') as f:
    f.write(header)
    f.write(homepage)
    for page in path:
        newpage = os.path.splitext(page)[0]
        newpage = newpage.replace("-", " ")
        print("title:", newpage)
        f.write("<a href=\"{0}\">{1}</a><br>".format(page, newpage))
    f.write("<br><br><div id=\"stamp\">Last generated: {}</div>".format(stamp))
    f.write(footer)

print("Fileconverter has finished")

print("Run search")
os.system("./search/pagefind --site web")