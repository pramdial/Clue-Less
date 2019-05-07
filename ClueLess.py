#!/usr/bin/env python

#===============================================================================
# - Imports
#===============================================================================
import random
from CaseFile import *
from Player import *
from Deck import *
from Card import *
from Weapon import *
# from Room import *
# from Hallway import *
from Board import *
import time
import Clue_Less_Tester
from operator import attrgetter

#==============================================================================
# - Configurations
#==============================================================================
# Set the Seed for consistent performance
seed = 123456789
seed = 987654321 
random.seed(seed)

debugger = 4  # Calls different Tests with different values. See Clue_Less_Tester Documentation.
ending_number = 100

# Make Sure input() is 2.x or 3.x compliant
try:
    input = raw_input
except NameError:
    pass

# Initialize card information
Rooms = ["Study", "Hall", "Lounge", "Library", "Billiard Room",
            "Dining Room", "Conservatory", "Ballroom", "Kitchen"]
Suspects = ["Colonel Mustard", "Miss Scarlet", "Professor Plum",
            "Mr. Green", "Mrs. White", "Mrs. Peacock"]
Weapons = ["Rope", "Lead Pipe", "Knife",
            "Wrench", "Candlestick", "Revolver"]
Master_List = Rooms + Suspects + Weapons

Hallways = [1,2,3,4,5,6,7,8,9,10,11,12]

# Locations
Study = "Study"
Hallway1 = "Study - Hall"
Hall = "Hall"
Hallway2 = "Hall - Lounge"
Lounge = "Lounge"
Hallway3 = "Study - Library"
Hallway4 = "Hall - Billiard Room"
Hallway5 = "Lounge - Dining Room"
Library = "Library"
Hallway6 = "Library - Billiard Room"
Billiard_Room = "Billiard Room"
Hallway7 = "Billiard Room - Dining Room"
Dining_Room = "Dining Room"
Hallway8 = "Library - Conservatory"
Hallway9 = "Billiard Room - Ballroom"
Hallway10 = "Dining Room - Kitchen"
Conservatory = "Conservatory"
Hallway11 = "Conservatory - Ballroom"
Ballroom = "Ballroom"
Hallway12 = "Ballroom - Kitchen"
Kitchen = "Kitchen"

#==============================================================================
# - Gameplay Functions
#==============================================================================
#-----------------------------------------------------------------------------
# - Time Stamp
#-----------------------------------------------------------------------------
def time_string_formatter(curr_time):
    # Convert the Time to a readable format
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
    return(formatted_time)

#-----------------------------------------------------------------------------
# - Initializing Game Functions
#-----------------------------------------------------------------------------
def get_player(i):
    # Prompt users to enter a name
    player = ''
    while player == '':  # Ensure a name is placed in the input
        player = input('Player ' + str(i) + ' - Enter your user name: ')

    return(player)

def copy_suspects(Suspects):
    # Copy the Suspect list for modifying
    copy = []
    for suspect in Suspects:
        copy.append(suspect)

    return(copy)

def choose_token(player, suspects):
    # Player chooses a character
    player_choice = 0
    valid_choice = False
    print("\n")
    print(player + ", Choose the Character you wish to play as")
    # print available options
    for suspect in suspects:
        if suspect == "Colonel Mustard":
            print("1 for Colonel Mustard")
        if suspect == "Miss Scarlet":
            print("2 for Miss Scarlet")
        if suspect == "Professor Plum":
            print("3 for Professor Plum")
        if suspect == "Mr. Green":
            print("4 for Mr. Green")
        if suspect == "Mrs. White":
            print("5 for Mrs. White")
        if suspect == "Mrs. Peacock":
            print("6 for Mrs. Peacock")

    player_choice = int(input("Input the value here: "))

    # Enssure the choice is valid
    while valid_choice == False and (player_choice > 0) and (player_choice < 7):
        if suspects[player_choice-1] != "None":
            valid_choice = True
        else:
            player_choice = int(input("Input a valid value here: "))

    return(player_choice)

def create_player(user_name, user_token):
    # Create player objects
    player = None
    cards = []
    if int(user_token) == 1:
        player = Player(user_name, "Colonel Mustard", True, 1, cards, False, Hallway5)
    elif int(user_token) == 2:
        player = Player(user_name, "Miss Scarlet", True, 1, cards, False, Hallway2)
    elif int(user_token) == 3: 
        player = Player(user_name, "Professor Plum", True, 1, cards, False, Hallway3)
    elif int(user_token) == 4:
        player = Player(user_name, "Mr. Green", True, 1, cards, False, Hallway9)
    elif int(user_token) == 5:
        player = Player(user_name, "Mrs. White", True, 1, cards, False, Hallway10)
    elif int(user_token) == 6:
        player = Player(user_name, "Mrs. Peacock", True, 1, cards, False,Hallway6)
    else:
        print("No Player Created")
        exit()

    return(player)

#-----------------------------------------------------------------------------
# - Gameplay Functions
#-----------------------------------------------------------------------------
def increment_tracker(players, turn_tracker):
    # If all players have gone once, increment the counter
    min_num = min(players,key=attrgetter('turnCount'))
    if turn_tracker < min_num.turnCount:
        return(min_num.turnCount)
    else:
        return(turn_tracker)

def players_turn(players, turn_tracker):
    # Choose the next player who matches the turn count
    for player in players:
        if player.turnCount == turn_tracker:
            player.playerTurn = True
            return(player) # This should always return
    else:
        print("Error in player turn")
        exit()
def show_hand_prompt(player):
    # Allow the player to decide to see their hand
    valid_choice = False
    show_hand_choice = 0
    print("\n")
    print("{}: Do you want to see your hand? ".format(player.playerName))
    while valid_choice == False:
        show_hand_choice = int(input("1 for yes and 2 for no: "))
        if (show_hand_choice == 1) or (show_hand_choice == 2):
            valid_choice = True
    
    return(show_hand_choice)

def prompt_accusation(player):
    # Prompt accusation options and return int for yes or no
    valid_choice = False
    accusation_choice = 0
    print("\n{}: Do you want to make an accusation? ".format(player.playerName))
    while valid_choice == False:
        accusation_choice = int(input("1 for yes and 2 for no: "))
        if (accusation_choice == 1) or (accusation_choice == 2):
            valid_choice = True

    return(accusation_choice)

def accuse(player, case_file):
    # Player will choose options and accuse. Returns True or False
    global Rooms, Weapons, Suspects, Master_List

    # Show Case File to make it easier to test the decision
    if debugger == 4:
        print("\n")
        print("---CASE FILE---")
        case_file.show_case_file()
    
    accusation_choices = []
    
    options = 1
    valid_choices = False

    while valid_choices == False:
        print("\n")
        print("Suspect options: ")
        for suspect in Suspects:
            print("{} for {}".format(options, suspect))
            options += 1
        suspect_choice = int(input("Choose the Suspect: "))
        if (suspect_choice <= len(Suspects)) and (suspect_choice > 0):
            accusation_choices.append(Suspects[suspect_choice-1])
            valid_choices = True

    options = 1
    valid_choices = False

    while valid_choices == False:
        print("\n")
        print("Room options: ")
        for room in Rooms:
            print("{} for {}".format(options, room))
            options += 1
        room_choice = int(input("Choose the Room: "))
        if (room_choice <= len(Rooms)) and (room_choice > 0):
            accusation_choices.append(Rooms[room_choice-1])
            valid_choices = True

    options = 1
    valid_choices = False

    while valid_choices == False:
        print("\n")
        print("Weapon options: ")
        for weapon in Weapons:
            print("{} for {}".format(options, weapon))
            options += 1
        weapon_choice = int(input("Choose the Weapon: "))
        if (weapon_choice <= len(Weapons)) and (weapon_choice > 0):
            accusation_choices.append(Weapons[weapon_choice-1])
            valid_choices = True

    Winner = player.make_accusation(accusation_choices[0], accusation_choices[1], accusation_choices[2], case_file)
    if Winner == False:
        print("\n")
        print(player.playerName + ": Your accusation was incorrect. You can no longer win, but you may still prove suggestions false.")
        player.actve = False

    return(Winner)

def prompt_movement_options(available_destinations):
    # Prompt to move to a location
    valid_choice = False
    movement_decision = 0
    print("\n")
    print("Choose a destination to move to? ")
    while valid_choice == False:
        movement_choice = 1
        for destination in available_destinations:
            print("{} for {}".format(movement_choice, destination))
            movement_choice += 1

        movement_decision = int(input("Choose your new location: "))
        if (movement_decision > 0) and (movement_decision <= len(available_destinations)):
            valid_choice = True

    return(movement_decision)

def select_token():
    global Suspects

    print("Choose a Suspect")
    suspect_choice = 1
    for suspect in Suspects:
        print("{} for {}".format(suspect_choice, suspect))
        suspect_choice += 1

    suspect_decision = int(input("Choose your suspect: "))

    return(Suspects[suspect_decision-1])

def select_weapon():
    global Weapons

    print("\n")
    print("Choose a Weapon")
    weapon_choice = 1
    for weapon in Weapons:
        print("{} for {}".format(weapon_choice, weapon))
        weapon_choice += 1

    weapon_decision = int(input("Choose your weapon: "))

    return(Weapons[weapon_decision-1])

def prompt_suggestion():
    # Prompt suggestion options and return int for yes or no
    valid_choice = False
    suggestion_choice = 0
    print("\n")
    print("Do you want to make an Suggestion? ")
    while valid_choice == False:
        suggestion_choice = int(input("1 for yes and 2 for no: "))
        if (suggestion_choice == 1) or (suggestion_choice == 2):
            valid_choice = True

    return(suggestion_choice)

def prompt_reveal(other_player):
    # Prompt reveal options and return int for yes or no
    valid_choice = False
    reveal_choice = 0
    print("{}: Do you want to reveal another Card? ".format(other_player.playerName))
    while valid_choice == False:
        reveal_choice = int(input("1 for yes and 2 for no: "))
        if (reveal_choice == 1) or (reveal_choice == 2):
            valid_choice = True

    return(reveal_choice)

def decision_tree(players, player, case_file, board):
    # Get decisions and prompt player for actions
    global Rooms, Weapons, Suspects, Master_List
    
    Winner = False
        
    # Propose making an accusation
    accusation_choice = prompt_accusation(player)
    if accusation_choice == 1:
        Winner = accuse(player, case_file)
        return(Winner)

    # else See where the player's token is
    token = player.playerToken
    token_location = board.get_token_location(token)
    
    # Check if the player's token has been moved or not
    if player.startLocation == token_location:   # The player was not moved
        available_destinations = board.get_available_destinations(token_location)
        if not available_destinations: # list is empty
            print("\n")
            print("No available destinations to move to")      
            # Propose making an accusation
            accusation_choice = prompt_accusation(player)
            if accusation_choice == 1:
                Winner = accuse(player, case_file)
                return(Winner)
            else:
                print("Lose Your Turn")
                return(Winner)        
        else:  # There are available spaces
            movement_choice = prompt_movement_options(available_destinations)
            new_location = available_destinations[movement_choice-1]
            
            board.remove_token_from_location(token)
            board.place_token_in_location(token, new_location)
            token_location = new_location
            player.startLocation = new_location

            if token_location in Rooms:
                # Propose Suggestion
                # suggestion_choice = prompt_suggestion()
                suggestion_choice = 1
                if suggestion_choice == 1: 
                    print("\n")   
                    print(player.playerName + ": Make a Suggestion")   
                    selected_token = select_token()
                    selected_weapon = select_weapon()
                    
                    board.remove_token_from_location(selected_token)
                    board.place_token_in_location(selected_token, token_location)
                    
                    board.remove_weapon_from_location(selected_weapon)
                    board.set_weapon_location(token_location, selected_weapon)
            
                    player.make_suggestion(selected_token, token_location, selected_weapon)
                    
                    reveal_counter = 0
                    for other_player in players:
                        if reveal_counter == 1:
                            break
                        if other_player is player:
                            continue
                        else:
                            other_player_cards = other_player.prove_suggestion_false(selected_token, token_location, selected_weapon)
                            if not other_player_cards:  # No matching cards
                                continue
                            else:  # has matching cards
                                reveal_counter = 0
                                for card in other_player_cards:
                                    if reveal_counter == 0:  # must show at least one card
                                        card_to_reveal = other_player.select_card_to_reveal(other_player_cards)
                                        print(card_to_reveal.name) 
                                        reveal_counter += 1
                                    else:
                                        reveal_choice = prompt_reveal(other_player)
                                        if reveal_choice == 1:
                                            card_to_reveal = other_player.select_card_to_reveal(other_player_cards)
                                            print(card_to_reveal.name)
                                        else:
                                            return(Winner)
                                        
                    accusation_choice = prompt_accusation(player)
                    if accusation_choice == 1:
                        Winner = accuse(player, case_file)
                        return(Winner)
                    else:
                        return(Winner)
                else:
                    # Propose making an accusation
                    accusation_choice = prompt_accusation(player)
                    if accusation_choice == 1:
                        Winner = accuse(player, case_file)
                        return(Winner)
                    else:
                        return(Winner)                   
            else:
                # In Hallway
                # Propose making an accusation
                accusation_choice = prompt_accusation(player)
                if accusation_choice == 1:
                    Winner = accuse(player, case_file)
                    return(Winner)
                else:
                    return(Winner)
    else:  # player was moved
        if token_location in Rooms:  # Should be true
            # Propose Suggestion
            suggestion_choice = prompt_suggestion()
            if suggestion_choice == 1:   
                           
                selected_token = select_token()
                selected_weapon = select_weapon()
                
                board.remove_token_from_location(selected_token)
                board.place_token_in_location(selected_token, token_location)
                
                board.remove_weapon_from_location(selected_weapon)
                board.set_weapon_location(token_location, selected_weapon)
        
                player.make_suggestion(selected_token, token_location, selected_weapon)

                reveal_counter = 0
                for other_player in players:
                    if reveal_counter == 1:
                            break
                    if other_player is player:
                        continue
                    else:
                        other_player_cards = other_player.prove_suggestion_false(selected_token, token_location, selected_weapon)
                        if not other_player_cards:  # No matching cards
                            continue
                        else:  # has matching cards
                            reveal_counter = 0
                            for card in other_player_cards:
                                if reveal_counter == 0:  # must show at least one card
                                    card_to_reveal = other_player.select_card_to_reveal(other_player_cards)
                                    print(card_to_reveal.name) 
                                    reveal_counter += 1
                                else:
                                    reveal_choice = prompt_reveal(other_player)
                                    if reveal_choice == 1:
                                        card_to_reveal = other_player.select_card_to_reveal(other_player_cards)
                                        print(card_to_reveal.name)
                                    else:
                                        return(Winner)
                                        
                # All players passed, return
                # Propose making an accusation
                accusation_choice = prompt_accusation(player)
                if accusation_choice == 1:
                    Winner = accuse(player, case_file)
                    return(Winner)
                else:
                    return(Winner)
            else:  # suggestion not chosen, can move           
                # Propose making an accusation
                accusation_choice = prompt_accusation(player)
                if accusation_choice == 1:
                    Winner = accuse(player, case_file)
                    return(Winner)
                else:
                    return(Winner)
        else:  # Should not occur
            # Propose making an accusation
            accusation_choice = prompt_accusation(player)
            if accusation_choice == 1:
                Winner = accuse(player, case_file)
                return(Winner)
            else:
                return(Winner)
            
def main():

    # Game Header
    print("\n========================================")
    print("{:^40}").format("CLUE-LESS")
    print("========================================\n")

    # -------------------------------------------------------------------------
    # - Setup Game
    #--------------------------------------------------------------------------

    global Rooms, Suspects, Weapons, Master_List
    
    # -----------------------------------------------------
    # Create the Board

    board = Board()
    
    # TEST Board
    if debugger == 1:
        Clue_Less_Tester.boardTest(board)

    board.add_all_items_to_board(Suspects, Weapons)
    
    # TEST Board with weapons and suspects
    if debugger == 1:
        Clue_Less_Tester.boardTest(board)

    # -----------------------------------------------------
    # Create Users

    # User inputs number of players. This may be overriden with multiple clients
    num_users = 0
    while (num_users < 1) or (num_users > 6):
        num_users = int(input('Input the number of players (1-6): '))

    # Have each player create a user name
    player_names = []
    for i in range(0, num_users):
        player_name = get_player(i+1)
        player_names.append(player_name)

    # TEST player names created
    if debugger == 2:
        Clue_Less_Tester.playerNames(player_names)

    # -----------------------------------------------------
    # Create the Players

    # Have players choose character tokens and create Player Objects
    players = []
    cards = []
    characters = copy_suspects(Suspects)
    for player in player_names:
        user_token = choose_token(player, characters)
        players.append(create_player(player, user_token))    
        characters[user_token - 1] = "None"

    # TEST Players created properly
    if debugger == 2:
        Clue_Less_Tester.playerCreated(players)

    # -----------------------------------------------------
    # Initialize cards and decks

    card_type = ""
    value = 1
    clue_deck = Deck()
    for name in Master_List:
        if name in Rooms:
            card_type = "Room"
        elif name in Suspects:
            card_type = "Suspect"    
        elif name in Weapons:
            card_type = "Weapon"
        else:
            print(name)
            print("Error")
            exit()

        # Create a Card and add to the Deck of cards
        clue_deck.cards.append(Card(value, card_type, name))
        value += 1

    # TEST Deck (ordered)
    if debugger == 3:
        Clue_Less_Tester.deck(clue_deck)

    clue_deck.shuffle_cards()

    # TEST Deck (shuffled)
    if debugger == 3:
        Clue_Less_Tester.deck(clue_deck)

    # Distribute Cards to Case File
    case_file = clue_deck.distribute_cards_case_file()
    
    # TEST Case File
    if debugger == 3:
        print("CASE FILE")
        case_file.show_case_file()

    # Distribute Cards to Players' Hands
    player_hands = []
    for i in range(0,len(players)):
        player_hands.append([])

    player_hands = clue_deck.distribute_cards_players(player_hands)

    player_hand_index = 0
    for player in players:
        player.cards = player_hands[player_hand_index]
        player_hand_index += 1

    # TEST if the hands have been filled
    if debugger == 3:
        for player in players:
            Clue_Less_Tester.hand(player.cards)

    # -------------------------------------------------------------------------
    # - Game Play
    #--------------------------------------------------------------------------

    Winner = False
    turn_tracker = 1
    while Winner == False:
        # End Game if There are no Winners
        player_count = num_users
        for player in players:
            if player.active == False:
                player_count -= 1            
        if player_count == 0:
            print("You all are Winners in my book! But better luck next time!")
            break
        
        # Choose the player
        turn_tracker = increment_tracker(players, turn_tracker)
        player = players_turn(players, turn_tracker)
                
        # If player is not active. End turn
        if player.active == False:
            player.turnCount += 1
            continue

        # If the player is active, prompt to veiw hand
        show_hand_decision = show_hand_prompt(player)
        if show_hand_decision == 1:
            player.show_hand()

        Winner = decision_tree(players, player, case_file, board)

        # If is Winner by accusation, end game
        if Winner == True:
            print("\n")
            print("The Winner is: " + player.playerName)
            print(case_file.show_case_file())
            break
        

        # End players turn
        player.turnCount += 1
        player.playerTurn = False

        # Limit turns 
        if debugger > 0:
            Clue_Less_Tester.turn_tester(ending_number)


if __name__ == "__main__":
    main()
    
'''
OLD CODE SNIPPETS

# def move_own_token(player, token_location, board, new_location):
#     # Move own token to a new location and update player and board
#     board.remove_token_from_location(player.playerToken)
#     
#     board.place_token_in_location(player.playerToken, new_location)
#     player.startLocation = new_location
#     print("{}'s new location is {}".format(player.playerName, player.startLocation))

# def move_player_token(token_location, token, board):
#     # Move a player's token to a new location
#     board.remove_token_from_location(token)
#     board.place_token_in_location(token, token_location)

# def move_weapon(token_location, weapon, board):
#     # Move a weapon to a new location
#     board.remove_weapon_from_location(weapon)
#     board.set_weapon_location(token_location, weapon)

#             token_location = move_player_token(new_location, token, board)
#             token_location = player.startLocation  
#             move_own_token(player, token_location, board, new_location)
#             token_location = player.startLocation

#             # Propose making an accusation
#             accusation_choice = prompt_accusation(player)
#             if accusation_choice == 1:
#                 Winner = accuse(player, case_file)
#                 return(Winner)

#                     move_player_token(token_location, selected_token, board)
#                     move_weapon(token_location, selected_weapon, board)

#                                     while reveal_counter < len(other_player_cards):
#                                         reveal_choice = prompt_reveal(other_player)
#                                         if reveal_choice == 1:
#                                             card_to_reveal = other_player.select_card()
#                                             print(card_to_reveal.name) 
#                                         else:
                                                              
#                             reveal_choice = prompt_reveal(other_player) 
#                             if reveal_choice == 1:
#                                 card_to_reveal = other_player.select_card()
#                                 print(card_to_reveal.name)
                    # All players passed, return
                    # Propose making an accusation
                    
#                                     while reveal_counter < len(other_player_cards):
#                                         reveal_choice = prompt_reveal(other_player)
#                                         if reveal_choice == 1:
#                                             card_to_reveal = other_player.select_card()
#                                             print(card_to_reveal.name) 
#                                         else:
                                                              
#                             reveal_choice = prompt_reveal(other_player) 
#                             if reveal_choice == 1:
#                                 card_to_reveal = other_player.select_card()
#                                 print(card_to_reveal.name)

#             available_destinations = board.get_available_options(token_location)
#             if not available_destinations: # list is empty
#                 print("No movements possible")
#                 # Propose making an accusation
#                 accusation_choice = prompt_accusation()
#                 if accusation_choice == 1:
#                     Winner = accuse(player, case_file)
#                     return(Winner)
#                 else:
#                     print("Lose Your Turn")
#                     return(Winner)
#             else:  # There are available spaces
#                 movement_choice = prompt_movement_options(available_destinations)
#                 new_location = available_destinations[movement_choice-1]
#                 move_own_token(player, token_location, board, new_location)
#                 token_location = player.startLocation
# 
#                 if token_location in Rooms:
#                     # Propose Suggestion
#                     # suggestion_choice = prompt_suggestion()
#                     suggestion_choice = 1
#                     if suggestion_choice == 1:    
#                         selected_token = select_token()
#                         selected_weapon = select_weapon()
#                         move_player_token(token_location, selected_token, board)
#                         move_weapon(token_location, selected_weapon, board)
#                         player.make_suggestion(selected_token, token_location, selected_weapon)
# 
#                         for other_player in players:
#                             if other_player is player:
#                                 pass
#                             else:
#                                 reveal_choice = prompt_reveal(other_player) 
#                                 if reveal_choice == 1:
#                                     card_to_reveal = other_player.select_card()
#                                     print(card_to_reveal.name)
#                     return(Winner)
#                 else:
#                     pass # Moved to a Hallway
# 
#                 # Propose making an accusation
#                 accusation_choice = prompt_accusation(player)
#                 if accusation_choice == 1:
#                     Winner = accuse(player, case_file)
#                     return(Winner)

'''