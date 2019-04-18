#!/usr/bin/env python

#===============================================================================
# - Documentation
#===============================================================================
# P. Ramdial 04/18/2019
# This Script is being used to test the different classes and their interactions

#===============================================================================
# - Imports
#===============================================================================
import random
from CaseFile import *
from Player import *
from Deck import *
from Card import *
from Weapon import *
from Room import *
from Hallway import *

#==============================================================================
# - Configurations
#==============================================================================
# Set the Seed for consistent performance
seed = 123456789
seed = 987654321 
random.seed(seed)

#===============================================================================
# - Class
#===============================================================================
        
#===============================================================================
# - Main
#===============================================================================

def main():

	# Initialize cards and deck
	card_type = ""
	value = 1
	# Initialize card information
	Rooms = ["Study", "Hall", "Lounge", "Library", "Billiard Room",
				"Dining Room", "Conservatory", "Ballroom", "Kitchen"]
	Suspects = ["Colonel Mustard", "Miss Scarlet", "Professor Plum",
				"Mr. Green", "Mrs. White", "Mrs. Peacock"]
	Weapons = ["Rope", "Lead Pipe", "Knife",
				"Wrench", "Candlestick", "Revolver"]
	Master_List = Rooms + Suspects + Weapons

	clue_deck = Deck()

	# -------------------------------------------------------------------------
	# Test Creating an ordered Deck of Cards
	for name in Master_List:
		if name in Rooms:
			card_type = "Room"
		elif name in Suspects:
			card_type = "Suspect"    
		elif name in Weapons:
			card_type = "Weapon"
		else:
			print("Error")
			exit()

		# Create a Card and add to the Deck of cards
		clue_deck.cards.append(Card(value, card_type, name))
		value += 1

	print("Initialized Deck")
	for card in clue_deck.cards:
		print(card)

	#--------------------------------------------------------------------------- 
	# Test shuffling the Cards

	clue_deck.shuffle_cards()
	print("\nShuffled Deck")
	for card in clue_deck.cards:
		print(card)

	#--------------------------------------------------------------------------- 
	# Test Distributing the Cards

	print("\n-- Distributing Cards--")

	# First distribute to the Case File list
	case_file = []
	case_file = clue_deck.distribute_cards(True, case_file)

	print("\nCase File")
	for card in case_file:
		print(card)

	# Sort Cards in Case file list as Room, Suspect, then Weapon
	case_file.sort(key=lambda x: x.value, reverse=False)

	print("\nSorted Case File")
	for card in case_file:
		print(card)

	# Fill the Case File object
	room = case_file[0]
	suspect = case_file[1]
	weapon = case_file[2]
	case_file = CaseFile(room, suspect, weapon)
	case_file_card_names = case_file.show_case_file()

	print("\nCard Names in the Case File")
	print(case_file_card_names)

	# Create Players and distribute Cards to their hands
	player_hand = []
	Homer = Player("Homer", True, 1, player_hand, True, "Dining")
	Marge = Player("Marge", True, 1, player_hand, True, "Kitchen")
	Bart = Player("Bart", True, 1, player_hand, True, "Billiard Room")
	Lisa = Player("Lisa", True, 1, player_hand, True, "Library")
	Maggie = Player("Maggie", True, 1, player_hand, True, "Conservatory")

	players = [Homer, Marge, Bart, Lisa, Maggie]
	player_hands = []
	for i in range(0,len(players)):
		player_hands.append([])

	print("\nPlayer's hand before receiving cards")
	print(player_hands)

	player_hands = clue_deck.distribute_cards(False, player_hands)

	player_hand_index = 0
	for player in players:
		player.cards = player_hands[player_hand_index]
		player_hand_index += 1

	print("\nPlayer's hand after receiving cards")
	print(Homer.cards)
	print(Marge.cards)
	print(Bart.cards)
	print(Lisa.cards)
	print(Maggie.cards)

	#---------------------------------------------------------------------------
	# Test Player Functions
	incorrect_guess = Homer.make_accusation("Mark", "Library", "Knife", case_file)
	print(incorrect_guess)

	correct_guess = Homer.make_accusation("Mrs. White", "Library", "Lead Pipe", case_file)
	print(correct_guess)

	#---------------------------------------------------------------------------
	# Test Weapon Creation and Function

	waepon_object = Weapon("Rope")
	waepon_object.displayWeapon()

	#---------------------------------------------------------------------------
	# Test Room

	room1 = Room("Lounge",True,Homer,waepon_object,True)
	print("Room 1: {}".format(room1.weapon.weaponName))

	room2 = Room("Conservatory",True,Homer,waepon_object,True)
	print("Room 2: {}".format(room2.weapon.weaponName))

	#---------------------------------------------------------------------------
	# Test Hallway

	hallway = Hallway(6,False,None,room1,room2)
	print("Hallway connects rooms: {} and {}".format(hallway.room1.roomName,
														hallway.room2.roomName))

if __name__ == "__main__":
    main()