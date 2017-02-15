# Hello World program in Python

import sys

method = sys.argv[1]
boardARGV2 = sys.argv[2]

f = open('output.txt', 'w')
f.write('argv1 ' + method + "\n")  # python will convert \n to os.linesep
f.write('argv2 ' + boardARGV2 + "\n")  # python will convert \n to os.linesep
#! python
#sys.stdout.write("hello from Python %s\n" % (sys.version,))

#TODO create state a state class
#TODO creat a solver class 
#TODO create a board class

class State:

    def __init__(self):
        self.path_to_goal = 0
        self.cost_of_path = 0
        self.nodes_expanded = 0
        self.fringe_size = 0
        self.max_fringe_size = 0
        self.search_depth = 0
        self.max_search_depth = 0
        self.running_time = 0
        self.max_ram_usage = 0

    def incNodes_expanded(self):
        self.nodes_expanded += 1

    def incFringe_size(self):
        self.fringe_size += 1
    

class Board:
 
    def __init__(self):
        self.parent = sys.argv[2]
        self.child = []

    def getParent(self):
        return self.parent
        
    def getChild(self):
        return self.child

    def setParent(self, parent):
        self.parent = parent

    def setChild(self):
        self.child = child

b = Board()
b2 = Board()
b3 = Board()

answer = b.getParent()
b2.setParent('new Parent man')

f.write ("class test: " + answer + "\n")
f.write ("class test: " + b2.getParent() + "\n")

f.write('path_to_goal: ' + "\n")
f.write('cost_of_path: ' + "\n")
f.write('nodes_expanded: ' + "\n")
f.write('fringe_size: ' + "\n")
f.write('max_fringe_size: ' + "\n")
f.write('search_depth: ' + "\n")
f.write('max_search_depth: ' + "\n")
f.write('running_time: ' + "\n")
f.write('max_ram_usage: ' + "\n") 

f.close()  # you can omit in most cases as the destructor will call it
