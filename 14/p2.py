#! /usr/bin/python
# https://adventofcode.com/2018/day/1

from collections import defaultdict
import re

# puzzle input 
puzzleInput = 920831
#puzzleInput = 18

def createNewRecipes(first, second, scores):
    total = scores[first] + scores[second]
    newScores = []

    if total < 10:
        newScores.append(total)
    else:
        newScores.append(int((total - (total % 10))/10))
        newScores.append(total % 10)

    for score in newScores:
        scores.append(score)

def selectRecipes(first,second,scores):
    stepsFirst  = 1 + scores[first]
    stepsSecond = 1 + scores[second]

    first  = (first + stepsFirst) % len(scores)
    second = (second + stepsSecond) % len(scores)

    return first,second

def findSoln(puzzleInput):
    puzzleInput = str(puzzleInput)
    scores = [3,7]
    first,second = 0,1
    # create new recipes until we reach puzzle input plus ten
    i = 0
    while True:
        createNewRecipes(first,second,scores)
        first,second = selectRecipes(first,second,scores)

        if len(scores) > len(puzzleInput):
            match = ''.join([str(score) for score in scores[i:i + len(puzzleInput)]])
            if match == puzzleInput: print(i); break
            i += 1

def main():
    findSoln(puzzleInput)

main()
