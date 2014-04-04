import os
import arff
from bs4 import BeautifulSoup
import sys
import runner

index = 0
filename = "index.html"
infoList = []
featureNames = [] # Appended to within included modules

while os.path.isfile(runner.data_file_location() + filename):
    info = []
    infoList.append(info)
    index = index + 1
    filename = "index.html." + str(index)

sys.path.append(os.path.join(os.path.dirname(__file__), 'tasks'))

# Only run the tasks passed on the command line
# HACK HACK HACK

task_list = sys.argv[-1]
if task_list == 'main.py':
    task_list = runner.tasks()
else:
    task_list = str.split(task_list, ',')


print "Running tasks: "
print task_list

for task in task_list:
    __import__(task)

arff.dump(runner.arff_file_location(), infoList, relation="webpage_info", names=featureNames)
