from __main__ import funcs, attrNames
import random
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/../data/')
from getRawData import importantFileNum

for i in range(50, 100):
	attrNames.append('noisy' + str(i))

attrNames.append('important')

def addNoisyAndImportanceAttr(info, fileObj, index):

	important = False
	if index < importantFileNum:
		important = True

	for i in range(50, 100):
		if random.randint(1, 100) < i:
			info.append(important)
		else:
			info.append(not important)

	info.append(important)

	return

funcs.append(addNoisyAndImportanceAttr)
