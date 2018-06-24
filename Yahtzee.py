#Nitya Pillai
#January 12 2018
#Yahtzee
#Project



import random

print ("Welcome to yahtzee!Let's play!")

turns=0
dice1=random.randint(1, 6)
dice2=random.randint(1, 6)
dice3=random.randint(1, 6)
dice4=random.randint(1, 6)
dice5=random.randint(1, 6)
 
n =5;
while n > 0 :  
    dices=[dice1, dice2, dice3, dice4, dice5]
    foundValue=0
    
    one_counter = dices.count(1)
    two_counter = dices.count(2)
    three_counter = dices.count(3)
    four_counter = dices.count(4)
    five_counter = dices.count(5)
    six_counter = dices.count(6)
    
    maxvalue= max( one_counter, two_counter, three_counter, four_counter, five_counter, six_counter)
    n=5-maxvalue

    if one_counter == maxvalue:
        foundValue = 1
    if two_counter==maxvalue:
        foundValue=2    
    if three_counter==maxvalue:
        foundValue=3
    if four_counter==maxvalue:
        foundValue=4
    if five_counter==maxvalue:
        foundValue=5
    if two_counter==maxvalue:
        foundValue=2   
    
    print(dices)
    
    if dice1==foundValue:
        dices.remove(dice1)
    if dice2==foundValue:
        dices.remove(dice2)
    if dice3==foundValue:
        dices.remove(dice3)
    if dice4==foundValue:
        dices.remove(dice4)
    if dice5==foundValue:
        dices.remove(dice5)
    turns+=1
   
    if dice1!=foundValue:
        dice1=random.randint(1, 6)
        dices=[dice1, dice2, dice3, dice4, dice5]
    if dice2!=foundValue:
        dice2=random.randint(1, 6)
        dices=[dice1, dice2, dice3, dice4, dice5]
    if dice3!=foundValue:
        dice3=random.randint(1, 6)
        dices=[dice1, dice2, dice3, dice4, dice5]
    if dice4!=foundValue:
        dice4=random.randint(1, 6)
        dices=[dice1, dice2, dice3, dice4, dice5]
    if dice5!=foundValue:
        dice5=random.randint(1, 6)
        dices=[dice1, dice2, dice3, dice4, dice5]
        
print ("Turns: ", turns)
        
print("Congratulations! You win!")          
        

        
        
            
