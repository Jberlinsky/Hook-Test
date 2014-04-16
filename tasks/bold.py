from bs4 import BeautifulSoup
from __main__ import funcs, attrNames

attrNames.append('hasBold')

def addBoldAttr(info, fileObject):

	soup = BeautifulSoup(fileObject)

	i = 0
	for bold in soup.find_all('b'):
		i = i+1

	hasBold = False
	if i:
		hasBold = True

	info.append(hasBold)
	
	return

funcs.append(addBoldAttr)
