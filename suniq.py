#Program to show you only unique lines between two files regardless of position in files.
#Written by Brayden Storms 3-19-2025
#Suniq V0.1

import sys

file1Lines = []
with open(sys.argv[1]) as tmp_file:
    for line in tmp_file:
        file1Lines.append(line.strip().upper())

file2Lines = []
with open(sys.argv[2]) as tmp_file:
    for line in tmp_file:
        file2Lines.append(line.strip().upper())

#Compare lines in file1
uniqLines1 = []
for line in file2Lines:
    if line not in file1Lines:
        print("File 2 uniq line %s",line)
        uniqLines1.append(line)

#Compare lines in file2
uniqLines2 = []
for line in file1Lines:
    if line not in file2Lines:
        print("File 1 uniq line %s",line)
        uniqLines2.append(line)

uniqLinesMaster = []
#Now combine both arrays only if a unique values
for line in uniqLines1:
    if line not in uniqLinesMaster:
        uniqLinesMaster.append(line)
        
for line in uniqLines2:
    if line not in uniqLinesMaster:
        uniqLinesMaster.append(line)      

for line in uniqLinesMaster:
    print(line)