# intervals time
import time

def isOverlap(a: list[int], b: list[int]):
    if a[0] > b[0]:
        return isOverlap(b, a)
    
    if a[1] < b[0]:
        return False
    
    return True

def merge(a: list[int], b: list[int]):
    a[0] = min(a[0], b[0])
    a[1] = max(a[1], b[1])
    return a
    
# not really needed since python can use a key
def list_compare(a: list[int], b: list[int]):    
    return a[0] < b[0]    

# count fresh if in any range
def part_1(intervals, ids):
    
    result = 0
    
    for n in ids:
        for interval in intervals:
            # if it's the range, count and go to the next id
            if interval[0] <= n <= interval[1]:
                result += 1
                break            
    
    print("Fresh ingredient ids:", result)

# merge the intervals and calculate the differences
# intervals is sorted
def part_2(intervals):
    merged = []
    merged.append(intervals[0])
    N = len(intervals)
    
    for i in range(1, N):
        a = merged[-1]  # get last merged interval
        b = intervals[i]
        if isOverlap(a, b):
            # combine if possible
            merged[-1] = merge(a, b)
        else:
            merged.append(b)
    
    result = 0
    for interval in merged:
        result += interval[1] - interval[0] + 1
    print("Total Fresh Ingredient IDs:", result)
    
    return merged

if __name__ == '__main__':
    
    start = time.time()
    
    intervals = []
    ids = []
    
    with open("inputs/day5.txt") as f:
        interval = True
        
        for line in f:
            if line == '\n':
                interval = False
                continue
        
            if interval:
                intervals.append([int(n) for n in line.strip().split('-')])
        
            else:
                ids.append(int(line.strip()))
            
        # inputs are very long but it shouldn't be a problem
        intervals.sort(key=lambda iv: iv[0])
            
        # part 1 can use the merged intervals 
        merged = part_2(intervals)
        part_1(merged, ids)
        
        # ideally we can merge then solve both parts but i don't want to rewrite this anymore
        
    end = time.time()
    
    # .002 secs! on my system
    print("Time:", f"{end - start:.4f}", "secs")  