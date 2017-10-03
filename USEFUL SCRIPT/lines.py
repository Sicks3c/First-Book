import time
from sys import argv
script, filename = argv
infile = open(filename, 'r')
lines = 0
characters = 0
for line in infile:
    wordslist = line.split()
    lines = lines + 1
    characters = characters + len(line)
print"counting lines and characters please wait"
time.sleep(3)
print"the lines", lines
print"the characters", characters
