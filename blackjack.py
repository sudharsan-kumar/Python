import random

def dealcards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(uscore,cscore):
    if uscore > 21 and cscore > 21:
        return "You and computer are both over 21. You lose."
    if uscore == cscore:
        return "Draw"
    elif cscore == 0:
        return 'Computer won.'
    elif uscore == 0:
        return 'You won'
    elif uscore > 21:
        return 'You are over 21. You Lost '
    elif cscore > 21:
        return "Computer is over 21.You win "
    elif uscore > cscore:
        return "You win "
    else:
        return "You lose "
def maingame():
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(dealcards())
        computer_cards.append(dealcards())
    

    while not game_over:
        print(f"Your hand: {user_cards}")
        print(f"Computer's open card: {computer_cards[0]}")
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if deal == "y":
                user_cards.append(dealcards())
            else:
                game_over = True 
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(dealcards())
        computer_score = calculate_score(computer_cards)              
    
    print(f"Your hand: {user_cards}, score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play Blackjack? Type 'y' or 'n': ") == "y":

  maingame()