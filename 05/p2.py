#! /usr/bin/python
# https://adventofcode.com/2018/day/5

from string import ascii_lowercase
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

# figure out a length
def scan(p):
    match = {}
    for c in ascii_lowercase:
        match[c.lower()] = c.upper()
        match[c.upper()] = c.lower()

    soln = []
    for c in p:
        if soln and c == match[soln[-1]]:
            soln.pop()
        else:
            soln.append(c)

    return len(soln)

# attempt without certain units
def scanWithout(p,u):
    p = p.replace(f"{u.lower()}","")
    p = p.replace(f"{u.upper()}","")
    newLen = scan(p)

    return newLen

def tryAllPossibilities(p):
    lens = {}
    for c in ascii_lowercase:
        lens[c] = scanWithout(p,c)

    minLen = None
    for k in lens:
        if not minLen or lens[k] < minLen:
            minLen = lens[k]

    return minLen

def writeSoln(part, soln):
    outfile = open("output" + str(part), "w")
    outfile.write(str(soln))
    outfile.close()

def main():
    lines = readInput()
    soln = tryAllPossibilities(lines[0])
    writeSoln(2,soln)

main()
