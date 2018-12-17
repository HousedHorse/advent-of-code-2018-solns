#! /usr/bin/python
# https://adventofcode.com/2018/day/2

from collections import defaultdict

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

twos   = 0
threes = 0

for ID in inlist:
    isTwos = False
    isThrees = False

    # default dict to store letter frequencies
    freq   = defaultdict(int)
    for c in ID:
        # increment freq of char if it exists
        freq[c] += 1
    for c in freq:
        if freq[c] == 2 and not isTwos:
            twos += 1
            isTwos = True
        if freq[c] == 3 and not isThrees:
            threes += 1
            isThrees = True

checksum = twos * threes

# write solution
ofile= open("output","w")
ofile.write(str(checksum))
ofile.close()
