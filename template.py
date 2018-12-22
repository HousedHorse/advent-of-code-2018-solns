#! /usr/bin/python
# https://adventofcode.com/2018/day/1

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

def writeSoln(part, soln):
    outfile = open("output" + str(part), "w")
    outfile.write(str(soln))
    outfile.close()

def main():
    lines = readInput()
    writeSoln(1,"foo")

main()
