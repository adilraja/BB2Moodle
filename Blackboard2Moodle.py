""" This files takes in a Blackboard quiz and converts it to a Moodle XML-ready format. After this you can upload the file to http://vletools.com and get a MoodleXML quiz. Eventually you can add it to Moodle question bank.

Input: Provide a BB question bank as a comman line input.

Author: Muhammad Adil
...
"""

import sys
filename = sys.argv[-1]

#if(sys.argc!=1):
# print('Number of arguments should be 1 and it should be a file name')
f = open(filename, 'r')
f2 = open('Moodle-'+filename, 'w')
f2.write('multichoice\n')
for line in f.readlines():
	tokens=line.split('\t')
	i=0;
	j=0
	for token in tokens[1:8]:	
		#print(len(tokens[1:7]))
		if(i==0):
			f2.write(token+'\n')
		if(i>=1 and i<=8 and i!=2):
			f2.write(chr((j-1) + ord('A'))+') '+token+'\n')
		if(i==2):
			j-=1
		i+=1
		j+=1
	f2.write('Answer: A\n\n')

f2.close()
f.close()
