#Manufacture the puzzle grid
def form_grid():
    global grid
    print('The Sudoku Solver Problem')
    for _ in range(9):
        row = input().split()
        temp = [int(block)for block in row]
        grid.append(temp)
    printGrid()
    
#print the grid
#It is used to display the initial puzzle before solving and the final solution after solving.
def printGrid():
    global grid
    for row in grid:
        print(row)
        
#fucntion to check that if block is placed on the given block..
def possible(row,col,digit):
    global grid
    for i in range(0,9):
        if grid[row][i] == digit:
            return False
    for i in range(0,9):
        if grid[i][col] == digit:
            return False
    square_row = (row//3)*3
    square_col = (col//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[square_row+i][square_col+j] == digit:
                return False    
    return True

def solve():
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for digit in range(1,10):
                    if possible(row,col,digit):
                        grid[row][col] = digit
                        solve()
                        grid[row][col] = 0  #Backtrack step
                return
    print('\nThe Solution\n')
    printGrid()
    

grid = []
form_grid()
solve()

# Examples Values For User Input
# 0 0 4 3 0 0 2 0 9
# 0 0 5 0 0 9 0 0 1
# 0 7 0 0 6 0 0 4 3
# 0 0 6 0 0 2 0 8 7
# 1 9 0 0 0 7 4 0 0
# 0 5 0 0 8 3 0 0 0
# 6 0 0 0 0 0 1 0 5
# 0 0 3 5 0 8 6 9 0
# 0 4 2 9 1 0 3 0 0
#------------------------#
# 3 0 6 5 0 8 4 0 0
# 5 2 0 0 0 0 0 0 0
# 0 8 7 0 0 0 0 3 1
# 0 0 3 0 1 0 0 8 0
# 9 0 0 8 6 3 0 0 5
# 0 5 0 0 9 0 6 0 0
# 1 3 0 0 0 0 2 5 0
# 0 0 0 0 0 0 0 7 4
# 0 0 5 2 0 6 3 0 0