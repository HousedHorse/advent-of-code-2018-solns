#! /usr/bin/python
# https://adventofcode.com/2018/day/13

from collections import defaultdict
import re

class Tile:
    def __init__(self,c,x,y):
        self.x = x
        self.y = y
        if c not in "><v^":
            self.ascii = c
            self.cart = None
        elif c == '>':
            self.ascii = '-'
            self.cart = Cart(c)
        elif c == '<':
            self.ascii = '-'
            self.cart = Cart(c)
        elif c == 'v':
            self.ascii = '|'
            self.cart = Cart(c)
        elif c == '^':
            self.ascii = '|'
            self.cart = Cart(c)
        self.neighbors = defaultdict(lambda: None)

    def __repr__(self):
        if self.cart is not None:
            return str(self.cart)
        else:
            return self.ascii

    def __str__(self):
        return self.__repr__()

    def move(self):
        # if we have a cart
        if self.cart is not None and self.cart.moved == False:
            # move the cart
            dest = self.neighbors[self.cart.direction]
            if dest != None:
                self.cart.moved = True
                # if dest is a corner tile
                if dest.ascii == "/":
                    if self.cart.direction == 'r':
                        self.cart.direction = 'u'
                    elif self.cart.direction == 'l':
                        self.cart.direction = 'd'
                    elif self.cart.direction == 'u':
                        self.cart.direction = 'r'
                    elif self.cart.direction == 'd':
                        self.cart.direction = 'l'
                elif dest.ascii == "\\":
                    if self.cart.direction == 'r':
                        self.cart.direction = 'd'
                    elif self.cart.direction == 'l':
                        self.cart.direction = 'u'
                    elif self.cart.direction == 'u':
                        self.cart.direction = 'l'
                    elif self.cart.direction == 'd':
                        self.cart.direction = 'r'
                # if dest is a junction
                if dest.ascii == '+':
                    # turn according to cart memory
                    self.cart.turn()

                if dest.cart is not None:
                    # remove carts
                    dest.cart = None
                    self.cart = None
                    return 2
                else:
                    dest.cart = self.cart
                    self.cart = None

class Cart:
    def __init__(self,c):
        self.ascii = c
        self.turnCounter = 0
        self.moved = False
        self.display = {'r':'>','l':'<','u':'^','d':'v'}
        if c == '>':
            self.direction = 'r'
        elif c == '<':
            self.direction = 'l'
        elif c == 'v':
            self.direction = 'd'
        elif c == '^':
            self.direction = 'u'

    def __repr__(self):
        return self.display[self.direction]

    def __str__(self):
        return self.__repr__()

    def turn(self):
        # directions
        CW = {'u':'r','r':'d','d':'l','l':'u'}
        CCW = {'u':'l','l':'d','d':'r','r':'u'}

        if self.turnCounter == 0:
            self.direction = CCW[self.direction]
        elif self.turnCounter == 2:
            self.direction = CW[self.direction]
        self.turnCounter = (self.turnCounter + 1) % 3

class Layout:
    def __init__(self,lines):
        self.rows = []
        self.carts = 0
        for y,line in enumerate(lines):
            row = []
            for x,c in enumerate(line):
                if c in '><v^':
                    self.carts += 1
                tile = Tile(c,x,y)
                row.append(tile)
            self.rows.append(row)
        for y,row in enumerate(self.rows):
            for x,tile in enumerate(row):
                # set tile neigbors
                if x != 0:
                    tile.neighbors['l'] = row[x-1]
                if x < len(line)-1:
                    tile.neighbors['r'] = row[x+1]
                if y != 0:
                    tile.neighbors['u'] = self.rows[y-1][x]
                if y < len(self.rows)-1:
                    tile.neighbors['d'] = self.rows[y+1][x]

    def __repr__(self):
        s = ""
        for row in self.rows:
            for tile in row:
                s += str(tile)
            s += "\n\r"
        return s

    def __str__(self):
        return self.__repr__()

    def tick(self):
        result = 0
        for row in self.rows:
            for tile in row:
                if tile.cart is not None:
                    tile.cart.moved = False
        for row in self.rows:
            for tile in row:
                if tile.cart is not None:
                    temp = tile.move()
                    if temp is not None: result += temp
        return result

    def run(self):
        result = 0
        step = 0
        while True:
            #print(f'tick: {step}')
            #print(self)
            if self.carts == 1:
                for row in self.rows:
                    for tile in row:
                        if tile.cart is not None: print(tile.x,tile.y)
                break
            result = self.tick()
            if result !=0:
                print(f"crash occurred!")
                self.carts -= result
                print(f"{self.carts} carts left!")
            step += 1

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
    layout = Layout(lines)
    layout.run()

main()
