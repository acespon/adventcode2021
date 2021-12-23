import numpy as np

with open("puzzleinput.txt") as f:
    lines = f.readlines()
    vector = ''.join(lines)
    grid=[]
    for num in vector:
        if num.isdigit():
            grid.append(int(num))
    grid = np.array(grid)
    grid = np.reshape(grid,(100,100))
        

print(len(grid))

copy = np.zeros((100,100))

def compare(point,n,s,e,w):
    for p in [n,s,e,w]:
        if point >= p:
            return False
    return True

def check_point(x,y,grid):
    n,s,e,w = 100,100,100,100

    north = (x-1,y)
    south = (x+1,y)
    east = (x,y+1)
    west = (x,y-1)
    
    if x-1 >= 0:
        n= grid[north]
    if x+1 <= len(grid)-1:
        s= grid[south]
    if y+1 <= len(grid)-1:
        e= grid[east]
    if y-1 >= 0:
        w= grid[west]
    
    point= grid[x,y]
    
    if compare(point,n,s,e,w):
        copy[x,y] = point +1
    else:
        pass
        


for x in range(len(grid)):
    for y in range(len(grid)):
        pass
        check_point(x,y,grid)    
    
    
    
    

answer = int(sum(sum(copy)))

if __name__ == "__main__":
    print("Day 9 - Advent of Code")
    print("Puzzle 17 answer is : %s" % answer)