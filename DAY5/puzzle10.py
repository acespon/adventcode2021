
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
        

def draw_diagonal(grid,vector):
    x1,y1,x2,y2 = vector
    ystart = 0
    xstart =0
    xend=0
    yend=0
    direction = 0
    #determine left most coord
    if y1 < y2:
        ystart = y1
        xstart = x1
        xend = x2
        yend = y2
    elif y1 > y2:
        ystart = y2
        xstart = x2
        xend = x1
        yend = y1
                                            
    #determine if x goes up or down
    if xend-xstart <0:
        direction = -1
    elif xend-xstart> 0:
        direction = 1
            
    #calculate the magnitude
    magnitude = abs(x1-x2)+1
    for i in range(magnitude):
        grid[xstart+(i*direction),ystart+i] += 1

       
grid = np.zeros((1000,1000))

print(len(vents))
print(vents[0])
print(extract_vector(vents[0]))

for line in vents:
    vector = extract_vector(line)
    x1,y1,x2,y2 = vector
    if x1 == x2 or y1 == y2:
        draw_line(grid,vector)
    else:
        draw_diagonal(grid,vector)

count = 0
for iy, ix in np.ndindex(grid.shape):
    if grid[iy, ix] >= 2:
        count +=1



answer = count

if __name__ == "__main__":
    


    print("Day 5.5 - Advent of Code")
    print("Puzzle 10 answer is : %s" % answer)