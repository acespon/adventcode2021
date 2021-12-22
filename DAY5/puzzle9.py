import numpy as np


with open("puzzleinput.txt") as f:
    vents = f.readlines()
    
def extract_vector(line):
    temp = line.split(' -> ')
    start = temp[0].split(',')
    end = temp[1].split(',')
    
    x1= start[0]
    y1= start[1]
    x2= end[0]
    y2= end[1]
    
    vector = [x1,y1,x2,y2]
    
    vector = [int(i) for i in vector]
    
    return vector
    
def draw_line(grid,vector):
    x1,y1,x2,y2 = vector
    if x1 == x2: #if the x coords are the same (vertical line)
        magnitude = abs(y1 - y2)+1
        minimum = min(y1,y2)
        for i in range(magnitude):
            grid[x1,minimum+i] += 1
    elif y1 == y2: #if the y coords are the same (horizontal line)
        magnitude = abs(x1 - x2)+1
        minimum = min(x1,x2)
        for i in range(magnitude):
            grid[minimum+i,y1] += 1
    else:
        
        
    
grid = np.zeros((1000,1000))

print(len(vents))
print(vents[0])
print(extract_vector(vents[0]))

for line in vents:
    vector = extract_vector(line)
    print(vector)
    draw_line(grid,vector)

count = 0
for iy, ix in np.ndindex(grid.shape):
    if grid[iy, ix] >= 2:
        count +=1



answer = count

if __name__ == "__main__":
    


    print("Day 5 - Advent of Code")
    print("Puzzle 9 answer is : %s" % answer)