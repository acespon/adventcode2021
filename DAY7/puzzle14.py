
import numpy as np

with open("puzzleinput.txt") as f:
    crabs = f.readline()
    crabs = crabs.split(',')
    crabs = [int(x) for x in crabs]

def fuel_cost(array,position):
    cost = 0
    for num in array:
        steps = abs(num-position)
        S = steps*(1+steps)/2 #sum of n terms (steps) in an arithmetic sequence e.g. 1+2+3+4+5+...+steps-1+steps
        cost += S
    
    return cost

#initialise the cost   
smallest_cost= fuel_cost(crabs,0)

for num in range(max(crabs)):
    if fuel_cost(crabs,num) < smallest_cost:
        smallest_cost = fuel_cost(crabs,num) 
        

answer = int(smallest_cost)

if __name__ == "__main__":
    print("Day 7.5 - Advent of Code")
    print("Puzzle 14 answer is : %s" % answer)