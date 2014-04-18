import json

def tasks():
  return ['titleMatch', 'linkNum', 'photoNum', 'strong', 'bold', 'emphasis', 'italic', 'important']
  #return ['linkNum', 'photoNum', 'strong', 'bold', 'emphasis', 'italic']
  #return ['linkNum']

def arff_file_location():
  return './data.arff'

def data_file_location():
  return './data/'

# Bridge for web runner
def dump_tasks():
  print json.dumps(tasks())

if __name__ == '__main__':
  dump_tasks()
