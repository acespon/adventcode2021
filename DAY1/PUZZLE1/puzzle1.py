#DAY 1

def depth_increases(measurements):
    count = 0
    currentMeasurement = 0

    for measurement in measurements:
        measurement = int(measurement)
        if measurement > currentMeasurement:
            count += 1
        currentMeasurement = measurement

    count -= 1
    return count

if __name__ == "__main__":
    with open('puzzleinput.txt') as f:
        readings = f.readlines()
        
    print("Day 1 - Advent of Code")
    print("The number of times a depth measurement increases is: " +         str(depth_increases(readings)))
