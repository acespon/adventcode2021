import numpy as np


with open("puzzleinput.txt") as f:
    initial_state = f.readline().split(',')
    initial_state = [int(x) for x in initial_state]
    initial_state = np.array(initial_state)
    

print(len(initial_state))

#after one day
for i in range(256):
    for fish in range(len(initial_state)):
        if initial_state[fish] == 0:
            #Reset timer and create new fish
            initial_state[fish] =6
            initial_state = np.append(initial_state,8)
        else:
            initial_state[fish] -= 1
    print(len(initial_state))
            
answer = len(initial_state)

if __name__ == "__main__":
    


    print("Day 6 - Advent of Code")
    print("Puzzle 11 answer is : %s" % answer)