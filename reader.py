import requests, re, sys, os, argparse, img2pdf
import urllib.request
# from fpdf import FPDF
from bs4 import BeautifulSoup

# usage
parser = argparse.ArgumentParser()
parser.add_argument("link", help="link to manga", type=str)
parser.add_argument("title", help="title to save as", type=str)
args = parser.parse_args()


# various setup
link = sys.argv[1]
manga = sys.argv[2]
mDir = manga + "_chapter" + str(1)
os.mkdir(mDir + "_imgs")
imgs = []

response = requests.get(link)
soup = BeautifulSoup(response.text, 'html.parser')

# grab all pages from parsed html
img_tags = soup.find_all('img')
pages = [img['src'] for img in img_tags]

# download pages if they match the correct format
i = 1
for page in pages:
    checkPage = re.match(r".*[0-9][0-9][0-9].jpg", page)
    if checkPage:
        fn = mDir + "_imgs/pg" + str(i) + ".jpg"
        image = urllib.request.urlretrieve(page, fn)
        imgs.append(fn)
        i = i+1

# convert folder to pdf format
with open("name.pdf","wb") as f:
    f.write(img2pdf.convert(imgs))


        

