from bs4 import BeautifulSoup
from __main__ import funcs, attrNames

attrNames.append('hasStrong')

def addStrongAttr(info, fileObject):

	soup = BeautifulSoup(fileObject)

	i = 0
	for strong in soup.find_all('strong'):
		i = i+1

	hasStrong = False
	if i:
		hasStrong = True

	info.append(hasStrong)

	return

funcs.append(addStrongAttr)