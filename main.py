import sys
import runner
import os
import arff
import json

sys.path.append(os.path.join(os.path.dirname(__file__), 'tasks'))

# Only run the tasks passed on the command line
# HACK HACK HACK

task_list = runner.tasks()

upperbound = 500
infoList = []
funcs = []
attrNames = [] # Appended to within included modules

for task in task_list:
    __import__(task)

if sys.argv[-1] == 'list-attributes':
    print json.dumps(attrNames)
    sys.exit(0)

print "Running tasks: "
print task_list

for i in range (0, upperbound):
    filename = str(i) + ".html"
    if os.path.isfile(runner.data_file_location() + filename):
        info = []
        fileObject = open(runner.data_file_location() + filename)
        for func in funcs:
            func(info, fileObject, i)
        infoList.append(info)

arff.dump(runner.arff_file_location(), infoList, relation="webpage_info", names=attrNames)
