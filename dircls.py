import sys

#!/usr/bin/env python

inputfile = sys.argv[1]

fh = open(inputfile, "r")

lineList = fh.readlines()

# A "success" is if a line is dir and the next line is a cls

success = 0
attempts = len(lineList)/2
i = 0

for i in range(1,len(lineList)-1):
	if lineList[i].find('dir') != -1 and lineList[i+1].find('cls') != -1:
		#print lineList[i]
		#print lineList[i+1]
		success = success + 1
	i = i + 1

rate = float(success)/float(attempts)
rate = float(rate) * 100

print 'Succeses: ' + str(success)
print 'Attempts: ' + str(attempts)
print 'Success Rate: ' + '%0.0f'%(rate)
