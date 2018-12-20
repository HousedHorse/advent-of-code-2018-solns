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

def writeSoln(part, soln):
    outfile = open("output" + str(part), "w")
    outfile.write(str(soln))
    outfile.close()

def main():
    lines = readInput()
    soln = scan(lines[0])
    writeSoln(1,soln)

main()
