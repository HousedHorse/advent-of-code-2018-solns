#! /usr/bin/python
# https://adventofcode.com/2018/day/10

from collections import defaultdict
import re

def readInput():
    # read file into a list of lines
    infile = open("input","r")
    lines = []
    while True:
        # read line and strip newline characters
        instr = infile.readline().rstrip("\r\n")

        if instr == '': # eof
            break

        lines.append(instr)
    infile.close()
    return lines

def parseInput(lines):
    stars = []

    pattern = re.compile(r".*<\s*(-*\d*),\s*(-*\d*)>.*<\s*(-*\d*),\s*(-*\d*)")

    for line in lines:
        match = pattern.match(line)

        px = int(match.group(1))
        py = int(match.group(2))
        vx = int(match.group(3))
        vy = int(match.group(4))

        stars.append([px,py,vx,vy])

    return stars

def printPossibleSolns(stars,breakPoint):
    # keep going until we decide to stop
    time = 0
    for i in range(breakPoint):
        # we need some meta-data on the stars
        xlo = min([x for x,y,_,_ in stars])
        xhi = max([x for x,y,_,_ in stars])
        ylo = min([y for x,y,_,_ in stars])
        yhi = max([y for x,y,_,_ in stars])

        # check to see if what we have is good or garbage
        # we will check to see if stars are similar in height
        if abs(ylo - yhi) <= 30:
            for y in range(ylo,yhi+1):
                for x in range(xlo,xhi+1):
                    if (x,y) in [(x,y) for x,y,_,_ in stars]:
                        print('#',end='')
                    else:
                        print('.',end='')
                print()
            print(f"time for above was {time}\n\r")

        for star in stars:
            star[0] += star[2] # increment x
            star[1] += star[3] # increment y

        time += 1

def main():
    lines = readInput()
    stars = parseInput(lines)

    printPossibleSolns(stars,100000)

main()
