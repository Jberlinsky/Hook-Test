import os
import arff
from bs4 import BeautifulSoup
import sys
import runner

index = 0
filename = "index.html"
infoList = []
featureNames = []

while os.path.isfile(runner.data_file_location() + filename):
    info = []
    infoList.append(info)
    index = index + 1
    filename = "index.html." + str(index)

sys.path.append(os.path.join(os.path.dirname(__file__), 'tasks'))

for task in runner.tasks():
    __import__(task)

arff.dump(runner.arff_file_location(), infoList, relation="webpage_info", names=featureNames)
