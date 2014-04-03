from __main__ import *

import os
from bs4 import BeautifulSoup

index = 0
filename = "index.html"

while os.path.isfile("./data/" + filename):

	f = open("./data/" + filename)
	soup = BeautifulSoup(f)

	i = 0
	for link in soup.find_all('a'):
		i = i+1

	link = False
	link10 = False
	link100 = False
	link1000 = False
	if i > 0:
		link = True
	if i > 10:
		link10 = True	
	if i > 100:
		link100 = True
	if i > 1000:
		link1000 = True

	infoList[index].append(link)
	infoList[index].append(link10)
	infoList[index].append(link100)
	infoList[index].append(link1000)

	f.close()
	index = index + 1
	filename = "index.html." + str(index)

featureNames.append('hasLinks')
featureNames.append('moreThan10Links')
featureNames.append('moreThan100Links')
featureNames.append('moreThan1000Links')
