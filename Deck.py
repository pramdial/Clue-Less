#!/usr/bin/env python

#==============================================================================
# - Documentation
#==============================================================================
# - P. Ramdial 04/16/19

#==============================================================================
# - Imports
#==============================================================================
import random
from CaseFile import *

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
        # Shuffle the cards in the deck
        for i in range(0, len(self.cards)):
            random_position = random.randint(0, len(self.cards)-1)
            temporary_card = self.cards[i]
            self.cards[i] = self.cards[random_position]
            self.cards[random_position] = temporary_card

    def distribute_cards_case_file(self):
        # Create and distribute the cards to the case file
        card_holder = []
        has_room = False
        room_card = None
        has_suspect = False
        suspect_card = None
        has_weapon = False
        weapon_card = None
        for card in self.cards:
            if (card.card_type == "Room") and (has_room == False):
                card_holder.append(card)
                room_card = card
                has_room = True
            if (card.card_type == "Suspect") and (has_suspect == False):
                card_holder.append(card)
                suspect_card = card
                has_suspect = True
            if (card.card_type == "Weapon") and (has_weapon == False):
                card_holder.append(card)
                weapon_card = card
                has_weapon = True

        for held_card in card_holder:  # Remove cards from deck that are in the case file
            for card in self.cards:
                if held_card is card:
                    self.cards.remove(card)
                    break
                else:
                    continue
        return(CaseFile(room_card, suspect_card, weapon_card))
      
    def distribute_cards_players(self, card_holder):
        # Distribute the cards to each players hand
        holder_row = 0
        for card in self.cards:
            if holder_row >= len(card_holder):
                holder_row = 0

            card_holder[holder_row].append(card)
            holder_row += 1

        return(card_holder)
