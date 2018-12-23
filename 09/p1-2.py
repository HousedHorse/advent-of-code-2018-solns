#! /usr/bin/python
# https://adventofcode.com/2018/day/1

from collections import defaultdict
from collections import deque
import re

# 465 players; last marble is worth 71498 points

players = 465
# part 1 has last = 71498
last = 7149800

def placeMarbles():
    marble = 0
    circle = deque([0])
    scores = defaultdict(int)

    while True:
        # next marble
        player = (marble % players) + 1
        marble += 1 

        if marble % 23 != 0:
            circle.rotate(-1)
            circle.append(marble)
        else:
            points = marble
            circle.rotate(7)
            points += circle.pop()
            scores[player] += points
            circle.rotate(-1)
        if marble == last: break

    return max(scores.values())

def main():
    print(placeMarbles())

main()
