def navigate(instructions,initx,inity):
    x = initx
    y = inity
    
    
    for instruction in instructions:
        #each instruction simplified 2d vector with a direction and magnitude.
        components = instruction.split()
        #At this point I would have used a switch statement but python doesnt have that till 3.10...
        direction = components[0]
        magnitude = int(components[1])
        
        if direction == 'forward':
            x += magnitude
        elif direction == 'down':
            y -= magnitude
        elif direction == 'up':
            y += magnitude        
    
    print("x: %d" % x )
    print("y: %d" % y )
    
    product = x * y
    
    return abs(product)
    

if __name__ == "__main__":
    with open("puzzleinput.txt") as f:
        instructions = f.readlines()
   
    print("Day 2 - Advent of Code")
    print("Puzzle 3 answer is : " + str(navigate(instructions,0,0)))