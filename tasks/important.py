from __main__ import *

import os

index = 0
filename = "index.html"

while os.path.isfile("./data/" + filename):

	important = False
	if index < 146:
		important = True

	infoList[index].append(important)

	index = index + 1
	filename = "index.html." + str(index)

featureNames.append('important')
