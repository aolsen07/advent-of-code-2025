import time
import copy

EMPTY = '.'
ROLL = '@'


def count_adjacent(board, row, col):
    adj = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[0]):
            if board[r][c] == ROLL:  # Or whatever condition you're checking
                adj += 1
    return adj
                
if __name__ == "__main__":
    board = []
    total_removed = 0
    count = 0
    
    def print_board(board):
        for line in board:
            print(''.join(line))
            
    start_time = time.time()
    
    with open('inputs/day4.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                # create board out of input file
                board.append([c for c in line])
    
    p1 = True
    print_board(board)
    
    # Part 1
    while True:
        new_board = copy.deepcopy(board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                # count rolls with fewer than 4 adjacent rolls 
                if board[i][j] == ROLL and count_adjacent(board=board, row=i, col=j) < 4:
                    new_board[i][j] = EMPTY
                    count += 1
        
        if p1: 
            print("Part 1 count:", count)
            p1 = False
            
        if count == 0:
            break
        
        total_removed += count
        count = 0
        board = new_board
        
    print(total_removed)
    print_board(board)
    final_time = time.time()
    print(final_time - start_time)