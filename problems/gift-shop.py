# day 2
import time
    
def check_invalid_id(curr_id: str, divisions: int):
    
    if len(curr_id) % divisions:
        return False
    
    l = len(curr_id) // divisions 
    prefix = curr_id[:l]
    for i in range(1, divisions):
        # compare to prefix
        if curr_id[(l * i):(l*(i+1))] != prefix:
            return False
    return True
          
if __name__ == "__main__":   
    
    start_time = time.time()
    part1_result = 0
    part2_result = 0
    
    with open("inputs/day2.txt", "r") as f:
        ranges = f.readline().split(',')
        
        for r in ranges:
            [a, b] = r.split('-')
            [a, b] = [int(a), int(b)]

            for n in range(a, b + 1):               
                curr = str(n)
                
                is_repetitive = False
                if check_invalid_id(curr, 2):
                    part1_result += int(curr)
                    is_repetitive = True
                    
                else: 
                    for l in range(2, len(curr) + 1):
                        if check_invalid_id(curr, l):
                            is_repetitive = True
                            break
                     
                if is_repetitive:        
                    part2_result += int(curr)
                        
    final_time = time.time()                
                    
    print("Part 1:", part1_result)
    print("Part 2:", part2_result)
    print("Time:", f"{final_time - start_time:.4f}", "secs")