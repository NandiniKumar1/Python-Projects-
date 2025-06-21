# This program is playing blackjack with two players.
import random # This lets us use random functions 

#Here we start the function to run the card program
def main():
    # Create a deck of cards
    deck = create_deck()
     # Get the number of cards to deal
    num_cards = int(input('How many cards should I deal? '))
    cards = list(deck.keys())  # Get the list of card names only
    random.shuffle(cards)  # Shuffle the cards??
    # Deal the cards.
    deal_cards(deck, num_cards) # Uses the values inputted from the user above 

# The create_deck function returns a dictionary
# representing a deck of cards

def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.
    return deck


 # Keep playing until you get 4 cards, because 2 per player needed 
    while len(cards) >= 4:
        player1_hand = []  # Player 1's first hand
        player2_hand = []  # Player 2's first hand

        # Give 2 cards to each player
        player1_hand.append(cards.pop()) # Gives player 1 a card
        player1_hand.append(cards.pop()) # Gives player 1 a second card

        player2_hand.append(cards.pop()) # Gives player 2 a card
        player2_hand.append(cards.pop()) # Gives player 2 a second card

        # Calculate the score for both players
        player1_score = calculate_score(player1_hand, deck)
        player2_score = calculate_score(player2_hand, deck)

        # Player 1 keeps drawing if under 17
        while player1_score < 17 and len(cards) > 0:
            player1_hand.append(cards.pop())
            player1_score = calculate_score(player1_hand, deck)# Cannot pick more than 17 or will go overboard 
        # Player 2 keeps drawing if under 17
        while player2_score < 17 and len(cards) > 0:
            player2_hand.append(cards.pop())
            player2_score = calculate_score(player2_hand, deck)# Cannot pick more than 17 or will go overboard

# Deals a number of cards and adds up their values
def deal_cards(deck, number):
    hand_value = 0  # Start with 0 points

    # If the number is bigger than how many cards we have, fix it
    if number > len(deck):
        number = len(deck)

    # Pick random cards and add their values
    for i in range(number):
        card = random.choice(list(deck))  # Pick a card
        print(card)  # Show the card
        hand_value += deck[card]  # Add the card’s value

    print("Total value of these cards:", hand_value)  # Show final value  

 # Show hands and scores
        print("\nPlayer 1's hand:", player1_hand)
        print("Player 1's score:", player1_score)
        print("Player 2's hand:", player2_hand)
        print("Player 2's score:", player2_score)

        # Decide who wins
        if player1_score > 21 and player2_score > 21:
            print("Both players loose. No winner.")
        elif player1_score > 21:
            print("Player 1 loses. Player 2 wins!")
        elif player2_score > 21:
            print("Player 2 lose. Player 1 wins!")
        elif player1_score > player2_score:
            print("Player 1 wins!")
        elif player2_score > player1_score:
            print("Player 2 wins!")
        else:
            print("It's a tie!")

    # Tell user game is done
    print("\nNo more cards left. Game over.")
