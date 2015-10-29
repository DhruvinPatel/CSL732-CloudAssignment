import sys
 for line in sys.stdin:  
 data = line.strip().split("\t")
      if len(data) == 3:  
        rollno,coursecode,grade = data  
        print "{0}\t{1}".format(coursecode, grade)  