"""
Maria Jose Rosales
conway.py
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]



def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)


def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    '''glider = np.array([[0, 0, 0, 0],
                       [0, 255, 255, 0],
                       [0, 255, 255, 0],
                       [0, 0, 0, 0]])
    grid[i:i + 4, j:j + 4] = glider'''


def patterns(grid, N):
    numBlock = 0
    numBeehive = 0
    numLoaf = 0
    numBoat = 0
    numTub = 0
    numverBlinker = 0
    numhorBlinker = 0
    numverToad =0
    numhorToad =0
    numBeacon4=0
    numBeacon3 = 0
    block = np.array([[0, 0, 0, 0],
                      [0, 255, 255, 0],
                      [0, 255, 255, 0],
                      [0, 0, 0, 0]])

    beehive = np.array([[0, 0, 0, 0, 0, 0],
                        [0, 0, 255, 255, 0, 0],
                        [0, 255, 0, 0, 255, 0],
                        [0, 0, 255, 255, 0, 0],
                        [0, 0, 0, 0, 0, 0]])

    loaf = np.array([[0, 0, 0, 0, 0, 0],
                     [0, 0, 255, 255, 0, 0],
                     [0, 255, 0, 0, 255, 0],
                     [0, 0, 255, 0, 255, 0],
                     [0, 0, 0, 255, 0, 0],
                     [0, 0, 0, 0, 0, 0]])

    boat = np.array([[0, 0, 0, 0, 0, ],
                     [0, 255, 255, 0, 0],
                     [0, 255, 0, 255, 0],
                     [0, 0, 255, 0, 0],
                     [0, 0, 0, 0, 0]])

    tub = np.array([[0, 0, 0, 0, 0],
                    [0, 0, 255, 0, 0],
                    [0, 255, 0, 255, 0],
                    [0, 0, 255, 0, 0],
                    [0, 0, 0, 0, 0]])

    verBlinker = np.array([[0,0,0,0,0],
                        [0,0,255,0,0],
                        [0,0,255,0,0],
                        [0,0,255,0,0],
                        [0,0,0,0,0]])
    horBlinker = np.array([[0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,255,255,255,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],])

    verToad = np.array([[0,0,0,0,0,0],
                     [0,0,0,255,0,0],
                     [0,255,0,0,255,0],
                     [0,255,0,0,255,0],
                     [0,0,255,0,0,0],
                     [0,0,0,0,0,0]])

    horToad = np.array([[0,0,0,0,0,0],
                       [0,0,0,0,0,0],
                       [0,0,255,255,255,0],
                       [0,255,255,255,0,0],
                       [0,0,0,0,0,0],
                       [0,0,0,0,0,0]])

    beacon4 = np.array([[0,0,0,0,0,0],
                       [0,255,255,0,0,0],
                       [0,255,255,0,0,0],
                       [0,0,0,255,255,0],
                       [0,0,0,255,255,0],
                       [0,0,0,0,0,0]])

    beacon3 =np.array([[0,0,0,0,0,0],
                       [0,255,255,0,0,0],
                       [0,255,0,0,0,0],
                       [0,0,0,0,255,0],
                       [0,0,0,255,255,0],
                       [0,0,0,0,0,0]])

    print("Block: ", findBlock(grid, numBlock, block, N))
    print("Beehive", findBeehive(grid, numBeehive, beehive, N))
    print("Loaf ", findLoaf(grid, numLoaf, loaf, N))
    print("Boat", findBoat(grid, numBoat, boat, N))
    print("Tub", findTub(grid, numTub, tub, N))
    print("V Blinker ", findverBlinker(grid,numverBlinker,verBlinker,N))
    print("H Blinker ", findhorBlinker(grid, numhorBlinker, horBlinker, N))
    print("V Toad ", findverToad(grid, numverToad,verToad,N))
    print("H Toad ", findhorToad(grid, numhorToad, horToad, N))
    print("Beacon ", findBeacon4(grid, numBeacon4, beacon4, N))
    print("Beacon ", findBeacon3(grid, numBeacon3, beacon3, N))


def findBlock(grid, numBlock, block, N):
    auxGrid = np.ones(N * N).reshape(N, N)
    blockGrid = np.zeros(16).reshape(4, 4)

    for i in range(len(grid) - 3):
        for j in range(len(grid) - 3):
            if auxGrid[i, j] == 1:
                for x in range(0, 4):
                    for y in range(0, 4):
                        blockGrid[x, y] = (grid[i + x, j + y])

                if np.all(blockGrid) == np.all(block):
                    numBlock += 1
                    for x in range(0, 4):
                        for y in range(0, 4):
                            auxGrid[x, y] = 0

    return numBlock


def findBeehive(grid, numBeehive, beehive, N):
    auxGrid = np.ones(N * N).reshape(N, N)
    beehiveGrid = np.zeros(30).reshape(6, 5)  # 6x5???

    for i in range(len(grid) - 5):
        for j in range(len(grid) - 4):  # por que 4?
            if auxGrid[i, j] == 1:
                for x in range(0, 6):
                    for y in range(0, 5):
                        beehiveGrid[x, y] = (grid[i + x, j + y])

                if np.all(beehiveGrid) == np.all(beehive):
                    numBeehive += 1
                    for x in range(0, 6):
                        for y in range(0, 5):
                            auxGrid[x, y] = 0

    return numBeehive


def findLoaf(grid, numLoaf, loaf, N):
    auxGrid = np.ones(N * N).reshape(N, N)
    loafGrid = np.zeros(36).reshape(6, 6)

    for i in range(len(grid) - 5):
        for j in range(len(grid) - 5):
            if auxGrid[i, j] == 1:
                for x in range(0, 6):
                    for y in range(0, 6):
                        loafGrid[x, y] = (grid[i + x, j + y])

                if np.all(loafGrid) == np.all(loaf):
                    numLoaf += 1
                    for x in range(0, 6):
                        for y in range(0, 6):
                            auxGrid[x, y] = 0

    return numLoaf


def findBoat(grid, numBoat, boat, N):
    auxGrid = np.ones(N * N).reshape(N, N)
    boatGrid = np.zeros(25).reshape(5, 5)
    for i in range(len(grid) - 4):
        for j in range(len(grid) - 4):
            if auxGrid[i, j] == 1:
                for x in range(0, 5):
                    for y in range(0, 5):
                        boatGrid[x, y] = (grid[i + x, j + y])
                # print(boatGrid)
                if np.all(boatGrid) == np.all(boat):
                    # print(boat)
                    numBoat += 1
                    for x in range(0, 5):
                        for y in range(0, 5):
                            auxGrid[x, y] = 0

    return numBoat


def findTub(grid, numTub, tub, N):
    auxGrid = np.ones(N * N).reshape(N, N)
    tubGrid = np.zeros(25).reshape(5, 5)

    for i in range(len(grid) - 4):
        for j in range(len(grid) - 4):
            if auxGrid[i, j] == 1:
                for x in range(0, 5):
                    for y in range(0, 5):
                        tubGrid[x, y] = (grid[i + x, j + y])

                if np.all(tubGrid) == np.all(tub):
                    numTub += 1
                    for x in range(0, 5):
                        for y in range(0, 5):
                            auxGrid[x, y] = 0

    return numTub

def findverBlinker(grid,numverBlinker,verBlinker,N):
        auxGrid = np.ones(N * N).reshape(N, N)
        blinkerGrid = np.zeros(25).reshape(5, 5)

        for i in range(len(grid) - 4):
            for j in range(len(grid) - 4):
                if auxGrid[i, j] == 1:
                    for x in range(0, 5):
                        for y in range(0, 5):
                            blinkerGrid[x, y] = (grid[i + x, j + y])

                    if np.all(blinkerGrid) == np.all(verBlinker):
                        numverBlinker += 1
                        for x in range(0, 5):
                            for y in range(0, 5):
                                auxGrid[x, y] = 0

        return numverBlinker


def findhorBlinker(grid, numhorBlinker, horBlinker, N):
    auxGrid = np.ones(N * N).reshape(N, N)
    blinkerGrid = np.zeros(25).reshape(5, 5)

    for i in range(len(grid) - 5):
        for j in range(len(grid) - 5):
            if auxGrid[i, j] == 1:
                for x in range(0, 5):
                    for y in range(0, 5):
                        blinkerGrid[x, y] = (grid[i + x, j + y])

                if np.all(blinkerGrid) == np.all(horBlinker):
                    numhorBlinker += 1
                    for x in range(0, 5):
                        for y in range(0, 5):
                            auxGrid[x, y] = 0

    return numhorBlinker

def findverToad(grid,numverToad,verToad,N):
    auxGrid = np.ones(N * N).reshape(N, N)
    toadGrid = np.zeros(36).reshape(6, 6)

    for i in range(len(grid) - 5):
        for j in range(len(grid) - 5):
            if auxGrid[i, j] == 1:
                for x in range(0, 6):
                    for y in range(0, 6):
                        toadGrid[x, y] = (grid[i + x, j + y])

                if np.all(toadGrid) == np.all(verToad):
                    numverToad += 1
                    for x in range(0, 6):
                        for y in range(0, 6):
                            auxGrid[x, y] = 0

    return numverToad

def findhorToad(grid,numhorToad,horToad,N):
    auxGrid = np.ones(N * N).reshape(N, N)
    toadGrid = np.zeros(36).reshape(6, 6)

    for i in range(len(grid) - 5):
        for j in range(len(grid) - 5):
            if auxGrid[i, j] == 1:
                for x in range(0, 6):
                    for y in range(0, 6):
                        toadGrid[x, y] = (grid[i + x, j + y])

                if np.all(toadGrid) == np.all(horToad):
                    numhorToad += 1
                    for x in range(0, 6):
                        for y in range(0, 6):
                            auxGrid[x, y] = 0

    return numhorToad

def findBeacon4(grid,numBeacon4,beacon4,N):
    auxGrid = np.ones(N * N).reshape(N, N)
    beaconGrid = np.zeros(16).reshape(4, 4)

    for i in range(len(grid) - 3):
        for j in range(len(grid) - 3):
            if auxGrid[i, j] == 1:
                for x in range(0, 4):
                    for y in range(0, 4):
                        beaconGrid[x, y] = (grid[i + x, j + y])

                if np.all(beaconGrid) == np.all(beacon4):
                    numBeacon4 += 1
                    for x in range(0, 4):
                        for y in range(0, 4):
                            auxGrid[x, y] = 0

    return numBeacon4

def findBeacon3(grid,numBeacon3,beacon3,N):
    auxGrid = np.ones(N * N).reshape(N, N)
    beaconGrid = np.zeros(36).reshape(6, 6)

    for i in range(len(grid) - 5):
        for j in range(len(grid) - 5):
            if auxGrid[i, j] == 1:
                for x in range(0, 6):
                    for y in range(0, 6):
                        beaconGrid[x, y] = (grid[i + x, j + y])

                if np.all(beaconGrid) == np.all(beacon3):
                    numBeacon3 += 1
                    for x in range(0, 6):
                        for y in range(0, 6):
                            auxGrid[x, y] = 0

    return numBeacon3

def neighbors(N, grid, i, j):
    livecells = 0

    if grid[i, (j - 1) % N] == 255:
        livecells += 1
    if grid[i, (j + 1) % N] == 255:
        livecells += 1
    if grid[(i - 1) % N, j] == 255:
        livecells += 1
    if grid[(i + 1) % N, j] == 255:
        livecells += 1
    if grid[(i - 1) % N, (j - 1) % N] == 255:
        livecells += 1
    if grid[(i - 1) % N, (j + 1) % N] == 255:
        livecells += 1
    if grid[(i + 1) % N, (j - 1) % N] == 255:
        livecells += 1
    if grid[(i + 1) % N, (j + 1) % N] == 255:
        livecells += 1
    return livecells


def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()
    # TODO: Implement the rules of Conway's Game of Life

    for i in range(len(grid)):
        for j in range(len(grid)):
            # print(i,j)
            cells = neighbors(N, grid, i, j)
            if (cells < 2) or (cells > 3):
                newGrid[i, j] = OFF
            else:
                if cells == 3:
                    newGrid[i, j] = ON

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,


# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments



    # set grid size
   #N = 5

    # set animation update interval
    updateInterval = 50

    # declare grid
    grid = np.array([])
    N=0
    with open('inputCW.txt', 'r') as f:
        lines = f.readlines()
        # print(lines)
        for i in range(len(lines)):
            if i == 0:
                N = int(lines[i])
                grid = np.zeros(N * N).reshape(N, N)
                continue
            coord = lines[i].split(",")
            x = int(coord[0])
            y = int(coord[1])
            #grid[y][x] = 255

    print(N)

    # Uncomment lines to see the "glider" demo

    addGlider(1, 1, grid)
    # populate grid with random on/off - more off than on
    grid = randomGrid(N)





    patterns(grid, N)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N,),
                                  frames=10,
                                  interval=updateInterval,
                                  save_count=50,
                                  repeat=False)

    plt.show()


# call main
if __name__ == '__main__':
    main()
