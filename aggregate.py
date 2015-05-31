import sys
import os

def Aggregate(dir):
   print "Aggregating: %s" % (dir)
   
   tag_records = {}
   
   # Enumerate files in dir
   files = os.listdir(dir)
  
   # Process each file
   for f in files:
      for line in open(dir+'\\'+f):
	     line.rstrip()
	     key, val = line.split("\t")
	     if key in tag_records:
	        tag_records[key] += int(val)
	     else:
	        tag_records[key] = int(val)
	
   # Construct output file name
   out_file_name = 'aggregate-' + dir
   out_file = open(out_file_name, 'wt')
   
   # Sort and write output file
   for k in sorted(tag_records):
      out_file.write(k + '\t' + str(tag_records[k]) + '\n')
   out_file.close()
   

if len(sys.argv) < 2:
   print "Please specify directory."
else:
   Aggregate(sys.argv[1])

