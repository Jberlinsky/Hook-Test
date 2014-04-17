from __main__ import funcs, attrNames
import random

attrNames.append('noisy50%')
attrNames.append('noisy55%')
attrNames.append('noisy60%')
attrNames.append('noisy65%')
attrNames.append('noisy70%')
attrNames.append('noisy75%')
attrNames.append('noisy80%')
attrNames.append('noisy85%')
attrNames.append('noisy90%')
attrNames.append('noisy95%')
attrNames.append('important')

def addNoisyAndImportanceAttr(info, index):

	important = False
	if index < 153:
		important = True

	noisy50 = important
	if random.randint(0,10) > 5:
		noisy50 = not important
	info.append(noisy50)

	noisy55 = important
	if random.randint(0,20) > 11:
		noisy55 = not important
	info.append(noisy55)

	noisy60 = important
	if random.randint(0,10) > 6:
		noisy60 = not important
	info.append(noisy60)

	noisy65 = important
	if random.randint(0,20) > 13:
		noisy65 = not important
	info.append(noisy65)

	noisy70 = important
	if random.randint(0,10) > 7:
		noisy70 = not important
	info.append(noisy70)

	noisy75 = important
	if random.randint(0,20) > 15:
		noisy75 = not important
	info.append(noisy75)

	noisy80 = important
	if random.randint(0,10) > 8:
		noisy80 = not important
	info.append(noisy80)

	noisy85 = important
	if random.randint(0,20) > 17:
		noisy85 = not important
	info.append(noisy85)

	noisy90 = important
	if random.randint(0,10) > 9:
		noisy90 = not important
	info.append(noisy90)

	noisy95 = important
	if random.randint(0,20) > 19:
		noisy95 = not important
	info.append(noisy95)

	info.append(important)

	return

funcs.append(addNoisyAndImportanceAttr)
