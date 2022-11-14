import numpy as np

class gameoflifegrid():
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.grid = np.zeros((rows,cols)).reshape((rows,cols))
        self.newGrid = np.zeros((rows,cols)).reshape((rows,cols))


    def neighbors(self,r,c):
        neighbor = []
        for i in range(r-1,r+2):
            for j in range(c-1,c+2):
                if i>=0 and i<self.rows and j>=0 and j<self.cols and (i!=r or j!=c):
                    neighbor.append((i,j))
        return neighbor


    def aliveneighbors(self,r,c):
        alive = 0
        for (row,column) in self.neighbors(r,c):
            alive += self.grid[row][column]
        return alive


    def nextstep(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 1:
                    if self.aliveneighbors(r, c) == 2 or self.aliveneighbors(r, c) == 3:
                        self.newGrid[r][c] = 1
                    else:
                        self.newGrid[r][c] = 0
                if self.grid[r][c] == 0:
                    if self.aliveneighbors(r, c) == 3:
                        self.newGrid[r][c] = 1
                    else:
                        self.newGrid[r][c] = 0
        temporaryGrid = self.grid
        self.grid = self.newGrid
        self.newGrid = temporaryGrid
        
    def clearGrid(self):
        self.grid = np.zeros((self.rows,self.cols)).reshape((self.rows,self.cols))
    
    def spawnGlider(self,r,c):
        toSpawn = [[5, 1],[6, 1],[6, 2],[5, 2],[5, 5],[4, 6],[5, 6],[6, 6],[3, 7],[7, 7],[5, 8],[2, 9],[2, 10],
                  [3, 11], [4, 12],[5, 12],[6, 12],[7, 11],[8, 10],[8, 9],[7, 17],[7, 20],[7, 21],[7, 22],[6, 22],
                  [5, 21],[6, 26],[5, 26],[1, 26],[0, 26],[1, 28],[5, 28],[2, 29],[3, 29],[4, 29],[4, 30],[3, 30],
                  [2, 30],[3, 35],[4, 35],[4, 36],[3, 36]]
        for [x,y] in toSpawn:
            self.grid[r+x,c+y] = 1
    
    def spawnReverseGlider(self,r,c):
        toSpawn = [[0, 0], [1, 0], [1, 1], [0, 1], [0, 6], [1, 6], [1, 7], [0, 7], [-1, 7], [-1, 6], [-2, 8], 
                   [-2, 10], [-3, 10],[2, 8], [2, 10], [3, 10], [3, 14], [4, 14], [4, 15], [4, 16], [2, 15], [4, 19], 
                   [4, 25], [3, 24], [2, 24], [1, 24], [0, 25],[-1, 26], [-1, 27], [5, 26], [5, 27], [2, 28], [2, 30], 
                   [2, 31], [1, 30], [3, 30], [0, 29], [4, 29], [2, 34], [2, 35], [3, 35], [3, 34]]
        for [x,y] in toSpawn:
            self.grid[r+x,c+y] = 1
    
    def spawnEaterAnd(self):
        toSpawn = [[56, 66], [57, 66], [57, 67], [57, 69], [57, 67], [55, 69], [55, 70],[56, 70], [55, 73], [56, 73], 
                   [56, 74], [55, 74], [59, 66], [59, 67], [60, 67], [60, 66], [57, 68]]
        for [x,y] in toSpawn:
            self.grid[x,y] = 1
            
    def spawnEaterOr(self):
        toSpawn = [[72, 82], [73, 82], [73, 83], [73, 84], [73, 85], [72, 86], [71, 86], [71, 85], [71, 89],
                [72, 89], [72, 90], [71, 90], [75, 82], [75, 83], [76, 83], [76, 82]]
        for [x,y] in toSpawn:
            self.grid[x,y] = 1

    def spawnEaterNot(self):
        toSpawn = [[32, 24], [32, 25], [33, 24], [33, 24], [33, 25], [32, 28], [32, 29], [33, 28],
                    [34, 29], [34, 30], [34, 31], [34, 32], [33, 32], [36, 31], [36, 32], [37, 32],
                    [37, 31]]
        for [x,y] in toSpawn:
            self.grid[x,y] = 1

    def spawnStopperOr(self):
        toSpawn = [[58, 111], [59, 111], [58, 112], [60, 112], [60, 113], [60, 114], [61, 114]]
        for [x,y] in toSpawn:
            self.grid[x,y] = 1

    def stopperAnd01(self):
        toSpawn = [[15, 28], [16, 28], [15, 29], [17, 29], [17, 30], [17, 31], [18, 31]]
        for [x,y] in toSpawn:
            self.grid[x,y] = 1
    def stopperAnd10(self):
        toSpawn = [[14, 68], [15, 68], [14, 69], [16, 69], [16, 70], [16, 71], [17, 71]]
        for [x,y] in toSpawn:
            self.grid[x,y] = 1
    def stopperAnd00(self):
        toSpawn = [[14, 68], [15, 68], [14, 69], [16, 69], [16, 70], [16, 71], [17, 71], [15, 28], [16, 28], [15, 29], [17, 29], [17, 30], [17, 31], [18, 31]]
        for [x,y] in toSpawn:
            self.grid[x,y] = 1
    def spawnStopperAnd(self):
        toSpawn = [[56, 55], [56, 56], [57, 56], [58, 55], [58, 54], [58, 53], [59, 53]]
        for [x,y] in toSpawn:
            self.grid[x,y] = 1

    def spawnStopperNot(self):
        toSpawn = [[14, 27], [15, 27], [14, 28], [16, 28], [16, 29], [16, 30], [17, 30]]
        for [x,y] in toSpawn:
            self.grid[x,y] = 1

    def spawnOr01(self):
        toSpawn = [[13, 66], [14, 66], [13, 67], [15, 67], [15, 68], [15, 69], [16, 69]]
        for [x,y] in toSpawn:
            self.grid[x,y] = 1

    def spawnOr10(self):
        toSpawn = [[13, 106], [14, 106], [13, 107], [15, 107], [15, 108], [15, 109], [16, 109]]
        for [x,y] in toSpawn:
            self.grid[x,y] = 1

    def spawnOr00(self,r,c):
        toSpawn = [[13, 66], [14, 66], [13, 67], [15, 67], [15, 68], [15, 69], [16, 69], [13, 106], [14, 106], [13, 107], [15, 107], [15, 108], [15, 109], [16, 109]]
        for [x,y] in toSpawn:
            self.grid[x,y] = 1
        
    
    def spawnNOTGate(self,prop):
        self.clearGrid()
        self.spawnGlider(1,0)
        self.spawnReverseGlider(3,40)
        self.spawnEaterNot()
        if not prop:
            self.spawnStopperNot()
    
    def spawnANDGate(self,prop1,prop2):
        self.clearGrid()
        self.spawnGlider(1,0)
        self.spawnGlider(0,40)
        self.spawnReverseGlider(3,90)
        self.spawnEaterOr()
        if not prop1 and not prop2:
            self.stopperAnd00()
            self.spawnStopperAnd()
        if not prop1 and prop2:
            self.stopperAnd01()
        if prop1 and not prop2:
            self.stopperAnd10()
            
    
            
     
    '''
    def makeGliderGun(self,x,y,orientation):
        # Requires 9 X 36 grid or 36 X 9 grid, depending on orientation
        if orientation == "NW": 
            self.grid[x+4][y] = 1
            self.grid[x+4][y+1] = 1
            self.grid[x+5][y] = 1
            self.grid[x+5][y+1] = 1
            self.grid[x+2][y+12] = 1
            self.grid[x+2][y+13] = 1
            self.grid[x+3][y+11] = 1
            self.grid[x+4][y+10] = 1
            self.grid[x+5][y+10] = 1
            self.grid[x+6][y+10] = 1
            self.grid[x+7][y+11] = 1
            self.grid[x+8][y+12] = 1
            self.grid[x+8][y+13] = 1
            self.grid[x+5][y+14] = 1
            self.grid[x+3][y+15] = 1
            self.grid[x+4][y+16] = 1
            self.grid[x+5][y+16] = 1
            self.grid[x+5][y+17] = 1
            self.grid[x+6][y+16] = 1
            self.grid[x+7][y+15] = 1
            self.grid[x+4][y+21] = 1
            self.grid[x+3][y+21] = 1
            self.grid[x+2][y+21] = 1
            self.grid[x+4][y+20] = 1
            self.grid[x+3][y+20] = 1
            self.grid[x+2][y+20] = 1
            self.grid[x+1][y+22] = 1
            self.grid[x+5][y+22] = 1
            self.grid[x+5][y+24] = 1
            self.grid[x+6][y+24] = 1
            self.grid[x+5][y+24] = 1
            self.grid[x][y+24] = 1
            self.grid[x+1][y+24] = 1
            self.grid[x+2][y+34] = 1
            self.grid[x+3][y+34] = 1
            self.grid[x+2][y+35] = 1
            self.grid[x+3][y+35] = 1
        elif orientation == "SW":
            self.grid[x][y+2] = 1
            self.grid[x][y+3] = 1
            self.grid[x+1][y+2] = 1
            self.grid[x+1][y+3] = 1
            self.grid[x+11][y] = 1
            self.grid[x+11][y+1] = 1
            self.grid[x+11][y+5] = 1
            self.grid[x+11][y+6] = 1
            self.grid[x+13][y+5] = 1
            self.grid[x+14][y+4] = 1
            self.grid[x+15][y+4] = 1
            self.grid[x+15][y+3] = 1
            self.grid[x+14][y+3] = 1
            self.grid[x+15][y+2] = 1
            self.grid[x+14][y+2] = 1
            self.grid[x+13][y+1] = 1
            self.grid[x+18][y+5] = 1
            self.grid[x+19][y+5] = 1
            self.grid[x+19][y+4] = 1
            self.grid[x+19][y+6] = 1
            self.grid[x+20][y+7] = 1
            self.grid[x+20][y+3] = 1
            self.grid[x+35][y+5] = 1
            self.grid[x+21][y+5] = 1
            self.grid[x+22][y+2] = 1
            self.grid[x+23][y+2] = 1
            self.grid[x+24][y+3] = 1
            self.grid[x+25][y+4] = 1
            self.grid[x+25][y+5] = 1
            self.grid[x+25][y+6] = 1
            self.grid[x+24][y+7] = 1
            self.grid[x+23][y+8] = 1
            self.grid[x+22][y+8] = 1
            self.grid[x+34][y+4] = 1
            self.grid[x+35][y+4] = 1
            self.grid[x+34][y+5] = 1
    
    
    def makeNOTGateWithInput(self):
        self.clearGrid()           
        self.makeGliderGun(0,40,"NW")
        self.makeGliderGun(40,40,"SW")
        
        
    def makeNOTGateWithoutInput(self):
        self.clearGrid()
        self.makeGliderGun(40,0,"SW")
'''
        