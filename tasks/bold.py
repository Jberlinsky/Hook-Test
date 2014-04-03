from __main__ import *

import os
from bs4 import BeautifulSoup

index = 0
filename = "index.html"

while os.path.isfile("./data/" + filename):

	f = open("./data/" + filename)
	soup = BeautifulSoup(f)

	i = 0
	for bold in soup.find_all('b'):
		i = i+1

	hasBold = False
	if i:
		hasBold = True

	infoList[index].append(hasBold)

	f.close()
	index = index + 1
	filename = "index.html." + str(index)

featureNames.append('hasBold')
