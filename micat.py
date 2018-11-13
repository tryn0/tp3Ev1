import sys

fh = open(sys.argv[1],"r")
line = fh.readline()
while line:
  print(line,end="")
  line = fh.readline()
fh.close()

