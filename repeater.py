

f = open("input.txt", "r")
g = open("output.txt", "wb")
line = f.readline() # throw away top line
line = f.readline().rstrip()
case = 1
while line:
    n = int(line) # number of strings in each case
    print n
    for i in range (0, n-1):
        line = f.readline().rstrip()
        print line


    print "end of case\n"
    case += 1


f.close
g.close



#g.write ()
