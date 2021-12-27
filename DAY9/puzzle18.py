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
    grid = np.pad(grid,1,constant_values=(100))
        

input = '21999432103987894921985678989287678967899899965678'

print(input)
vector = []

for num in input:
    vector.append(int(num))

vector = np.array(vector)
print(vector)
test = np.reshape(vector,(5,10))
print()

for x in range(5):
    for y in range(10):
        if test[x,y] == 9:
            test[x,y] = 0
        else: 
            test[x,y] =1
    
print()
padded = np.pad(test,1,constant_values=(0))
print(padded)
    
def check_point(grid):
    current_label = 0
    relationships = []
    for i in range(50):
        relationships.append([i])
    for x in range (1,len(grid[:,0])-1):
        for y in range(1,len(grid[0,:])-1):
            if grid[x,y] == 1:
                north = grid[x-1,y] if grid[x-1,y] != 0 else 0
                west = grid[x,y-1] if grid[x,y-1] != 0 else 0
                if north == 0 and west == 0:
                    current_label += 1                
                    grid[x,y] = current_label
                elif north != 0 and west !=0:
                    print(north,west)
                    relationships[north].append(west)
                    relationships[west].append(north)
                    grid[x,y] = min(north,west,current_label)
                else:
                    grid[x,y] = current_label
      
    for p in range (1,len(grid[:,0])-1):
        for q in range(1,len(grid[0,:])-1):
            label = grid[p,q]   
            grid[p,q] = min(relationships[label])          
    for p in range (1,len(grid[:,0])-1):
        for q in range(1,len(grid[0,:])-1):
            label = grid[p,q]   
            grid[p,q] = min(relationships[label])  
    for p in range (1,len(grid[:,0])-1):
        for q in range(1,len(grid[0,:])-1):
            label = grid[p,q]   
            grid[p,q] = min(relationships[label])  


check_point(padded)
print()
print(padded)



    
    
        
    


