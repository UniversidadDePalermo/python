from os import walk

PATH = "./contents"

def scan(dir, index = {}):
  """
  Builds a directory map with the directory in the provided path
  """
  for (dirpath, dirnames, filenames) in walk(dir):
    if len(dirnames) > 0:
      for dirname in dirnames:
        scan(dir + '/' + dirname, index)

    if len(filenames) > 0:
      index[dirpath] = filenames

  return index
