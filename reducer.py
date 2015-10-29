import sys  gradesTotal = 0  oldKey = None  
noOfGrades=0  
 
for line in sys.stdin:  
    data_mapped = line.strip().split("\t")      if len(data_mapped) != 2:  
        # Something has gone wrong. Skip this line.  
        continue  
 
    thisKey, thisGrade = data_mapped  
 
    if oldKey and oldKey != thisKey:  
        print oldKey, "\t", gradesTotal/noOfGrades          oldKey = thisKey;          gradesTotal = 0          noOfGrades = 0  
 
    oldKey = thisKey  
    gradesTotal += float(thisGrade)      noOfGrades = noOfGrades + 1  if oldKey != None:  
    print oldKey, "\t", gradesTotal/noOfGrades  
