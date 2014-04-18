from bs4 import BeautifulSoup
from __main__ import funcs, attrNames

attrNames.append('hasPhotos')
attrNames.append('moreThan10Photos')
attrNames.append('moreThan100Photos')

def addPhotoNumAttr(info, fileObject, index):

	soup = BeautifulSoup(fileObject)

	i = 0
	for photo in soup.find_all('img'):
		i = i+1

	photo = False
	photo10 = False
	photo100 = False
	if i > 0:
		photo = True
	if i > 10:
		photo10 = True
	if i > 100:
		photo100 = True

	info.append(photo)
	info.append(photo10)
	info.append(photo100)
	
	return

funcs.append(addPhotoNumAttr)
