import numpy as np

with open("puzzleinput.txt") as f:
    initial_state = f.readline().split(',')
    initial_state = [int(x) for x in initial_state]
    initial_state = np.array(initial_state)
    
'''
This was such a fun problem!
Think, there are 9 possible stages of life a lanternfish could exist in
(Timer values from 0-8)
So, count the number of lanternfish at each stage.
After each day:
    -How many fish are about to spawn? (Record this)
    -Move each group of fish into the next stage (Easy way to do this is to pop() 
    the first element in the list which shifts each value's index to the left)
    -Then append the number of fish you just popped (the 'spawned' fish).
    -The number of fish that popped also corresponds to the number of 'spawning'
    fish, so add that to the number of fish with a timer of 6 
    
'''
snapshot = np.zeros(9)

for num in initial_state:
    snapshot[num] += 1

print(snapshot)

for day in range(256):
    numSpawning = snapshot[0]
    snapshot = np.delete(snapshot,0)
    snapshot = np.append(snapshot,numSpawning)
    snapshot[6] += numSpawning
    
print(snapshot)
    
answer = int(sum(snapshot))

if __name__ == "__main__":
    print("Day 6.5 - Advent of Code")
    print("Puzzle 12 answer is : %s" % answer)