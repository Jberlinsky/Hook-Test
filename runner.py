import json

def tasks():
  return ['linkNum', 'photoNum', 'strong', 'bold', 'emphasis', 'italic', 'important']

def arff_file_location():
  return './data.arff'

def data_file_location():
  return './data/'

# Bridge for web runner
def dump_tasks():
  print json.dumps(tasks())
