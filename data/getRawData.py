import os

with open('sample-urls.txt') as urls:
	cmd = 'rm index.html*'
	os.system(cmd)
	for url in urls:
		cmd = 'wget ' + url
		os.system(cmd)