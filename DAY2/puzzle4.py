
def steer(instructions,initx,inity):
    x = initx
    y = inity
    aim = 0
    
    
    for instruction in instructions:
        #This time the first part of each line is a command instead of a specific direction.
        components = instruction.split()
        command = components[0]
        magnitude = int(components[1])
        
        if command == 'forward':
            x += magnitude
            y += aim * magnitude
        elif command == 'down':
            aim += magnitude
        elif command == 'up':
            aim -= magnitude        
    
    print("x: %d" % x )
    print("y: %d" % y )
    
    product = x * y
    
    return abs(product)
    

if __name__ == "__main__":
    with open("puzzleinput.txt") as f:
        instructions = f.readlines()
   
    print("Day 2.5 - Advent of Code")
    print("Puzzle 4 answer is : " + str(steer(instructions,0,0)))