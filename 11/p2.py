#! /usr/bin/python
# https://adventofcode.com/2018/day/11

from collections import defaultdict
import re

# puzzle input
puzzleInput = 6042

class Grid:
    def __init__(self,gsn):
        self.grid = []
        for y in range(1,301):
            self.grid.append([])
            for x in range(1,301):
                rackId = x + 10
                power = ((rackId * y) + gsn) * rackId
                # keep only 100's digit
                if power >= 100:
                    power = power % 1000
                    power -= (power % 100)
                    power = int(power/100)
                else:
                    power = 0
                power -= 5
                self.grid[y - 1].append(power)

    def sumnxn(self,x,y,size):
        # check we will be on the grid
        if x < 1 or y < 1 or x > (300 - size) or y > (300 - size):
            return None

        # normalize to deal with a list
        x -= 1
        y -= 1

        total = 0
        for i in range(y,y+size):
            for j in range(x,x+size):
                total += self.grid[i][j]

        return total

    def findHighestSum(self):
        total = None
        xhi, yhi, sizehi = 0,0,0

        for size in range(1,301):
            for y in range(1,301):
                for x in range(1,301):
                    newSum = self.sumnxn(x,y,size)
                    if newSum != None and (total == None or newSum > total):
                        total = newSum
                        xhi = x
                        yhi = y
                        sizehi = size

        return xhi,yhi,sizehi

    def __repr__(self):
        s = ""
        for y in self.grid:
            for x in y:
                s += f"{x} "
            s += "\n\r"
        return s

def main():
    grid = Grid(puzzleInput)
    print(grid.findHighestSum())

main()
