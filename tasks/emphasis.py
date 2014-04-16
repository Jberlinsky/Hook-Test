from bs4 import BeautifulSoup
from __main__ import funcs, attrNames

attrNames.append('hasEmphasis')

def addEmphasisAttr(info, fileObject):

	soup = BeautifulSoup(fileObject)

	i = 0
	for em in soup.find_all('em'):
		i = i+1

	hasEmphasis = False
	if i:
		hasEmphasis = True

	info.append(hasEmphasis)
	return

funcs.append(addEmphasisAttr)