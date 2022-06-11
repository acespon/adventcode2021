import numpy as np

with open("puzzleinput.txt") as f:
    input = f.readlines()

#positions = [int(line.split(" ")[-1]) for line in input]
positions = [4,8]
score1 = 0
score2 = 0
numrolls =0

dice = 0

def move(position,spaces):
    while spaces >0:
        spaces -= 1
        position += 1
        if position == 10:
            position =1
    
    return position
    
def roll_dice(dice):
    if dice == 99:
        roll1= 100
        roll2 = 1
        roll3 = 2
    else:
        roll1 = dice +1
        roll2 = dice +2
        roll3 = dice +3
    
    
    return [roll1,roll2,roll3]


while (score1 < 1000 and score2 < 1000):
    #player 1 rolls dice
    p1roll = roll_dice(dice)
    spaces = sum(p1roll)
    dice = p1roll[2]
    positions[0] = move(positions[0],spaces)
    score1+= positions[0]
    
    #player 1 rolls dice
    p2roll = roll_dice(dice)
    spaces = sum(p2roll)
    dice = p2roll[2]
    positions[1] = move(positions[1],spaces)
    score2+= positions[1]
    
    print(score1)
    print(score2)
            
    numrolls+= 6
    print(numrolls)







answer = 42

if __name__ == "__main__":
    print("Day 21 - Advent of Code")
    print("Puzzle 41 answer is : %s" % answer)