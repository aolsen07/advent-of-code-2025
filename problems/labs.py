from copy import deepcopy

START = 'S'
EMPTY = '.'
BEAM = '|'
SPLITTER = '^'
    
# part 1
def count_splits(grid):
    splits = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            cell = grid[i][j]

            # skip empty spaces
            if cell == EMPTY:
                continue

            # make sure we don't index out of bounds when looking at row below
            if i + 1 >= len(grid):
                continue

            below = grid[i+1]

            # start beam
            if cell == START:
                below[j] = BEAM
                continue

            # split beam
            if cell == BEAM and below[j] == SPLITTER:
                if j - 1 >= 0:
                    below[j-1] = BEAM
                if j + 1 < len(below):
                    below[j+1] = BEAM
                splits += 1
                continue

            # let beam travel
            if cell == BEAM and below[j] == EMPTY:
                below[j] = BEAM
                continue

            # other cells: no-op
            pass
    
    print("Total Splits:", splits)
    
# part 2
def count_timelines(grid, start_row=0):
    pass
    
if __name__ == '__main__':
    
    grid = []
    with open('inputs/day7.txt') as f:
        for line in f:
            # split into characters
            grid.append(list(line.strip()))
            
    count_splits(deepcopy(grid))
    print(count_timelines(deepcopy(grid)))
    