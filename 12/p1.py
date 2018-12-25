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
        instr = infile.readline()

        if instr == '': # eof
            break

        instr = instr.strip()

        lines.append(instr)
    infile.close()
    return lines

def parseInput(lines):
    pattern = re.compile(r"initial state: (.*)")
    match = pattern.match(lines[0])
    initial = match.group(1)

    pattern = re.compile(r"(.*) => (.*)")
    rules = {}
    for line in lines[1:]:
        match = pattern.match(line)
        if match:
            rule = match.group(1)
            result = rule
            result = result[:2] + match.group(2) + result[3:]
            rules[rule] = result

    return initial,rules

def findSoln(initial,rules):
    state = initial
    for k in rules:
    for gen in range(21):


def main():
    lines = readInput()
    initial,rules = parseInput(lines)

main()
