from sys import argv
script, filename = argv
data = open(filename)
print len(data.readlines())
