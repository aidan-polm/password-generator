import random

def deal(hand):
    drawn_card = random.choice(range(1, 11))
    hand.append(drawn_card)
    
def evaluate(user_score, dealer_score):
    if dealer_score < user_score <= 21:
        print(f"Your score: {user_score}\nDealer score: {dealer_score}\nYou win!")
    elif user_score < dealer_score <= 21:
        print(f"Your score: {user_score}\nDealer score: {dealer_score}\nYou lost :(")
    elif user_score > 21:
        print(f"You bust")

def game():
    user_cards = []
    dealer_cards = []
    
    for _ in range(2):
        deal(user_cards)
        deal(dealer_cards)
    
    print(f"Your cards are: {user_cards} ({sum(user_cards)})")
    print(f"The dealer has: {dealer_cards[0]}")
    
    while sum(user_cards) < 21:
        hit = input("Would you like to hit? y or n. ")
    
        if hit == 'y':
            deal(user_cards)
            print(f'Your cards: {user_cards} ({sum(user_cards)})\nDealer has: {dealer_cards[0]}')
        elif hit == 'n':
            while sum(dealer_cards) < 17:
                deal(dealer_cards)
            break
    
    user_score = sum(user_cards)
    dealer_score = sum(dealer_cards)
    
    evaluate(user_score, dealer_score)

start = input("Are you ready to start a game of blackjack? y or n. ")

if start == 'y':
    game()
else:
    print("Okay. We'll just chill.")