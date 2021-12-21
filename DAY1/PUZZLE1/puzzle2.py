
def sliding_window_increases(measurements):
    count = 0
    
    for i in range(0, len(measurements)-3):     
        window = sum(measurements[i:i+3])
        nextWindow = sum(measurements[i+1:i+4])
        
        if nextWindow > window:
            count += 1
    
    return count



if __name__ == "__main__":
    with open("puzzleinput.txt") as f:
        readings = f.readlines()
        
    measurements = [int(reading) for reading in readings]
        
    print("Day 1.5 - Advent of Code")
    print("The number of three measurement sums bigger than the previous are: " + str(sliding_window_increases(measurements)))