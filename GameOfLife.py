class gameoflifegrid():
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.grid = []
        self.newGrid = []
        for r in range(self.rows):
            self.grid.append([])
            self.newGrid.append([])
            for c in range(self.cols):
                self.grid[r].append(0)
                self.newGrid[r].append(0)


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
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                self.grid[r][c] = 0
    
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
        
        