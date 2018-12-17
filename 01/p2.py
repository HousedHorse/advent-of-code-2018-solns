#!/usr/bin/python
# https://adventofcode.com/2018/day/1

infile = open("input","r")

from collections import defaultdict

# read file into a list of lines
inlist = []
while True:
    # read line and strip newline characters
    instr = infile.readline().rstrip("\r\n")

    if instr == '': # eof
        break

    inlist.append(instr)

infile.close()

# calculate frequencies and keep track of how many times we've seen them
freqs = defaultdict(int)
freq = 0
done = False
while True:
    for i in inlist:
        freq += int(i)
        freqs[freq] += 1
        if freqs[freq] == 2:
            done = True
            break
    if done: break


# write solution
ofile= open("output2","w")
ofile.write(str(freq))
ofile.close()
