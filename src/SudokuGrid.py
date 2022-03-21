class SudokuGrid :
    def __init__(self,grid=[]) :
        if grid :
            i = iter(grid)
            j = len(next(i))
            if j == 9 and all(len(l) == j for l in i): 
                self.grid = grid
                return
        self.grid = [[0 for i in range(9)] for j in range(9)]
        
    def show(self) :
        print('-------------------------',end='\n')
        for i in range(9) :
            for j in range(9) :
                if j==0 : 
                    print('|',end=(' '))
                print(self.grid[i][j],end=(' '))
                if j in [2,5] : 
                    print('|',end=(' '))
                if j==8 : 
                    print('|',end=('\n'))
                if ((i+1)%3==0 and j==8) : 
                    print('-------------------------',end='\n')
        
    def test(self,x,y,n) :
        for i in range(9) :
            if self.grid[i][y] == n : return False
        for i in range(9) :
            if self.grid[x][i] == n : return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(3) :
            for j in range(3) :
                if self.grid[x0+i][y0+j] == n : return False
        return True
    
    def solve(self) :
        for i in range(9) :
            for j in range(9) :
                if self.grid[i][j] == 0 :
                    for n in range(1,10) :
                        if self.test(i,j,n) :
                            self.grid[i][j] = n
                            self.solve()
                            self.grid[i][j] = 0
                    return
        self.show()
        return