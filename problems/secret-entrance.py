import time 

class Dial:
    def __init__(self):
        # dial starts pointing at 50
        self.pos = 1000000000 + 50
        self.N = 100
        self.ends_at_zero = 0
        self.points_to_zero = 0
        
    def turn(self, rotation: str):
        direction = rotation[0]
        points = int(rotation[1:])
        
        # trim down full rotations
        while points > 0:
            curr = min(points, 100)
            if curr == 100:
                points -= 100
                self.points_to_zero += 1
                continue
            
            # negative direction
            if direction == 'L':
                for i in range(curr):
                    self.pos -= 1
                    if self.pos % self.N == 0:
                        self.points_to_zero += 1
                    
            # positive direction
            else:
                for i in range(curr): 
                    self.pos += 1
                    if self.pos % self.N == 0:
                        self.points_to_zero += 1
            
            points -= curr
        
        if self.pos % self.N == 0:
            self.ends_at_zero += 1
        
if __name__ == "__main__":
    start_time = time.time()
    result = 0
    dial = Dial()
    with open('inputs/day1.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                dial.turn(line)
    final_time = time.time()
            
    print("Points at Zero:", dial.ends_at_zero) # 1182
    print("Total points at zero:", dial.points_to_zero)
    print("Time:", f"{final_time - start_time:.4f}", "secs")    