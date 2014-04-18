from bs4 import BeautifulSoup
from __main__ import funcs, attrNames

attrNames.append('hasItalic')

def addItalicAttr(info, fileObject, index):

	soup = BeautifulSoup(fileObject)

	i = 0
	for it in soup.find_all('i'):
		i = i+1

	hasItalic = False
	if i:
		hasItalic = True

	info.append(hasItalic)
	
	return

funcs.append(addItalicAttr)
