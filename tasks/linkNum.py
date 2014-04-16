from bs4 import BeautifulSoup
from __main__ import funcs, attrNames

attrNames.append('hasLinks')
attrNames.append('moreThan10Links')
attrNames.append('moreThan100Links')
attrNames.append('moreThan1000Links')

def addLinkNumAttr(info, fileObject):

	soup = BeautifulSoup(fileObject)

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

	info.append(link)
	info.append(link10)
	info.append(link100)
	info.append(link1000)
	
	return

funcs.append(addLinkNumAttr)
