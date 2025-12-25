import time

if __name__ == '__main__':
    edges = {}
    with open('inputs/day11.txt') as f:
        for line in f:
            [a, b] = line.strip().split(':')
            edges[a] = b.split()
        print(edges)
            
    def paths_to_out(node, visited):
        
        result = 0
        
        if "out" in edges[node]:
            return 1
        
        for dest in edges[node]:
            if dest not in visited:
                result += paths_to_out(dest, visited + [node])
        
        return result
    
    # this takes a long time
    def dac_and_fft(node, visited, dac=False, fft=False):
        
        result = 0
        
        if ("out" in edges[node]):
            if dac and fft:
                print("Found one!")
                return 1
            else:
                return 0
        
        if node == 'dac':
            dac = True
            
        if node == 'fft':
            fft = True
        
        for dest in edges[node]:
            if dest not in visited:
                result += dac_and_fft(dest, visited + [node], dac, fft)
        
        return result
        
        
    
    # print(paths_to_out("you", []))
    print(dac_and_fft("svr", []))
    
    

    