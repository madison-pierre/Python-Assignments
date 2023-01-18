# Dr Michaels
# blackjack_game.py
# 4/14/21
# This file contains information on a card and deck class.
# Together we will build a player class
# Then begin designing rules for a game

# Global variables used to create a new deck
face = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suit = ["Clubs", "Diamonds", "Hearts", "Spades"]

import random

class Card:
    # Constructor method for Card.
    # Takes as input a face and suit value. 
    # If they are not found in the global variables above, the card will be set to a 2 of clubs
    def __init__(self, the_face, the_suit):
        global face, suit
        if (the_face in face and the_suit in suit):
            self.face = the_face
            self.suit = the_suit
        else:
            #print("Illegal card value, creating a 2 of Clubs")
            self.face = -1
            self.suit = "ILLEGAL CARD"

    # Retuns the suit value of the calling card
    def get_suit(self):
        return self.suit

    # Returns the face value of the calling card
    def get_face(self):
        return self.face

    # Compares the face and suit attributes of other_card to those possessed by the calling card
    def __eq__(self, other_card):
        return (self.face == other_card.get_face()) and (self.suit == other_card.get_suit())

    # Returns the value of self > other_card
    # The first comparison is on face value. If the faces are different, we return the result of
    # self.face > other_card.get_face()
    # If they are tied, we return the result of self.suit > other_card.get_suit()
    def __gt__(self, other_card):
        if self.face > other_card.get_face():
            return True
        elif (self.face == other_card.get_face()):
            return self.suit > other_card.get_suit()
        else:
            return False

    # Card tostring. Will return the card in the format "Face of Suit"
    def __str__(self):
        return "%s of %s" % (self.face, self.suit)
		
		
class Deck:
	
    # The constructor method for the Deck.
    # It takes no parameters.
    # It fills a deck with 52 unique card, and then uses random.shuffle to randomly order the deck
    # The counter will be used to indicate which card is at the "top" of the deck
    # i.e. all cards above counter will have been dealt
    def __init__(self):
        self.deck = []
        self.counter = 0
        global face
        global suit
        for the_face in face:
            for the_suit in suit:
                self.deck.append(Card(the_face, the_suit))
        for i in range(7):
            random.shuffle(self.deck)

    # Returns the top card of the deck if it exists (if we have not previously dealt 52 cards)
    # We could add in a method to automatically shuffle the deck if we reach this point
    def deal(self):
        if self.counter < 52:
            result = self.deck[self.counter]
            self.counter += 1
            return result

    # Randomly shuffles the deck array seven times.
    def shuffle(self):
        self.counter = 0
        for i in range(7):
            random.shuffle(self.deck)

    # tostring method for deck class.
    # Prints out all 52 cards in the deck, one per line.
    # We indicate with an X cards that have been dealt
    # << Current Top Card indicates which card is the current top of the deck.
    def __str__(self):
        result = ""
        for i in range(52):
            if i == self.counter:
                result += "%s << Current Top Card\n" % self.deck[i]
            elif i < self.counter:
                result += "%s X\n" % self.deck[i]
            else:
                result += "%s\n" % self.deck[i]
        return result

class Blackjack_Player:
    
    def __init__(self):
        self.hand = []

    def get_score(self):
        score=0
        for card in self.hand:
            value = card.get_face()
            if(value >=2 and value <=10):
                score= score+value
            elif(value >=11 and value <=13):
                score= score+10
            elif(value > 13):
                aceChoice = input("ACE FOUND: Should Ace be 1 or 11?")
                print("You may be asked this question again. Keep your answer the same.")
                if(aceChoice == "1"):
                    score = score+1
                else:
                    score= score+11
        return score
    

    def first_card(self):
        if(len(self.hand) > 0):
            return self.hand[0]
        else:
            return "Game not started"
    
    def add_card(self, card):
        self.hand.append(card)
     
    def get_hand(self):
        return self.hand

     
    def __str__(self):
        if(len(self.hand) == 0):
            return "No cards in hand"
        else:
            result = ""
            for i in range(0, len(self.hand)):
                score = self.get_score()
                result += " %s " % self.hand[i]
                result += "\n MY SCORE: %s" % score
            return result
    
    
class Blackjack_Game:
    
    def __init__(self):
        self.player = Blackjack_Player()
        self.dealer = Blackjack_Player()
        self.Deck = Deck()
      
    def play_game(self):
        print("Starting a new game!")
        game_done = False
        while (not game_done):
            print("This is your current hand: ")
            print("%s" % self.player)
            print("This is what you see of the dealer: %s" % self.dealer.first_card())
            val = input("Do you want to get another card? (Y/N)")
            if(val == "Y" or val == "y"):
                print("Dealing card to player")
                card = self.Deck.deal()
                print("Player dealt %s" % card)
                self.player.add_card(card)
                currentPlayerScore = self.player.get_score()
                print("Dealer will now draw...")
                self.dealerLogic()
                currentDealerScore = self.dealer.get_score()
                print("DEALER SCORE IS NOW: %s" % currentDealerScore )
                if(currentPlayerScore > 21):
                    game_done = True
                    print("PLAYER WENT BUST")
                if(currentDealerScore > 21):
                    game_done = True
                    print("DEALER WENT BUST")
            else:
                print("No more cards, time to stop playing.")
                game_done = True

        
        playerScore = self.player.get_score()
        dealerScore = self.dealer.get_score()
        winner="No One"
        if(playerScore > 21):
            winner="Dealer"
        elif(dealerScore > 21):
            winner="Player"
        else:
            if(playerScore > dealerScore):
                winner="Player"
            elif(dealerScore > playerScore):
                winner="Dealer"
            else:
                winner="Dealer"
        print("%s has won!" % winner)
        print("GAME OVER")
        return winner

    def dealerLogic(self):
        dealerScore = self.dealer.get_score()
        if(dealerScore <= 17):
            card = self.Deck.deal()
            self.dealer.add_card(card)
        

       
    def __str__(self):
        return "Nothing to see here!"

def gameplayLoop(rounds):
    playerWins=0
    dealerWins=0
    while rounds > 0:
        new_game = Blackjack_Game()
        win = new_game.play_game()
        if(win == "Player"):
            playerWins += 1
        else:
            dealerWins +=1
        rounds=rounds-1
        print("Dealer Wins: %s" % dealerWins)
        print("Player Wins: %s" % playerWins)



def main():
    print("This will be our blackjack simulator!")
    my_game = Blackjack_Game()
    #print("Let us test the game!")
    #my_game.play_game()
    print("We will test our gameplay loop")
    gameplayLoop(3)
    
	
	
	
main()
