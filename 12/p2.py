#! /usr/bin/python
# https://adventofcode.com/2018/day/12

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

    initial = initial

    pattern = re.compile(r"(.*) => (.*)")
    rules = {}
    for line in lines[1:]:
        match = pattern.match(line)
        if match:
            rule = match.group(1)
            result = match.group(2)
            rules[rule] = result

    return initial,rules

def findSoln(initial,rules):
    state = initial
    offset = 0
    for gen in range(1000):
        state = '.....'+state+'.....'
        offset += 5
        newState = ['.' for _ in state]
        for i in range(len(state)-2):
            pattern = state[i:i+5]
            if pattern in [k for k in rules]:
                newState[i+2] = rules[pattern]
            else:
                newState[i+2] = '.'
        state = ''.join(newState)
        # strip extra dots 
        oldlen = len(state)
        state = state.lstrip('.')
        offset -= (oldlen-len(state))
        state = state.rstrip('.')
        print(state,offset)

    # this is really hacky
    # noticed that it devolves into a stable pattern somwhere around 1000 generations
    # then we can just manually check the offset for the 50000000000th
    offset = -940 - int(49999999000)

    soln = 0
    for i,c in enumerate(state):
        if c == '#': 
            soln += (i-offset)

    print(soln)

def main():
    lines = readInput()
    initial,rules = parseInput(lines)
    findSoln(initial,rules)

main()
