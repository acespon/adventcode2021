import numpy as np

with open("puzzleinput.txt") as f:
    crabs = f.readline()
    crabs = crabs.split(',')
    crabs = [int(x) for x in crabs]

def fuel_cost(array,position):
    cost = 0
    for num in array:
        cost += abs(num-position)
    
    return cost
    
#initialise the cost   
smallest_cost= fuel_cost(crabs,0)
for num in range(max(crabs)):
    if fuel_cost(crabs,num) < smallest_cost:
        smallest_cost = fuel_cost(crabs,num) 
        

answer = smallest_cost

if __name__ == "__main__":
    print("Day 7 - Advent of Code")
    print("Puzzle 13 answer is : %s" % answer)