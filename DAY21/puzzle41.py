import numpy as np

with open("puzzleinput.txt") as f:
    input = f.readlines()

positions = [int(line.split(" ")[-1]) for line in input]

print(positions)


dice = 1

def roll_dice():
    spaces = (dice*3) + 3
    dice += 2
    
    return spaces
    
roll_dice()
print(dice)
    



answer = 42

if __name__ == "__main__":
    print("Day 21 - Advent of Code")
    print("Puzzle 41 answer is : %s" % answer)