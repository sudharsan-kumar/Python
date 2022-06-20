## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
from tkinter import Y

card=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def add_card(tcard):
    global card
    tcard.append(random.choice(card))
    


ans = input ('Want to play Blackjack ?')
user_card = []
computer_card = []
ans1 = 'y'
for i in range (0,2):
    user_card.append(random.choice(card))
for i in range (0,2):
    computer_card.append(random.choice(card))
while ans == 'y':
    x = 0
    print(user_card)
    print(computer_card[0])
    for user_c in user_card:
        x += int (user_c)
    print(x)
    if ans == 'y':
        if x < 21:
            add_card(user_card)
        elif x == 21:
            print('Won')
            ans1 = 'n'
        elif x > 21:
            o = 0
            for i in user_card:
                if i == 11:
                    user_card[o] = 1
                o += 1
            print (user_card)
            x = 0
            for user_c in user_card:
                x += int (user_c)
            print (f'new total:{x}')
            if x < 21:
                add_card(user_card)
                print(user_card)
            if x > 21:
                print('Lost')
                ans1 = 'n'
            elif x == 21:
                ans1 = 'n'
                print('Won')
    if ans1 == 'y':
        ans = input('Do you wanna continue?')
while ans1 != 'n': 
    print('Computer')   
    z = 0
    for computer_c in computer_card:
        z += int (computer_c)
    if z < 17:
            add_card (computer_card)
    else :
        print(computer_card)
        ans1 = 'n'
        if abs(21-x) > abs(21-z):
            print('Lost')
        elif abs(21-x) < abs(21-z):
            print('Won')
        elif abs(21-x) == abs(21-z):
            print('Draw')




        