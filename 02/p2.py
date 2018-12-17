#! /usr/bin/python
# https://adventofcode.com/2018/day/2

# find the number of differences between two IDs
def compareTwoIDs(first, second):
    diffcount = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            diffcount +=1
    return diffcount

# return all identical letters in the same positions between two IDs
def findSimilar(first, second):
    similar = ""
    for i in range(len(first)):
        if first[i] == second[i]:
            similar += first[i]
    return similar


# read input
infile = open("input","r")
inlist = []
while True:
    # read line and strip newline characters
    instr = infile.readline().rstrip("\r\n")

    if instr == '': # eof
        break

    inlist.append(instr)
infile.close()

soln = ""
done = False
for i in range(len(inlist)):
    if done: break
    for j in range(i+1,len(inlist)):
        # find diff number
        diff = compareTwoIDs(inlist[i],inlist[j])
        if diff == 1:
            # if we found two strings witha  diff of 1...
            # the solution is what they have in common
            soln = findSimilar(inlist[i],inlist[j])
            done = True
            break


# write solution
ofile= open("output2","w")
ofile.write(soln)
ofile.close()
