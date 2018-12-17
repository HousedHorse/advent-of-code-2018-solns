#!/usr/bin/python
# https://adventofcode.com/2018/day/1

infile = open("input","r")

# read file into a list of lines
inlist = []
while True:
    # read line and strip newline characters
    instr = infile.readline().rstrip("\r\n")

    if instr == '': # eof
        break

    inlist.append(instr)

infile.close()

# calculate frequency
freq = 0
for i in inlist:
    freq += int(i)

# write solution
ofile= open("output1","w")
ofile.write(str(freq))
ofile.close()
