#!/usr/bin/env python


#==============================================================================
# - Documentation
#==============================================================================
# - Created 20190416

#==============================================================================
# - Imports
#==============================================================================
import random

#==============================================================================
# - Configurations
#==============================================================================
# Set the Seed for consistent performance
seed = 123456789
seed = 987654321 
random.seed(seed)

# Initialize card information
Rooms = ["Study", "Hall", "Lounge", "Library", "Billiard Room",
         "Dining Room", "Conservatory", "Ballroom", "Kitchen"]
Suspects = ["Colonel Mustard", "Miss Scarlet", "Professor Plum",
            "Mr. Green", "Mrs. White", "Mrs. Peacock"]
Weapons = ["Rope", "Lead Pipe", "Knife", "Wrench", "Candlestick", "Revolver"]

Master_List = Rooms + Suspects + Weapons

# Place holders for lists
case_file = [] 
players = [[],[],[]]

#==============================================================================
# - Classes
#==============================================================================
class Card(object):
    '''
    This is the Generic Card Class
    Attributes:
        - value:     int  - To be taken out
        - card_type: String
        - name:      String
    Behaviors:  Do we actually need these?
        - set_type()
        - get_type()
    '''
    def __init__(self, value, card_type, name):
        self.value = value
        self.card_type = self.set_type(card_type)  # card_type
        self.name = name
        
    def set_type(self, card_type):
        if card_type == "Room":
            return("Room")
        elif card_type == "Suspect":
            return("Suspect")
        elif card_type == "Weapon":
            return("Weapon")
        else:
            print("Error")

    def get_type(self):
        return(self.card_type)
    
    
class Deck(object):
    '''
    This is the Deck Class which is composed of Cards
    Attributes:
        - cards: List of Cards
    Behaviors:
        - shuffle_cards()
        - distribute_cards()
    '''
    
    def __init__(self):
        self.cards = []
    
    def shuffle_cards(self):
        '''
        Shuffle the cards in the deck.
        '''
        for i in range(0, len(self.cards)):
            random_position = random.randint(0, len(self.cards)-1)
            temporary_card = self.cards[i]
            self.cards[i] = self.cards[random_position]
            self.cards[random_position] = temporary_card
      
            
    def distribute_cards(self, is_case_file, card_holder):
        '''
        Fills the card_holder list with cards.
        '''
        if is_case_file:
            for card in self.cards:
                matching_type = False
                for held_card in card_holder:
                    if card.card_type == held_card.card_type:
                        print("Card Type in holder")
                        matching_type = True
                        break
                    else:
                        continue
                if matching_type == False:
                    card_holder.append(card)
                else:
                    matching_type = False
            for held_card in card_holder:
                 self.cards.remove(held_card)
        elif not is_case_file:
            holder_index = 0
            for card in self.cards:
                if holder_index >= len(card_holder):
                    holder_index = 0

                card_holder[holder_index].append(card)
                holder_index += 1
        else:
            print("Error")

        return(card_holder)
            
        
            
        
#==============================================================================
# - Main Driver
#==============================================================================

def main(case_file, players):
    
    # Initialize deck and variables
    deck = Deck()
    card_type = ""
    value = 1
    
    # Create an ordered Deck of Cards
    for item in Master_List:
        if item in Rooms:
            card_type = "Room"
        elif item in Suspects:
            card_type = "Suspect"    
        elif item in Weapons:
            card_type = "Weapon"
        else:
            print("Error")
            exit()
        
        deck.cards.append(Card(value, card_type, item))
        value += 1
    
    print("Initialized Deck")
    for card in deck.cards:
        print("Number: {}, Type: {}, Name: {}".format(card.value, card.card_type, card.name))

    #---------------------------------------------------------------------------
    # Shuffle the Cards

    deck.shuffle_cards()
    print("\nShuffled Deck")
    for card in deck.cards:
         print("Number: {}, Type: {}, Name: {}".format(card.value, card.card_type, card.name))
       
    #---------------------------------------------------------------------------
    # Distribute the Cards
    print("\n-- Distributing Cards--")
    # case_file = [] 
    case_file = deck.distribute_cards(True, case_file)
    print("\nCase File")
    for card in case_file:
         print("Number: {}, Type: {}, Name: {}".format(card.value, card.card_type, card.name))

    # players = [[],[]]
    players = deck.distribute_cards(False, players)
    index = 0
    print("\nPlayer Hands")
    for player in players:
        print("Player: {}".format(index))
        index += 1
        for card in player:
             print("Number: {}, Type: {}, Name: {}".format(card.value, card.card_type, card.name))
        
if __name__ == "__main__":
    main(case_file, players)
