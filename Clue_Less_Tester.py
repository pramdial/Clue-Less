#!/usr/bin/env python

#===============================================================================
# - Documentation
#===============================================================================
# P. Ramdial 04/20/2019
# This Script is being used to test the different classes and their interactions in the game logic
# debugger values Test:	- 1: boardTest()
#						- 2: playerNames(), playerNames()
#                       - 3: deck(), hand(), 
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
from Board import *

def boardTest(board):
	# Check to see if the board is correct
	print("\n -- Board --")
	for cell in board.locations:
		if cell.location_type == "Room":
			print("Location: {},\n\t Links: {},\n\t Weapon: {},\n\t Players: {}".format(cell.name, cell.links, cell.weapon, cell.players))
		else:
			print("Location: {},\n\t Links: {},\n\t Players: {}".format(cell.name, cell.links, cell.players))
	print("\n")
	
def playerNames(player_names):
	# Check to see if the player names were created
	print("\n -- User Names --")
	for player_name in player_names:
		print(player_name)
	print("\n")
	exit()

def playerNames(players):
	# Check Player Classes
	print("\n -- Player Objects --")
	for player in players:
		print(player)
	print("\n")

def deck(deck):
	# Print Cards in Decks
	print("\n -- Cards in Deck --")
	for card in deck.cards:
		print(card)
		print("\n")

def hand(hand):
	# Print Cards in the hands
	print("\n -- Cards in Hand --")
	for card in hand:
		print(card)
		print("\n")

turn_count = 0
def turn_tester(ending_number):
	global turn_count
	turn_count += 1
	if turn_count > ending_number:
		print("Ending loop")
		exit()


