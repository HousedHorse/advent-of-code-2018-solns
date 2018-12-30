#! /usr/bin/python
# https://adventofcode.com/2018/day/15

from collections import defaultdict
import re
from functools import total_ordering

class Unit:
    def __init__(self,c,t,a):
        self.tile = t
        self.team = c
        self.hp = 200
        if self.team == 'G':
            self.attack = 3
        else:
            self.attack = a

    def __str__(self):
        return str(self.tile)

    def __repr__(self):
        return str(self)

    def move(self,d):
        if d.unit is not None:
            return
        self.tile.unit = None
        self.tile = d
        d.unit = self

    def attackEnemy(self,e):
        if e is None:
            return None
        e.hp -= self.attack
        if e.hp <= 0:
            team = e.tile.unit.team
            e.tile.unit = None
            return team
        return None

@total_ordering
class Tile:
    def __init__(self,c,x,y,a):
        self.x = x
        self.y = y
        self.wall = False
        if c in 'GE':
            self.unit = Unit(c,self,a)
        elif c == '#':
            self.wall = True
            self.unit = None
        else:
            self.unit = None

    def __str__(self):
        s = ''
        if self.wall:
            s += '#'
        elif self.unit is not None:
            s += self.unit.team
        else:
            s += '.'
        s += f'({self.x:3d},{self.y:3d})'
        return s

    def __repr__(self):
        return self.__str__()

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __lt__(self,other):
        if self.y < other.y:
            return True
        elif self.y == other.y:
            return self.x < other.x
        else:
            return False

    def __hash__(self):
        return hash((self.x,self.y))


class Graph:
    def __init__(self, lines, a):
        self.adj = defaultdict(list)
        self.order = []
        self.tiles = []
        for y,line in enumerate(lines):
            self.tiles.append([])
            for x,c in enumerate(line):
                tile = Tile(c,x,y,a)
                self.tiles[y].append(tile)
                if not tile.wall: self.order.append(tile)
        self.order.sort()
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                if not self.tiles[y][x].wall:
                    # add top if necessary
                    if y >= 1 and not self.tiles[y-1][x].wall:
                        self.addEdge(self.tiles[y][x],self.tiles[y-1][x])
                    # add left if necessary
                    if x >= 1 and not self.tiles[y][x-1].wall:
                        self.addEdge(self.tiles[y][x],self.tiles[y][x-1])
                    # add right if necessary
                    if x < len(self.tiles[y])-1 and not self.tiles[y][x+1].wall:
                        self.addEdge(self.tiles[y][x],self.tiles[y][x+1])
                    # add bottom if necessary
                    if y < len(self.tiles)-1 and not self.tiles[y+1][x].wall:
                        self.addEdge(self.tiles[y][x],self.tiles[y+1][x])

    def __str__(self):
        s = ''
        #for node in sorted(list(self.adj)):
        #    s += f'{str(node)} => '
        #    for child in self.adj[node]:
        #        s += f'{str(child)}, '
        #    s += '\n\r'
        #return s
        for line in self.tiles:
            for tile in line:
                s += str(tile)[0]
            s += '\n\r'
        return s

    def __repr__(self):
        return self.__str__()

    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.adj[u].sort()

    def bfs(self,s,condition):
        visited = set()
        queue = []
        parent = defaultdict(lambda: None)
        path = []

        queue.append(s)
        visited.add(s)

        while queue:
            s = queue.pop(0)
            # if we found our target
            if condition(s):
                curr = s
                while curr is not None:
                    path.insert(0,curr)
                    curr = parent[curr]
                return path
            for v in self.adj[s]:
                if v not in visited and v.unit is None:
                    visited.add(v)
                    parent[v] = s 
                    queue.append(v)
        return None

    # find the nearest goblin or elf to a given tile
    # use a closure to accomplish this via the bfs function
    def findEnemy(self,s,enemy):
        def nextTo(v):
            for u in self.adj[v]:
                if u.unit is not None and u.unit.team == enemy:
                    return True
            return False
        path = self.bfs(s,nextTo)
        if path is None: return None
        return path[1:]

class Game:
    def __init__(self,lines,a):
        self.graph = Graph(lines,a)
        self.elves = 0
        self.goblins = 0
        for t in self.graph.order:
            if t.unit is not None:
                if t.unit.team == 'E':
                    self.elves += 1
                if t.unit.team == 'G':
                    self.goblins += 1

    def __str__(self):
        return str(self.graph)

    def __repr__(self):
        return str(self)

    def turn(self):
        hasGone = set()
        for t in self.graph.order:
            unit = t.unit
            if unit is not None and unit not in hasGone:
                # check if combat is over
                if self.elves <= 0 or self.goblins <= 0:
                    hp = 0
                    for t in self.graph.order:
                        if t.unit is not None:
                            hp += t.unit.hp
                    return hp
                hasGone.add(unit)
                # find path to nearest enemy
                if unit.team == 'G':
                    enemy = 'E'
                else:
                    enemy = 'G'
                path = self.graph.findEnemy(t,enemy)
                # if we have no path, pass our turn
                if path is None: continue
                # if we are not next to an enemy already
                if len(path) > 0:
                    unit.move(path[0])
                # if we are next to an enemy
                # find target
                lowest = None
                target = None
                for v in self.graph.adj[unit.tile]:
                    if v.unit is not None and v.unit.team == enemy:
                        if lowest is None or v.unit.hp < lowest:
                            lowest = v.unit.hp
                            target = v.unit
                if target is not None:
                    killed = unit.attackEnemy(target)
                    if killed is not None:
                        if killed == 'E':
                            self.elves -= 1
                            return False
                        if killed == 'G':
                            self.goblins -= 1
        return None

    def run(self):
        turns = 1 
        while True:
            print(f'start turn {turns}')
            print(self.graph)
            result = self.turn()
            if result is False:
                return False
            if result is not None:
                print(result)
                print(turns - 1)
                return result * (turns - 1)
            turns += 1

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

def main():
    lines = readInput()
    i = 3
    while True:
        i += 1
        g = Game(lines,i)
        result = g.run()
        if result is False:
            continue
        else:
            print(result)
            break

main()
