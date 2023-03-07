import random
import art



############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## The following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###############################################################


def get_card(players_cards):
    global score
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    for length in range(1):
        players_deck = random.choice(cards)
        players_cards += [f'{players_deck}']
        score += int(players_deck)


def get_card_ai(ai_card):
    global ai_scores
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    for length in range(1):
        ai_deck = random.choice(cards)
        ai_card += [f'{ai_deck}']
        ai_scores += int(ai_deck)


    # lengths = len(ai_card)
    # number = 0
    # for num in range(lengths):
    #     ai_scores += int(ai_card[number])
    #     number += 1

def blackjack():
    continuing = True
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == 'n':
        continuing = False
    if start == 'y':
        print(art.logo_blackjack)
        #pre reqs
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        players_cards = []
        ai_card = []
        first_card = []
        global score
        score = 0
        global ai_scores
        ai_scores = 0

        for length in range(2):
            players_deck = random.choice(cards)
            players_cards += [f'{players_deck}']
            score += players_deck

        for length in range(2):
            ai_deck = random.choice(cards)
            ai_card += [f'{ai_deck}']
            ai_scores += ai_deck
            first_card = ai_card[0]

    while continuing:
        if score > 21 or ai_scores > 21:
            if '11' in players_cards:
                players_cards.remove('11')
                players_cards.append('1')
                score -= 10
            if '11' in ai_card:
                ai_card.remove('11')
                ai_card.append('1')
                ai_scores -= 10
            else:
                continuing = False
                break
        if score == 21:
            print('Blackjack!')
            continuing = False
            break
        elif ai_scores == 21:
            print('Blackjack!')
            continuing = False
            break

        print(f'    Your cards: {players_cards}, current score: {score}')
        print(f'    Computers first card: {first_card} ')

        play = input("Type 'y' to get another card, type 'n' to pass: ")

        if play == 'n':
            while ai_scores < 16:
                get_card_ai(ai_card)
            continuing = False
        if play == 'y':
            get_card(players_cards)
            if ai_scores < 16:
                get_card_ai(ai_card)

    def win():
        if score == ai_scores:
            message = 'You tied!'

        elif score > 21:
            message = 'You lost by going over.'

        elif ai_scores > 21:
            message = 'You won because they went over.'

        else:
            if score > ai_scores:
                message = 'You won by score'

            elif score < ai_scores:
                message = 'You lost by score'

        print(f'    Your final hand: {players_cards}, final score: {score}')
        print(f'    Computers final hand: {ai_card}, final score: {ai_scores}')
        print(message)
    win()
    restart = False
    go_again = input("Would you like to go again. 'y' or 'n': ")
    if go_again == 'y':
        blackjack()


blackjack()

