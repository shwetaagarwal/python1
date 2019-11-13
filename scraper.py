#import urllib
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os
import sys
import time
print(sys.version)
base_url = "http://apod.nasa.gov/apod/archivepix.html"
currentDirectory = os.getcwd()
download_directory = os.path.join(currentDirectory,"apod_pics")
content = urllib.request.urlopen(base_url).read()

start = time.time()
img_count = 0
for link in BeautifulSoup(content, "lxml").findAll("a"):
	print("Following link:", link)
	sub_url = urljoin( base_url, link["href"] )
	if img_count > 20:
		break
	content = urllib.request.urlopen(sub_url).read()
	for img in BeautifulSoup(content, "lxml").findAll("img"):
		if img_count > 20:
			break
		img_url = urljoin(sub_url,img["src"])
		print("Downloading image:",img_url)
		img_count += 1
		#img_name = img_url.split("/")[-1] # get the last bit to get image name
		img_pair = os.path.split(img_url)
		img_name = img_pair[1]
		urllib.request.urlretrieve(img_url, os.path.join(download_directory, img_name))
endtime = time.time()
time_taken = endtime - start
print(time_taken)