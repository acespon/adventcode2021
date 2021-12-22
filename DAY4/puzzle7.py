import numpy as np

with open("puzzleinput.txt") as f:
    bingo_cards = f.readlines()


def create_card(raw):
    square =''.join(raw)
    vector =[]
    for char in range(0,len(square)-2,3):
        vector.append(int(square[char:char+2]))
    
    card = np.reshape(vector,(5,5))
    
    return card
    
    
def bingo(card):
    for row in range(5):
        for column in range(5):
            if sum(card[row,:]) == 0:
                return True
            elif sum(card[:,column]) == 0:
                return True
    
    
    return False    


drawnNumbers = bingo_cards[0][0:-1].split(',')
drawnNumbers = list(map(int,drawnNumbers))

print(drawnNumbers)

smallest_count = 100
current_card = 0
winning_card =[]
winning_card_num=0
bingo_number = 0

for line in range(2,len(bingo_cards),6):
    current_card += 1
    
    card = create_card(bingo_cards[line:line+5])
    print(card)
    print()
    
    count = 0
    for num in drawnNumbers:
        count +=1
        for row in range(5):
            for column in range(5):
                if card[row,column] == num:
                    card[row,column] = 0
        if count > smallest_count:
            break
        if count < smallest_count and bingo(card) :
            bingo_number = num
            winning_card = card
            winning_card_num = current_card
            smallest_count = count
            break
    
            
    print(card)
    print("numbers taken: %s "% count)
    print("smallest count: %s " % smallest_count)
    print()
    print()
    
                
        
    
print("Winning Card: %s" % winning_card_num)
print(winning_card)
print("Number that called bingo first: %s" % bingo_number)
print(sum(sum(winning_card)))

print(bingo_number * sum(sum(winning_card)))
    

if __name__ == "__main__":

    print("Day 4 - Advent of Code")
    print("Puzzle 7 answer is : ")