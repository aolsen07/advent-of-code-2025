# battery joltage
# 2 pointers
import time

def largest_possible_joltage(bank):
    
    # 2 pointers and joltage formula
    i = 0
    j = 1
    result = bank[0] * 10 + bank[1]
    
    # order matters
    for i in range(len(bank) - 1):
        for j in range(i + 1, len(bank)):
            result = max((bank[i] * 10) + bank[j], result)
            
    return result

# backtracking
def activate_batteries(bank, choose):
    
    if choose == 0: 
        return []
    
    # have to select the rest of the elements
    if len(bank) == choose:
        return bank
    
    return max([bank[0]] + activate_batteries(bank=bank[1:], choose=choose-1), activate_batteries(bank=bank[1:], choose=choose))
    int(''.join(map(str, bank[:len(bank)])))
    
    

if __name__ == "__main__":
    start_time = time.time()
    
    result = 0
    p2_result = 0
    with open('inputs/day3.txt', 'r') as f:
        for line in f:
            bank = [int(c) for c in line.strip()]

            result += largest_possible_joltage(bank=bank)
            p2_result += int(''.join(map(str, activate_batteries(bank=bank, choose=12))))
            
    
    final_time = time.time()
            
    print("Total output joltage:", result) 
    print("New total joltage:", p2_result)
    
    print("Time:", f"{final_time - start_time:.4f}", "secs")  