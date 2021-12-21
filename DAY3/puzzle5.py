from scipy import stats
import numpy as np


def power_consumption(report):
    values =[]
    
    for diagnostic in report:
        binary=[]
        #each diagnostic is a string of 1s and 0s
        for char in diagnostic:
            binary.append(char)
        values.append(binary)
        
    gamma= ''.join(stats.mode(values)[0][0].tolist()[0:-1])
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)
    print(gamma)
    print(epsilon)
    print("gamma: %s" % int(gamma,2))
    print("epsilon: %s" % int(epsilon,2))
    return int(gamma,2) * int(epsilon,2)




if __name__ == "__main__":
    with open("puzzleinput.txt") as f:
        diagnostics = f.readlines()
   
    print("Day 3 - Advent of Code")
    print("Puzzle 5 answer is : " + str(power_consumption(diagnostics)))