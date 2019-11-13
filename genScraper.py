import urllib
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os

baseUrl = "http://apod.nasa.gov/apod/archivepix.html"
#currentDirectory = os.getcwd()
#download_directory = os.path.join(currentDirectory,"apod_pics")

img_count = 0
visited = set()
toVisit = set((baseUrl,))#{baseUrl}

##RuntimeError: Set changed size during iteration

while toVisit:
	#add all sublinks toVisit
	url = toVisit.pop()
	print ("VISITING " + url)
	content = urllib.request.urlopen(url).read()
	for link in BeautifulSoup(content,"lxml").findAll("a"):
		sub_link = urljoin(url,link["href"])
		if  sub_link not in visited:
			toVisit.add(sub_link)
			print ("adding toVisit " + sub_link)
		else:
			print ("already visited" + sub_link)
		
	#get images on this page
	for img in BeautifulSoup(content,"lxml").findAll("img"):
		img_url = urljoin(url,img["src"])
		print("Downloading image:",img_url)
		#not actually downloading
	
	visited.add(url)
	#print(visited)
