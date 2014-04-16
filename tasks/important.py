from __main__ import funcs, attrNames

attrNames.append('important')

def addImportanceAttr(info, index):

	important = False
	if index < 153:
		important = True

	info.append(important)

	return

funcs.append(addImportanceAttr)
