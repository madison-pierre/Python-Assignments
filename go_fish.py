# Dr Michaels
# go_fish.py
# 4/21/21
# This file contains information on a card and deck class.
# Together we will build a player class
# Then begin designing rules for a game

# Global variables used to create a new deck
face = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suit = ["Clubs", "Diamonds", "Hearts", "Spades"]

import random

def insertionSort(my_array): 
    for i in range(1, len(my_array)): 
        key = my_array[i] 
        j = i-1
        while j >= 0 and key < my_array[j] : 
                my_array[j + 1] = my_array[j] 
                j -= 1
        my_array[j + 1] = key 
        res = ""
        for k in range(0,i+1):
            res += "%s " % my_array[k]

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
            
    def get_counter(self):
        return self.counter

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
   
   
   
   
class GF_Player:

    # The go fish player has three attributes
    # hand = current hand composed of card objects
    # points = the number of 4 card matches (4 cards of the same face) that the player has
    def __init__(self):
        self.hand = []
        self.points = 0
        
    def reset(self):
        self.hand = []
        self.points = 0
        
    def hand_size(self):
        return len(self.hand)
        
    def add_card(self, card):
        if isinstance(card, Card):
            self.hand.append(card)
            
    def remove_card(self,card):
        if isinstance(card, Card):
            self.hand.remove(card)
            
    def check_match(self):
        # This should scan through the cards and determine if any player has 4 matches
        # HINT - Consider the poker code we looked at for the four of a kind
        # HINT - A player cannot have a match currently if they do not have at least 4 cards
        matches=[]
        if(self.hand_size() >= 4):
            insertionSort(self.hand)
            matches=self.check_four_match() #Helper method
            if len(matches) > 0:
                self.points=self.points+1
        return matches
            
        
    def check_four_match(self):
        n=1
        while n+2 < self.hand_size():
            if self.hand[n-1].get_face() == self.hand[n+2].get_face():
                return [self.hand[n-1],self.hand[n],self.hand[n+1],self.hand[n+2]]
            n+=1
        return []
        
    def get_points(self):
        return self.points
        
    def search(self, face):
        result = []
        print("\n CHECKING %s" %self)
        print("For a face of %s" %face)
        for card in self.hand:
            current_face = card.get_face()
            found_face = (card.get_face() == face)
            if(found_face): 
                print("\n Found a card! It's the %s" % card)
                result.append(card)
        if len(result)!=0:
            for item in result:
                print("\n I'll be taking that...")
                self.remove_card(item) #Had to do the remove seperately otherwise length of hand gets messed up
        return result

    def get_most_occuring_face(self,last_face_requested): #method for the computer to determine most important cards to ask for
        insertionSort(self.hand)
        print("\n It won't ask for %s" % last_face_requested)
        n=1
        counter=0
        two_cards=False
        index_of_two_cards=0
        three_cards=False
        index_of_three_cards=0
        faces_in_deck=[]
        for card in self.hand:
            faces_in_deck.append(card.get_face())
        while n < self.hand_size():
            if((faces_in_deck[n] == faces_in_deck[n-1]) and counter == 1):
                three_cards = True
                index_of_three_cards=n
            elif(faces_in_deck[n] == faces_in_deck[n-1]):
               two_cards = True
               index_of_two_cards=n
               counter+=1
            n+=1
        if(three_cards and (faces_in_deck[index_of_three_cards] != last_face_requested)):
            return faces_in_deck[index_of_three_cards]
        elif(two_cards and (faces_in_deck[index_of_two_cards] != last_face_requested)):
            return faces_in_deck[index_of_two_cards]
        elif(last_face_requested == faces_in_deck[n-1]):
            return faces_in_deck[0]
        else:
            return faces_in_deck[n-1]

        while n < self.hand_size():
            last_face=self.hand[n-1].get_face()
            this_face=self.hand[n].get_face()
            if(this_face==last_face):
                pairs+=1
            two_pairs =(pairs==2)
            one_pair = (pairs==1)
            if(two_pairs):
                return self.hand[n].get_face()
            elif(one_pair):
                return self.hand[n].get_face()
            else:
                pairs=0
            if(n == self.hand_size()-1):
                return self.hand[0].get_face()
            n+=1
        
    def __str__(self):
        if len(self.hand) > 0:
            result = "%s" % self.hand[0]
            for i in range(1, len(self.hand)):
                result += ", %s" % self.hand[i]
            result += ", Points: %s" % self.points
            return result
        elif self.points > 0:
            return "The player has no cards but has the following point total: %s" % self.points
        else:
            return "This player has not played yet"
        
        


class GF_Game:

    def __init__(self):
        self.player = GF_Player()
        self.computer = GF_Player()
        self.comp_last = None # We can use this data point to represent the last card the computer played
        self.deck = Deck()
    
    def start_game(self):
        self.player.reset()
        self.computer.reset()
        self.deck.shuffle()
        for i in range(7):
            self.player.add_card(self.deck.deal())
            self.computer.add_card(self.deck.deal())
        
    def play_game(self):
        # The First thing we will do is start/reset the game state
        # We will play the game until either the computer or human has 0 cards
        self.start_game()
        turn = "human"
        while (self.player.hand_size() > 0) and (self.computer.hand_size() > 0):
            # Loop will continue until either player has no cards in hand
            if (turn == "human"):
                print("\n Here is the current human data:\n%s" %self.player)
                face_wanted = input("\n Please enter a face value you contain to search the computer hand: ")
                result=self.computer.search(int(face_wanted)) #Making sure face_wanted was an int was something that messed me up for a long time
                if len(result)==0:
                    print("\n Go fish...")
                    card_from_deck=self.deck.deal()
                    self.player.add_card(card_from_deck)
                    print("\n Player dealt %s" % card_from_deck)
                else:
                    for card in result:
                        self.player.add_card(card)
                matching_cards=self.player.check_match()        
                if(len(matching_cards)!=0):
                    print("\n PLAYER HAS FOUR OF A KIND!")
                    print("Player earned a point.")
                    for card in matching_cards:
                        self.player.remove_card(card)
                turn = "computer"
            else:
                print("\n Here is the current Computer hand: %s" % self.computer)
                self.computer_move()
                turn = "human"
                
                
        if (self.player.get_points() > self.computer.get_points()):
            print("\n\nTHE HUMAN HAS WON!")
        elif (self.player.get_points() < self.computer.get_points()):
            print("\n\nTHE COMPUTER HAS WON!")
        else:
            print("\n\nTHE GAME IS A TIE!")
        
            
        
    def computer_move(self):
        #COMPUTER CAN'T ASK FOR THE SAME CARD TWICE
        most_occuring_face=self.computer.get_most_occuring_face(self.comp_last)
        self.comp_last = most_occuring_face
        #Look and see which face we have the most of
        #If we have alot of different faces it asks for the first card in the hand
        print("\n The computer asks: You got any %s 's?" % most_occuring_face)
        result= self.player.search(most_occuring_face)
        #search works!
        if(len(result)==0):
            print("\n Computer has to go fish...")
            card_from_deck=self.deck.deal()
            self.computer.add_card(card_from_deck)
            print("\n Computer dealt %s" % card_from_deck)
        else:
            for card in result:
                self.computer.add_card(card)
        matching_cards=self.computer.check_match()        
        if(len(matching_cards)!=0):
            print("\n COMPUTER MADE A MATCH!")
            print("Computer earned a point")
            for card in matching_cards:
                self.computer.remove_card(card)
        
        
        
    

    
    def __str__(self):
        return "The current game state:\n\nPLAYER ONE\n%s\n\nPLAYER TWO\n%s" % (self.player, self.computer)



def main():
    print("This code will launch a game and begin its cycle of play!")
    my_game = GF_Game()
    my_game.play_game()
main()
