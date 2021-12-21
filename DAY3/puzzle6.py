
from scipy import stats
import numpy as np


def oxygen(report):
    values =[]
    temp = []
    
    for diagnostic in report:
        binary=[]
        #each diagnostic is a string of 1s and 0s
        for char in diagnostic:
            binary.append(char)
        values.append(binary)
        
    print()
    print(len(values))
    
    print(values[0][0]== '0')
    
    print()
    
    
    for i in range(len(values[0])-1):
        print("index %s" % i)
        bin = []
        count0 = 0
        count1 = 0
        for line in values:
            if line[i] == '0':
                count0 +=1
            else:
                count1 +=1
            bin.append(line[i])
                
        
        print("zeros: %s" % count0)
        print("ones: %s" % count1)
        mode = ''
        if count0 > count1:
            mode = '0'
        else: 
            mode = '1'
        print(mode)
        
        temp = []
        if len(values) == 1:
            break
        else:
            for line in values:
                if line[i] == mode:
                    temp.append(line)
            values = temp
                    
        print(len(bin))
        print("len of values: %s" % len(values))
        

                
                
                
    
    print(len(values))
    
    last = ''.join(values[0])
    
    print(last)
    last = int(last,2)
    
    print(last)
    return last


def co2(report):
    values =[]
    temp = []
    
    for diagnostic in report:
        binary=[]
        #each diagnostic is a string of 1s and 0s
        for char in diagnostic:
            binary.append(char)
        values.append(binary)
        
    print()
    print(len(values))
    
    print(values[0][0]== '0')
    
    print()
    
    
    for i in range(len(values[0])-1):
        print("index %s" % i)
        bin = []
        count0 = 0
        count1 = 0
        for line in values:
            if line[i] == '0':
                count0 +=1
            else:
                count1 +=1
            bin.append(line[i])
                
        
        print("zeros: %s" % count0)
        print("ones: %s" % count1)
        mode = ''
        least= ''
        if count0 <= count1:
            mode = '0'
            least= '1'
        else: 
            mode = '1'
            least = '0'
        print(mode)
        
        temp = []
        temp2 = []
        if len(values) == 1:
            break
        else:
            for line in values:
                if line[i] == mode:
                    temp.append(line)
            values = temp
                    
        print(len(bin))
        print("len of values: %s" % len(values))
        

                
                
                
    
    print(len(values))
    
    last = ''.join(values[0])
    
    print(last)
    last = int(last,2)
    
    print(last)
    return last




if __name__ == "__main__":
    with open("puzzleinput.txt") as f:
        diagnostics = f.readlines()
   
    print("Day 3.5 - Advent of Code")
    print("Puzzle 6 oxygen is : " + str(oxygen(diagnostics)))
    print("Puzzle 6 co2 is : " + str(co2(diagnostics)))
    print("Puzzle 6 Answer is : " + str(oxygen(diagnostics)*co2(diagnostics)))