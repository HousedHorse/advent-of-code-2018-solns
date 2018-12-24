#! /usr/bin/python
# https://adventofcode.com/2018/day/11

from collections import defaultdict
import re

# puzzle input
puzzleInput = 6042

class Grid:
    def __init__(self,gsn):
        self.grid = []
        # hold sums of vertical strips of size 1 .. 300
        self.stripSum = [[[0 for _ in range(300)] for _ in range(300)] for _ in range(301)]

        for x in range(1,301):
            self.grid.append([])
            for y in range(1,301):
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
                self.grid[x - 1].append(power)

        # preprocess the matrix to calculate stripsums
        self.preProcess()

    # calculate strip sums for k = 1 up to N
    def preProcess(self):
        for k in range (300):
            # column by column
            for x in range (300):
                # first kx1 rectangle
                total = 0
                for y in range(k):
                    total += self.grid[x][y]
                self.stripSum[k][x][0] = total

                # remaining rectangles
                for y in range(1,300-k):
                    total += self.grid[x][y+k-1] - self.grid[x][y-1]
                    self.stripSum[k][x][y] = total

    def maxSumNxN(self,size):
        total = 0
        maxtotal = None
        xhi = 0
        yhi = 0
        for j in range(0,300-size+1):

            total = 0
            # first subsquare in row j
            for i in range(0,size):
                total += self.stripSum[size][i][j]

            if maxtotal == None or total > maxtotal:
                maxtotal = total
                xhi,yhi = i,j

            # remaining subsqures in row j
            for i in range(1,300-size+1):
                total += self.stripSum[size][i+size-1][j] - self.stripSum[size][i-1][j]
                if maxtotal == None or total > maxtotal:
                    maxtotal = total
                    xhi,yhi = i,j

        xhi += 1
        yhi += 1
        return xhi,yhi,maxtotal

    def findHighestSum(self):
        highest = None
        xhi, yhi, sizehi = 0,0,0

        for size in range(1,301):
            x,y,total = self.maxSumNxN(size)
            if highest == None or total > highest:
                highest = total
                xhi,yhi,sizehi = x,y,size

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
