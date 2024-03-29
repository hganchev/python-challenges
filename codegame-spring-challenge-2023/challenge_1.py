import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cellsWithResources = [] # cells that formes the line to cell with resource
cellsWithEggs = [] # cells that formes the line to cell with resource
number_of_cells = int(input())  # amount of hexagonal cells in this map
print("number_of_cells: ", number_of_cells, file=sys.stderr, flush=True)
for i in range(number_of_cells):
    # _type: 0 for empty, 1 for eggs, 2 for crystal
    # initial_resources: the initial amount of eggs/crystals on this cell
    # neigh_0: the index of the neighbouring cell for each direction
    _type, initial_resources, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    if _type == 1:
        cellsWithEggs.append(i)
    if _type == 2:
        cellsWithResources.append(i)
    

number_of_bases = int(input())
print("input: ", number_of_bases, file=sys.stderr, flush=True)
if number_of_bases == 1:
    for i in input().split():
        my_base_index = int(i)
        print("mybase: ", int(i), file=sys.stderr, flush=True)
    for i in input().split():
        opp_base_index = int(i)
        print("oponent base: ", int(i), file=sys.stderr, flush=True)

    # Sort for closest ones
    if my_base_index > 30:
        cellsWithEggs.sort(reverse = True)
        cellsWithResources.sort(reverse = True)
    else:
        cellsWithEggs.sort()
        cellsWithResources.sort()

    # Do the actions
    actions = []
    for cell in cellsWithEggs:
        actions.append("LINE " + str(my_base_index) + " " + str(cell) + " " + str(2))
    for cell in cellsWithResources:
        actions.append("LINE " + str(my_base_index) + " " + str(cell) + " " + str(2))
else:
    my_base_index = []
    opp_base_index = []
    for i in input().split():
        my_base_index.append(int(i))
        print("mybase: ", int(i), file=sys.stderr, flush=True)
    for i in input().split():
        opp_base_index.append(int(i))
        print("oponent base: ", int(i), file=sys.stderr, flush=True)

    # Sort for closest ones
    cellsWithEggs.sort()
    cellsWithResources.sort()

    # Do the actions
    actions = []
    for cell in cellsWithEggs:
        for base_index in my_base_index:
            actions.append("LINE " + str(base_index) + " " + str(cell) + " " + str(2))
    for cell in cellsWithResources:
        for base_index in my_base_index:
            actions.append("LINE " + str(base_index) + " " + str(cell) + " " + str(2))

# game loop
while True:
    for i in range(number_of_cells):
        # resources: the current amount of eggs/crystals on this cell
        # my_ants: the amount of your ants on this cell
        # opp_ants: the amount of opponent ants on this cell
        resources, my_ants, opp_ants = [int(j) for j in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print("resources: ", resources, file=sys.stderr, flush=True)
    print("my_ants: ", my_ants, file=sys.stderr, flush=True)
    print("opp_ants: ", opp_ants, file=sys.stderr, flush=True)
    # WAIT | LINE <sourceIdx> <targetIdx> <strength> | BEACON <cellIdx> <strength> | MESSAGE <text>
    print("actions: ", actions, file=sys.stderr, flush=True)

    # TODO: choose actions to perform and push them into actions
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if len(actions) == 0:
        print('WAIT')
    else:
        print(';'.join(actions))
