from __main__ import *

import os
from bs4 import BeautifulSoup

index = 0
filename = "index.html"

while os.path.isfile("./data/" + filename):

	f = open("./data/" + filename)
	soup = BeautifulSoup(f)

	i = 0
	for em in soup.find_all('i'):
		i = i+1

	hasItalic = False
	if i:
		hasItalic = True

	infoList[index].append(hasItalic)

	f.close()
	index = index + 1
	filename = "index.html." + str(index)

featureNames.append('hasItalic')
