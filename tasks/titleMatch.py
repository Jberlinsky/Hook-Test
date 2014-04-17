from __main__ import funcs, attrNames
from bs4 import BeautifulSoup
import random
import re

titleMatchNum = 100

alphabs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','.','.','.','.']

patterns = []

for i in range(0, titleMatchNum):
	pattern = ''
	for i in range(0, 9):
		alphab = random.choice(alphabs)
		pattern = pattern + alphab
		if random.randint(0,1) == 0:
			break
	patterns.append(pattern)

for i in range(0, titleMatchNum):
	attrNames.append('titleMatch' + patterns[i])

def addTitleMatchAttr(info, fileObject):

	soup = BeautifulSoup(fileObject)
	title = ''
	if soup.title:
		title = soup.title.string

	if title:
		for i in range(0, titleMatchNum):
			m = re.search(patterns[i], title)
			if m:
				info.append(True)
			else:
				info.append(False)
	else:
		for i in range(0, titleMatchNum):
			info.append(False)

	return

funcs.append(addTitleMatchAttr)
