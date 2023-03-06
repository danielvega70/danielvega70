import sys

class Node():
    def_init_(self, state, parent, action)
        self.state = state 
        self.parent = parent 
    self.action = action 


class stackFrontier():
    def_init_(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class Maze:
    def __init__(self, filename):
        # read maze from file and set height and width of maze
        with open(filename) as f:
            contents = f.read()

        # validate start and goal
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # determine height and width of maze
        self.height = contents.count("\n") + 1
        self.width = max(len(line) for line in contents.split("\n"))

        # keep track of walls
        self.walls = []
        lines = contents.split("\n")
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if lines[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif lines[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif lines[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

    def in_bounds(self, id):
        i, j = id
        return 0 <= i < self.height and 0 <= j < self.width

    def passable(self, id):
        return not self.walls[id[0]][id[1]]

    def neighbors(self, id):
        i, j = id
        results = [(i+1, j), (i, j-1), (i-1, j), (i, j+1)]
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def cost(self, current, next):
        return 1

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
