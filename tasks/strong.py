from __main__ import *

import os
from bs4 import BeautifulSoup

index = 0
filename = "index.html"

while os.path.isfile("./data/" + filename):

	f = open("./data/" + filename)
	soup = BeautifulSoup(f)

	i = 0
	for strong in soup.find_all('strong'):
		i = i+1

	hasStrong = False
	if i:
		hasStrong = True

	infoList[index].append(hasStrong)

	f.close()
	index = index + 1
	filename = "index.html." + str(index)

featureNames.append('hasStrong')
