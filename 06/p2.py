#! /usr/bin/python
# https://adventofcode.com/2018/day/6

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

# create points from input
def parseInputToPoints(lines):
    points = []

    pattern = re.compile(r"\s*(\d*),\s*(\d*)")
    for line in lines:
        match = pattern.match(line)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            points.append((x,y))

    return points


# manhattan distance
def mhd(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def findSoln(points):
    xlo = min([x for x,y in points])
    xhi = max([x for x,y in points])
    ylo = min([y for x,y in points])
    yhi = max([y for x,y in points])

    # default dict to hold score
    score = defaultdict(int)

    # find scores
    for x in range(xlo, xhi+1):
        for y in range(ylo, yhi+1):
            for point in points:
                score[(x,y)] += mhd((x,y),point)

    # find the size of the area
    size = 0
    for k in score:
        if score[k] < 10000:
            size += 1

    return size

def writeSoln(part, soln):
    outfile = open("output" + str(part), "w")
    outfile.write(str(soln))
    outfile.close()

def main():
    lines = readInput()
    points = parseInputToPoints(lines)
    soln = findSoln(points)
    writeSoln(2,soln)

main()
