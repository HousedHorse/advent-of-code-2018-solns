#! /usr/bin/python
# https://adventofcode.com/2018/day/4

from collections import defaultdict
from functools import total_ordering
import re

# a class to represent event times
@total_ordering
class Time:
    def __init__(self,y,mo,d,h,mi):
        self.year   = y
        self.month  = mo
        self.day    = d
        self.hour   = h
        self.minute = mi

    def __repr__(self):
        return f"[{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}]"


    # a time is equal if all its fields are equal
    def __eq__(self,other):
        return (self.year == other.year and self.month == other.month and 
                self.day == other.day and self.hour == other.hour and
                self.minute == other.minute)

    def __neq__(self,other):
        return not (self == other)

    # these if statements are ugly but the alternatives were uglier!
    def __lt__(self,other):
        if self.year < other.year:
            return True
        if self.year > other.year:
            return False
        if self.month < other.month:
            return True
        if self.month > other.month:
            return False
        if self.day < other.day:
            return True
        if self.day > other.day:
            return False
        if self.hour < other.hour:
            return True
        if self.hour > other.hour:
            return False
        if self.minute < other.minute:
            return True
        return False

    # we need this to hash our object
    def __key(self):
            return (self.year, self.month, self.day, self.hour, self.minute)

    # hash our object so we can use it as a key in our dictionary later
    def __hash__(self):
        return hash(self.__key())

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

def parseInput(lines):
    shift = re.compile(r"\[(\d*)-(\d*)-(\d*)\s*(\d*):(\d*)\]\s*Guard\s*#(\d*)")
    sleep = re.compile(r"\[(\d*)-(\d*)-(\d*)\s*(\d*):(\d*)\]\s*falls\s*a(sleep)")
    wake = re.compile(r"\[(\d*)-(\d*)-(\d*)\s*(\d*):(\d*)\]\s*(wake)s\s*up")
    events = {}

    for line in lines:
        match = None
        i = 0
        # parse the line depending on line type
        while(match == None):
            if i == 0: match = shift.match(line)
            if i == 1: match = sleep.match(line)
            if i == 2: match = wake.match(line)
            if i == 3: break
            i += 1
        # log event
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        hour = match.group(4)
        minute = match.group(5)
        # create a time object to rep event time
        time = Time(year,month,day,hour,minute)
        # add the event to the dictionary by time
        events[time] = match.group(6)

    return events

def processInput(events):
    sleptMinutes = defaultdict(int)
    sortedTimes  = sorted(events.keys())
    for time in sortedTimes:
        # guard watch event
        if events[time].isdigit():
            gid = int(events[time])
        # guard sleep event
        elif events[time] == "sleep":
            sleepTime = int(time.minute)
        # guard wake event
        elif events[time] == "wake":
            wakeTime    = int(time.minute)
            # what minutes does he sleep?
            for minute in range(sleepTime,wakeTime+1):
                sleptMinutes[(gid,minute)] += 1

    # find the highest minute slept by any guard
    maxMinuteNum = 0
    maxMinute    = 0
    for (gid,m) in sleptMinutes:
        if sleptMinutes[(gid,m)] > maxMinuteNum:
            maxMinuteNum = sleptMinutes[(gid,m)]
            maxMinute    = m
            maxGuard     = gid

    # find the answer
    return str(maxMinute * maxGuard)

def main():
    lines = readInput()
    events = parseInput(lines)
    writeSoln(2,processInput(events))

main()
