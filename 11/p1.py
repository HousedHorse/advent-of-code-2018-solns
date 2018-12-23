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

    def sum3x3(self,x,y):
        # check we will be on the grid
        if x < 1 or y < 1 or x > (300 - 3) or y > (300 - 3):
            return None

        # normalize to deal with a list
        x -= 1
        y -= 1

        total = 0
        for i in range(y,y+3):
            for j in range(x,x+3):
                total += self.grid[i][j]

        return total

    def findHighestSum(self):
        total = None
        xhi, yhi = 0,0

        for y in range(1,301):
            for x in range(1,301):
                newSum = self.sum3x3(x,y)
                if newSum != None and (total == None or newSum > total):
                    total = newSum
                    xhi = x
                    yhi = y

        return xhi,yhi

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
