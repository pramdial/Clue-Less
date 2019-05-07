#!/usr/bin/env python

#===============================================================================
# - Documentation
#===============================================================================
# P. Lin 04/17/2019
# P. Ramdial - Modified to take Card Objects 04/18/2019

# NOTE:
#   1. player_turn type boolean instead of Player
#   2. current_location type string instead of int
#   3. make_suggestion() returns a list of strings

# class: Player
# attributes: player_name(string), active(boolean), turn_count(int), cards(List<Card>),
#               player_turn(boolean), current_location(string)
# function: make_accusation(CaseFile), make_suggestion()

class Player:
    def __init__(self, player_name, player_token, active, turn_count, cards, player_turn, start_location):
        self.playerName = player_name
        self.playerToken = player_token
        self.active = active
        self.turnCount = turn_count
        self.cards = cards
        self.playerTurn = player_turn
        self.startLocation = start_location

    def __repr__(self):
        return("User Name: {},\n\tCharacter: {},\n\tStart Location: {},\n\tTurn Count: {}".format(self.playerName, self.playerToken, self.startLocation, self.turnCount))
    
    def show_hand(self):
        # Show the cards in the players hand
        print("\n")
        print(self.playerName)
        for card in self.cards:
            print(card)

    def make_accusation(self, suspect, room, weapon, casefile):
        if suspect.lower() == casefile.suspect.name.lower() and \
                room.lower() == casefile.room.name.lower() and \
                weapon.lower() == casefile.weapon.name.lower():
            return True
        else:
            return False

    def make_suggestion(self, suspect, room, weapon):
        print("{}'s suggestion: Suspect: {}, Room: {}, Weapon {}".format(self.playerName, suspect, room, weapon))
        # return [suspect.lower(), room.lower(), weapon.lower()]

    def select_card_to_reveal(self, other_player_cards):
        card_index = 1
        selected_card = 0
        valid_choice = False
        print("\n")
        print(self.playerName + ": Select one of the following cards")
        while valid_choice == False:
            for card in other_player_cards:
                print("{} for {}".format(card_index, card.name))
                card_index += 1
            selected_card = int(input("Input option Here: "))
            if (selected_card > 0) and (selected_card <= len(other_player_cards)):
                valid_choice = True
        return(other_player_cards[selected_card-1])
    
    def prove_suggestion_false(self, selected_token, token_location, selected_weapon):
        # Check to see if there are matching cards in the hand
        matching_cards = []
        for card in self.cards:
            if card.name == selected_token:
                matching_cards.append(card)
            if card.name == token_location:
                matching_cards.append(card)
            if card.name == selected_weapon:
                matching_cards.append(card)
                
        return(matching_cards)
