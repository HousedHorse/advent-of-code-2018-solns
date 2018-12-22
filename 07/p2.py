#! /usr/bin/python
# https://adventofcode.com/2018/day/1

from collections import defaultdict
import re
from string import ascii_uppercase

# representation of a graph
class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.adj[u].sort(reverse=True)

    def __repr__(self):
        s = ""
        for k in sorted(self.adj):
            s += f"{k} -> "
            for v in self.adj[k]:
                s += f"{v}, "
            s += "\r\n"
        return s

    # Khan's algorithm
    def topOrder(self):
        # store in degree of each vertex
        inDegree = defaultdict(int)

        # calculate in degree of each vertex
        for u in list(self.adj):
            for v in self.adj[u]:
                inDegree[v] += 1

        # queue to store all vertices with in degree 0
        queue = []
        for u in list(self.adj):
            if inDegree[u] == 0:
                queue.append(u)

        # store topological ordering of vertices
        order = []

        while queue:
            u = queue.pop(0)
            order.append(u)

            for v in self.adj[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    queue.append(v)
            # keep things sorted alphabetically
            queue.sort()

        return order

    def work(self,workers):
        # define a dictionary with times
        time = {}
        for i,u in enumerate(ascii_uppercase):
            time[u] = 60 + i + 1

        # store in degree of each vertex
        inDegree = defaultdict(int)

        # calculate in degree of each vertex
        for u in list(self.adj):
            for v in self.adj[u]:
                inDegree[v] += 1

        # queue to store all vertices with in degree 0
        queue = []
        for u in list(self.adj):
            if inDegree[u] == 0:
                queue.append(u)

        # set to store tasks in progress
        inProgress = set()

        timeTaken = 0
        queue.sort()
        while queue or inProgress:
            # dispatch workers to available vertices
            while workers > 0 and queue:
                workers -= 1
                u = queue.pop(0)
                inProgress.add(u)
                print(f"{timeTaken}: starting {u}!")

            timeTaken += 1

            # work on in progress vertices
            for v in list(inProgress):
                time[v] -= 1
                if time[v] == 0:
                    print(f"{timeTaken}: done {v}!")
                    inProgress.remove(v)
                    workers += 1
                    for u in self.adj[v]:
                        inDegree[u] -= 1
                        if inDegree[u] == 0:
                            queue.append(u)

            # keep things sorted alphabetically
            queue.sort()

        return timeTaken

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

def parseInput(lines):
    # dictionary representation for the graph
    graph = Graph()

    pattern = re.compile(r"Step ([A-Z]) must be finished before step ([A-Z])")
    for line in lines:
        match = pattern.match(line)
        if match:
            # add vertex (if necessary) and its directed edge
            graph.addEdge(match.group(1),match.group(2))

    print(graph)
    return graph

def stackToString(stack):
    s = ""
    for i in stack:
        s += i
    return s

def writeSoln(part, soln):
    outfile = open("output" + str(part), "w")
    outfile.write(str(soln))
    outfile.close()

def main():
    lines = readInput()
    graph = parseInput(lines)
    soln = graph.work(5)
    print(soln)
    writeSoln(2,soln)

main()
