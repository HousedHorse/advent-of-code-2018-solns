#! /usr/bin/python
# https://adventofcode.com/2018/day/3

from collections import defaultdict
import re

class Claim:
    # parse string s into claim
    def __init__(self,s):
        i = 0

        pattern = re.compile(r"#(\d*)\s*@\s*(\d*)\s*,\s*(\d*):\s*(\d*)\s*x\s*(\d*)")
        match = pattern.match(s)

        self.id = int(match.group(1))
        self.x =  int(match.group(2))
        self.y =  int(match.group(3))
        self.w =  int(match.group(4))
        self.h =  int(match.group(5))

        self.overlaps = False

    # for testing
    def __str__(self):
        s = ""
        s += "ID:" + str(self.id) + "\r\n"
        s += "  x:" + str(self.x) + "\r\n"
        s += "  y:" + str(self.y) + "\r\n"
        s += "  w:" + str(self.w) + "\r\n"
        s += "  h:" + str(self.h) + "\r\n"
        return s
    def __repr__(self):
        return "class(" + str(self.id) + ")"

# read file into a list of lines
infile = open("input","r")
inlist = []
while True:
    # read line and strip newline characters
    instr = infile.readline().rstrip("\r\n")

    if instr == '': # eof
        break

    inlist.append(instr)
infile.close()

# parse each line as a claim
claims = []
for ell in inlist:
    claims.append(Claim(ell))

# claim cloth segments
cloth = defaultdict(list)
for c in claims:
    for x in range(c.x, c.x + c.w ):
        for y in range(c.y, c.y + c.h):
            # if the cloth has already been claimed
            if len(cloth[(x,y)]) >= 1:
                # set original claim as invalid
                cloth[(x,y)][0].overlaps = True
                # set current claim as invalid
                c.overlaps = True
            # append the claim
            cloth[(x,y)].append(c)

for claim in claims:
    if not claim.overlaps:
        soln = claim.id

outfile = open("output2","w")
outfile.write(str(soln))
outfile.close()
