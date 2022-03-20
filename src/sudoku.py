def show_grid() :
    global grid
    print('-------------------------',end='\n')
    for i in range(9) :
        for j in range(9) :
            if j==0 : 
                print('|',end=(' '))
            print(grid[i][j],end=(' '))
            if j in [2,5] : 
                print('|',end=(' '))
            if j==8 : 
                print('|',end=('\n'))
            if ((i+1)%3==0 and j==8) : 
                print('-------------------------',end='\n')

def test(x,y,n) :
    global grid
    for i in range(9) :
        if grid[i][y] == n : return False
    for i in range(9) :
        if grid[x][i] == n : return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3) :
        for j in range(3) :
            if grid[x0+i][y0+j] == n : return False
    return True

def solve() :
    global grid
    for i in range(9) :
        for j in range(9) :
            if grid[i][j] == 0 :
                for n in range(1,10) :
                    if test(i,j,n) :
                        grid[i][j] = n
                        solve()
                        grid[i][j] = 0
                return
    show_grid()


grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
show_grid()
solve()
