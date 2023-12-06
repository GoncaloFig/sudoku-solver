def is_valid_move(grid, row, col, number):


    for x in range(9):
        if grid[row][x] == number:
            return False
        
    for x in range(9):
        if grid[x][col] == number:
            return False
        
    corner_row = row - row % 3
    corner_col = col - col % 3

    for x in range(3):
        for y in range(3):
            if grid[corner_row + x] [corner_col + y] == number:
                return False
            
    return True

def solve(grid, row, col):

    # We are in the last col but not in the last row, then continuo to the next row
    if col == 9:
        # We are in the last col and the last row, then it is solved
        if row == 8:
            return True
        row += 1
        col = 0

    # If the current slot already has a value, just go to the next col
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)
    
    # Try all possibilities
    for num in range(1, 10):
        # If it is the right number just update the value
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col + 1):
                return True
        # If we dont find a valid number make it 0   
        grid[row][col] = 0

    return False

sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve(sudoku_grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(sudoku_grid[i][j], end=" ")
        print()
    
else:
    print("No solution for this Sudoku")