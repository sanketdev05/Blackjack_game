import random 

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []
total = []
should_continue = True

def next_card():
    if len(player_cards) == 0 and len(dealer_cards) == 0:
        print(logo)
        for i in range(1,3):
            x = random.choice(cards)
            y = random.choice(cards)
            player_cards.append(x)
            dealer_cards.append(y)
        return player_cards, dealer_cards
    else:
        x = random.choice(cards)
        y = random.choice(cards)
        player_cards.append(x)
        dealer_cards.append(y)
        return player_cards, dealer_cards

def determine_ace():
    index = 0
    for element in player_cards:
        if element == 11:
            if total[0] > 11:
                player_cards[index] = 1
        index += 1

def cards_calc():
    determine_ace()
    sum_of_playercards = 0
    sum_of_dealercards = 0
    for x,y in zip(player_cards, dealer_cards):
        sum_of_playercards += x
        sum_of_dealercards += y
    return sum_of_playercards, sum_of_dealercards

total = cards_calc()

def decide():
    if total[1]<17:
        one_card = random.choice(cards)
        dealer_cards.append(one_card)
    
    if total[0]>total[1] or total[0] == 20:
        print("You win") 
    elif total[0] == total[1]:
        print("Draw")
    elif total[0]<total[1] or total[0] == 20 :
        print("You lose")

def wentover():
    print(f"Your cards: {player_cards}, Current score = {total[0]}\nComputer's first card: {dealer_cards[0]}")
    print(f"Your final hand: {player_cards}, Final score = {total[0]}\nComputer's final card: {dealer_cards}, Final score = {total[1]}")

    print(f"You went over. You lose")
    

while should_continue:
    response = input("Type 'y' to get another card. type 'n' to pass: ")

    if response == 'y':
        next_card()
        cards_calc()
        total = cards_calc()
        # determine_ace()
        if total[0]>21 or total[1]>21:
            wentover()       
            should_continue = False
        else:
            print(f"Your cards: {player_cards}, Current score = {total[0]}\nComputer's first card: {dealer_cards[0]}")
    else:
        should_continue = False
        print(f"Your final hand: {player_cards}, Final score = {total[0]}\nComputer's final card: {dealer_cards}, Final score = {total[1]}")
        decide()
        
