import urllib2
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/customsearch-cmd-line/')
from getUrls import getUrlList

result = getUrlList()
urls = result[0]
importantFileNum = result[1]

index = 0
for url in urls:
	try:
		remotefile = urllib2.urlopen(url, timeout = 3)
		localFile = open(os.path.dirname(__file__) + '/' + str(index) + '.html', 'w')
		localFile.write(remotefile.read())
		localFile.close()
		print 'successfully download raw datum:' + url
		index = index + 1
	except:
		if index < importantFileNum:
			importantFileNum = importantFileNum - 1
		continue
