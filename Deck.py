#!/usr/bin/env python

#==============================================================================
# - Documentation
#==============================================================================
# - P. Ramdial 04/16/19

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

#==============================================================================
# - Class
#============================================================================== 
class Deck(object):
    '''
    This is the Deck Class which is composed of Cards
    Attributes:
        - cards: List of Cards
    Behaviors:
        - shuffle_cards(): Shuffles the cards in the deck.
        - distribute_cards(): Fills the card_holder list with cards.
    '''
    def __init__(self):
        self.cards = []
    
    def shuffle_cards(self):
        for i in range(0, len(self.cards)):
            random_position = random.randint(0, len(self.cards)-1)
            temporary_card = self.cards[i]
            self.cards[i] = self.cards[random_position]
            self.cards[random_position] = temporary_card
      
    def distribute_cards(self, is_case_file, card_holder):
        # print(card_holder)
        if is_case_file:  # If True, fill the holder with one of each Card type
            for card in self.cards:
                matching_type = False
                for held_card in card_holder:
                    if card.card_type == held_card.card_type:
                        # print("Card Type in holder")
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

        elif not is_case_file:  # Fill all Player's hands
            holder_row = 0
            for card in self.cards:
                if holder_row >= len(card_holder):
                    holder_row = 0       
                card_holder[holder_row].append(card)
                holder_row += 1

        else:
            print("Error")

        # print(card_holder)
        return(card_holder)