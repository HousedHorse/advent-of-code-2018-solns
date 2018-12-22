#! /usr/bin/python
# https://adventofcode.com/2018/day/8

from collections import defaultdict
import re

class Node:
    def __init__(self,children,data):
        self.children = children
        self.data = data

    def sumData(self):
        s = 0
        for d in self.data:
            s += d
        return s

    def sumTree(self):
        s = self.sumData()
        for c in self.children:
            s += c.sumTree()
        return s

    def __repr__(self):
        return self.toString(0)

    def toString(self,level):
        s = ""
        s += f"{level * '   '}{self.data}\n\r"
        for c in self.children:
            s += c.toString(level + 1)
        return s

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

def parseInput(s):
    nums = []

    # continually extract numbers from s
    pattern = re.compile(r"(\d*\s*)")
    while s:
        match = pattern.match(s)
        s = re.sub(match.group(1),'',s,1)
        nums.append(int(match.group(1).strip()))

    # root of the tree
    root = createTree(nums)

    return root

def createTree(nums):
    cnum = nums.pop(0)
    dnum = nums.pop(0)

    children = []
    data = []

    for i in range(cnum):
        children.append(createTree(nums))

    for i in range(dnum):
        data.append(nums.pop(0))

    return Node(children,data)

def main():
    lines = readInput()
    tree = parseInput(lines[0])
    print(tree.sumTree())

main()
