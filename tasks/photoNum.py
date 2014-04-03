from __main__ import *

import os
from bs4 import BeautifulSoup

index = 0
filename = "index.html"

while os.path.isfile("./data/" + filename):

	f = open("./data/" + filename)
	soup = BeautifulSoup(f)

	i = 0
	for photo in soup.find_all('img'):
		i = i+1

	photo = False
	photo10 = False
	photo100 = False
	if i > 0:
		photo = True
	if i > 10:
		photo10 = True
	if i > 100:
		photo100 = True

	infoList[index].append(photo)
	infoList[index].append(photo10)
	infoList[index].append(photo100)

	f.close()
	index = index + 1
	filename = "index.html." + str(index)

featureNames.append('hasPhotos')
featureNames.append('moreThan10Photos')
featureNames.append('moreThan100Photos')
