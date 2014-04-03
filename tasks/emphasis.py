from __main__ import *

import os
from bs4 import BeautifulSoup

index = 0
filename = "index.html"

while os.path.isfile("./data/" + filename):

	f = open("./data/" + filename)
	soup = BeautifulSoup(f)

	i = 0
	for em in soup.find_all('em'):
		i = i+1

	hasEmphasis = False
	if i:
		hasEmphasis = True

	infoList[index].append(hasEmphasis)

	f.close()
	index = index + 1
	filename = "index.html." + str(index)

featureNames.append('hasEmphasis')
