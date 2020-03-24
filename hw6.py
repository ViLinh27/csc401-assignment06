#hw6 collaborator: Vi-Anh Nguyen
import random
#5.38
def collatz(x):
    #condition for positive integers only
    #output has to be a sequence until it hits 1
    if x > 0:
        print(x)
        #make a loop to output collatz sequence:
        #make sequence stop when output=1
        while x!=1:
            #make conditions for even numbers
            if x%2==0:
                x= x /2
            #make conditions for odd numbers
            else:
                x=3*x+1
            print(int(x))
            
#5.42
def primeFac(pnum):
    pfac=[]     
    div=2
    while pnum != 1:
        if pnum%div==0:
            pfac.append(div)
            pnum=pnum//div
        else:
            div+=1
    return pfac
             
#5.48
def sublist(list1,list2):
    lo=[]
    for i in list1:
        #this loop checks everything in list1
        if i in list2:
            #this checks if we can find elements of list1 in list2
            #check order of matched up elements
            lo.append(list2.index(i))
            #check if indices in lo ascend
    while lo[-1]>lo[-2]:
        return True
    return False

    
#6.22-----make dictionary
def mirror(s):
    #make mirror image of inputed string(reverse)
    #invalid if there is an e in the string
    '''sample output:
    >>>mirror('vow')
    'wov'
    >>>mirror('bed')
    'INVALID'
    '''
    if 'e' not in s:
        for i in s:
            ml={'d':'b','p':'q'}
            #ml2={'d':'b','q':'p'}
            for j in ml:
                if i==j:
                    return s.replace(i,ml[j])[::-1]
        return s[::-1]
    else:
        return 'INVALID'
    
#6.30---
#reference: https://pynative.com/python-random-choice/
def rps(p1,p2):
    p1=p1.upper()
    p2=p2.upper()
    if p1=='R':
        if p2=='R':
            return(0)
            
        elif p2=='P':
            return(1)
        else:
            return(-1)
    if p1=='P':
        if p2=='R':
            return(-1)
        elif p2=='P':
            return(0)
        else:
            return(1)
    if p1=='S':
        if p2=='R':
            return(1)
        elif p2=='P':
            return(-1)
        else:
            return(0)
        
def simul(n):
    #prints round of games of Rock,paper,scissors between p1 and p2
    #outputs palyer who wins the most rounds wins the n-round game, ties possible
    #function should print result of game as shown:
    '''sample output:
    >>>simul(1)
    Player1
    >>>simul(1)
    Tie
    >>>simul(100)
    Player2
    '''
    #0- means tie
    #1-means p2 won
    #-1 means p1 won
    pc=['R','P','S']
    #random.choice(pc)---picks random item from pc list
    tw=0
    p1w=0
    p2w=0
    i=0
    
    while i <=n:
        p1c=random.choice(pc)
        p2c=random.choice(pc)
        rps(p1c,p2c)
        i+=1
        #print(p1w,p2w,tw)

    #compare the wins
    if p1w>p2w and p1w>tw:
        print('Player 1')
    elif p2w>p1w and p2w>tw:
        print('Player 2')
    else:
        print('Tie')
    
#6.31--------------------------------------------
    '''Craps is a dice-based game played in many casinos. Like blackjack, a player plays against the
house. The game starts with the player throwing a pair of standard, six-sided dice. If the player
rolls a total of 7 or 11, the player wins. If the player rolls a total of 2, 3, or 12, the player
loses. For all other roll values, the player will repeatedly roll the pair of dice until either she
rolls the initial value again (in which case she wins) or 7 (in which case she loses)
(a) Implement function craps() that takes no argument, simulates one game of craps, and returns
1 if the player won and 0 if the player lost.
>>>craps()
0
>>>craps()
1
>>> craps()
1'''
def craps():
    #start with player throwing two side dice
    #if player rolls total of 7 or 11, player wins-ouput 1
    #if player rolls total of 2,3 or 12, player loses-output 0
    #any other total:repeat roll until 1-initial value rolled(output 1) OR 2-roll a 7(output 0)
    pr1=random.randrange(1,7)
    pr2=random.randrange(1,7)
    pt=pr1+pr2
    if pt==7 or pt==11:
        return 1
    elif pt==2 or pt==3 or pt==12:
        return 0
    else:
        while pt!=7:
            pr1_s=random.randrange(1,7)
            pr2_s=random.randrange(1,7)
            pt2=pr1_s+pr2_s
            if pt2==pt:
                return 1
        return 0    
    
'''
(b)Implement function testCraps() that takes a positive integer n as input, simulates n games of
craps, and returns the fraction of games the player won.
>>> testCraps(10000)
0.4844
>>> testCraps(10000)
0.492
'''
def testCraps(n):
    #returns #games player won/#games played total
    gc=0
    gw=0
    while gc<=n:
        gc+=1
        craps()
        return gw/gc

#doctest

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw6TEST.py'))
