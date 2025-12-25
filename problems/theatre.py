import time

def calculate_area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

if __name__ == '__main__':
    
    # print(calculate_area((7,1), (11,7)) == 35)
    # print(calculate_area((7,3), (2,3)) == 6)
    # print(calculate_area((2,3), (7,3)) == 6)
    
    tiles = []
    max_area = 0
    
    with open("inputs/day8.txt") as f:
        for line in f:
            tiles.append([int(n) for n in line.strip().split(',')])
            
    # part 1, slow
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            max_area = max(max_area, calculate_area(tiles[i], tiles[j]))
        
    print(max_area)