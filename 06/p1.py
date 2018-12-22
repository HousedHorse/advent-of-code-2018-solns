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

def closest(p,points):
    best = points[0]
    tie = False

    for point in points[1:]:
        x1,y1 = point
        x2,y2 = p
        if mhd(point,p) < mhd(best,p):
            best = point
            tie = False
        elif mhd(point,p) == mhd(best,p):
            tie = True

    if tie:
        return (-1,-1)
    else:
        return best

def findSoln(points):
    xlo = min([x for x,y in points])
    xhi = max([x for x,y in points])
    ylo = min([y for x,y in points])
    yhi = max([y for x,y in points])

    # set to hold infinite points
    inf = set()
    # default dict to hold score
    score = defaultdict(int)

    # find scores
    for x in range(xlo, xhi+1):
        for y in range(ylo, yhi+1):
            point = closest((x,y),points)
            if point != (-1,-1):
                score[point] += 1

    # handle infinite regions...
    # we choose 50 as a far enough outer perimeter
    # and we posit that a point closest to this perimeter is
    # in the infinite score set
    # top of square
    for x in range(xlo-1,xhi+2):
        inf.add(closest((x,ylo-50),points))
    # bottom of square
    for x in range(xlo-1,xhi+2):
        inf.add(closest((x,yhi+50),points))
    # left of square
    for y in range(ylo-1,yhi+2):
        inf.add(closest((xlo-50,y),points))
    # right of square
    for y in range(ylo-1,yhi+2):
        inf.add(closest((xhi+50,y),points))

    # find the best area
    # that is, the largest finite score
    best = None
    for k in score:
        if k not in inf and (best is None or score[k] > best):
            best = score[k]

    return best

def writeSoln(part, soln):
    outfile = open("output" + str(part), "w")
    outfile.write(str(soln))
    outfile.close()

def main():
    lines = readInput()
    points = parseInputToPoints(lines)
    soln = findSoln(points)
    writeSoln(1,soln)

main()
