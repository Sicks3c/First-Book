from sys import argv
script, filename = argv
infile = open(filename, 'r')
lines = 0
characters = 0
for line in infile:
    wordslist = line.split()
    lines = lines + 1
    characters = characters + len(line)
print"the lines", lines
print"the characters", characters
