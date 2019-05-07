#===============================================================================
# - Imports
#===============================================================================
import random

#==============================================================================
# - Configurations
#==============================================================================
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

class Location(object):
	'''
	The is the Parent location class.
	Attributes:
		- name: String		- Room or Hallway name
		- occupied: Bool	- Has player or not
		- player: String 	- Character token
		- links: List 		- Names of locations connected to the location
		- location_type: String		- Empty in this class
	Behaviors:
		- __init__():		- Constructor which sets location and links
	'''
	def __init__ (self, location, links):
		self.name = location
		self.occupied = False
		self.players = []
		self.links = links
		self.location_type = ""


class Room(Location):
	'''
	The Room class which is a subclass of the Location Class.
	Attributes:
		- location_type: String	- Room
		- weapon: String		- Weapon name
	Behaviors:
		- __init__():		- Constructor which calls the super and sets the location_type. b
	'''
	def __init__(self, location, links):
		super(Room, self).__init__(location, links)
		self.location_type = "Room" 
		self.weapon = ""


class Hallway(Location):
	'''
	The Hallway class which is a subclass of the Location Class.
	Attributes:
		- location_type: String	- Hallway
	Behaviors:
		- __init__():		- Constructor which calls the super and sets the location_type.
	'''
	def __init__(self, location, links):
		super(Hallway, self).__init__(location, links)
		self.location_type = "Hallway"
		self.weapon = ""  # Should always be empty


class Board:
	'''
	The Board class which is a list of locations.
	Attributes:
		- locations: List 	- Location objects
	Behaviors:
		- __init__():		- Constructor which calls buil_board() to set the locations
		- build_board():	- Creates Location objects and appends to the list
		- add_all_weapons_to_board():	- Initialize weapons on the board in random rooms
	'''
	def __init__(self):
		self.locations = self.build_board()

	def build_board(self):
		# Create Location objects and appends to the locations list to be returned for the board.
		locations = []
		
		locations.append(Location(Study, [Hallway1, Hallway3, Kitchen]))
		locations.append(Hallway(Hallway1, [Study, Hall]))
		locations.append(Room(Hall, [Hallway1, Hallway2, Hallway4]))
		locations.append(Hallway(Hallway2, [Hall, Lounge]))
		locations.append(Room(Lounge, [Hallway2, Hallway5, Conservatory]))
		locations.append(Hallway(Hallway3, ["Study", Library]))
		locations.append(Hallway(Hallway4, [Hall, Billiard_Room]))
		locations.append(Hallway(Hallway5, [Lounge, Dining_Room]))
		locations.append(Room(Library, [Hallway3, Hallway6, Hallway8]))
		locations.append(Hallway(Hallway6, [Library, Billiard_Room]))
		locations.append(Room(Billiard_Room, [Hallway4, Hallway6, Hallway7, Hallway9]))
		locations.append(Hallway(Hallway7, [Billiard_Room, Dining_Room]))
		locations.append(Room(Dining_Room, [Hallway5, Hallway7, Hallway10]))
		locations.append(Hallway(Hallway8, [Library, Conservatory]))
		locations.append(Hallway(Hallway9, [Billiard_Room, Ballroom]))
		locations.append(Hallway(Hallway10, [Dining_Room, Kitchen]))
		locations.append(Room(Conservatory, [Hallway8, Hallway11, Lounge]))
		locations.append(Hallway(Hallway11, [Conservatory, Ballroom]))
		locations.append(Room(Ballroom, [Hallway9, Hallway11, Hallway12]))
		locations.append(Hallway(Hallway12, [Ballroom, Kitchen]))
		locations.append(Room(Kitchen, [Hallway10, Hallway12, Study]))

		return(locations)

	def add_all_items_to_board(self, Suspects, Weapons):
		# Initialize suspect tokens on the board
		for location in self.locations:
			if location.name == Hallway5:
				location.occupied = True
				location.players.append("Colonel Mustard")
			elif location.name == Hallway2:
				location.occupied = True
				location.players.append("Miss Scarlet")
			elif location.name == Hallway3:
				location.occupied = True
				location.players.append("Professor Plum")
			elif location.name == Hallway11:
				location.occupied = True
				location.players.append("Mr. Green")
			elif location.name == Hallway12:
				location.occupied = True
				location.players.append("Mrs. White")
			elif location.name == Hallway8:
				location.occupied = True
				location.players.append("Mrs. Peacock")
			else:
				continue
		
		# Initialize weapons on the board in random rooms
		added_weapons = 0
		while added_weapons < 6:
			for location in self.locations:
				if location.location_type == "Room":
					if location.weapon == "":
						add_weapon = random.randint(0,1)
						if add_weapon == 1:
							location.weapon = Weapons[added_weapons]
							added_weapons += 1
						else:
							continue
					else:
						continue
				else:
					continue

	def get_token_location(self, token):
		# Find the location of the matching token and return its location
		for location in self.locations:
			if location.players == None:
				continue
			else:
				for player in location.players:
					if player == token:
						return(location.name)

	def remove_token_from_location(self, token):
		for location in self.locations:
			if location.players == None:
				continue
			else:
				for player in location.players:
					if player == token:
						location.players.remove(token)
						return()
		print("No Token Found")

	def place_token_in_location(self, token, new_location):
		for location in self.locations:
			if location.name == new_location:
				location.players.append(token)

	def get_location_index(self, location_name):
		# Return the index of the matching location
		i = 0
		for location in self.locations:
			if location.name == location_name:
				return(i)
			else:
				i += 1
				
	def set_player_location(self, index, player):
		self.locations[index].occupied = True
		self.locations[index].players.append(player)

	def get_weapon_location(self, weapon):
		for location in self.locations:
			if location.location_type == "Room":
				if location.weapon == weapon:
					return(weapon)
					break

	def set_weapon_location(self, room, weapon):
		for location in self.locations:
			if location.location_type == "Room":
				if location.name == room:
					location.weapon = weapon
					break

	def remove_weapon_from_location(self, weapon):
		for location in self.locations:
			if location.location_type == "Room":
				if location.weapon == weapon:
					location.weapon = ""
					break

	def get_available_destinations(self, player_location):
		# Get the location's links that are not occupied
		linked_spaces = []
		for location in self.locations:
			if location.name == player_location:  # We found the player's location	
				for link in location.links:  # Get the names of each link
					linked_spaces.append(link)

		# See availability
		available_spaces = []
		for link in linked_spaces:
			for location in self.locations:  # re-iterate through locations
				if (location.name == link):  # Match
					if (location.location_type == "Hallway") and (location.occupied == False):
						available_spaces.append(location.name)
					elif (location.location_type == "Room"):  # Multiple people can be in a room
						available_spaces.append(location.name)
					else:
						pass

		return(available_spaces)

	def print_board_layout(self):

		Study = None
		Hallway1 = None
		Hall = None
		Hallway2 = None
		Lounge = None
		Hallway3 = None
		Hallway4 = None
		Hallway5 = None
		Library = None
		Hallway6 = None
		Billiard_Room = None
		Hallway7 = None
		Dining_Room = None
		Hallway8 = None
		Hallway9 = None
		Hallway10 = None
		Conservatory = None
		Hallway11 = None
		Ballroom = None
		Hallway12 = None
		Kitchen = None

		for location in self.locations:
			if location.name == "Study":
				Study = location
			if location.name == "Study - Hall":
				Hallway1 = location
			if location.name == "Hall":
				Hall = location
			if location.name == "Hall - Lounge":
				Hallway2 = location
			if location.name == "Lounge":
				Lounge = location
			if location.name == "Study - Library":
				Hallway3 = location
			if location.name == "Hall - Billiard Room":
				Hallway4 = location
			if location.name == "Lounge - Dining Room":
				Hallway5 = location
			if location.name == "Library":
				Library = location
			if location.name == "Library - Billiard Room":
				Hallway6 = location
			if location.name == "Billiard Room":
				Billiard_Room = location
			if location.name == "Billiard Room - Dining Room":
				Hallway7 = location
			if location.name == "Dining Room":
				Dining_Room = location
			if location.name == "Library - Conservatory":
				Hallway8 = location
			if location.name == "Billiard Room - Ballroom":
				Hallway9 = location
			if location.name == "Dining Room - Kitchen":
				Hallway10 = location
			if location.name == "Conservatory":
				Conservatory = location
			if location.name == "Conservatory - Ballroom":
				Hallway11 = location
			if location.name == "Ballroom":
				Ballroom = location
			if location.name == "Ballroom - Kitchen":
				Hallway12 = location
			if location.name == "Kitchen":
				Kitchen = location

			# {:10} ?
		print("___________________________________________________________________________________________________________")
		print("|{:^15} = {:^20} = {:^15} = {:^20} = {:^15}    |".format(Study.name, Hallway1.name, Hall.name, Hallway2.name, Lounge.name))
		print("|{:10}   {:10}   {:10}   {:10}   {:10}|".format(Study.players, Hallway1.players, Hall.players, Hallway2.players, Lounge.players))
		# print("|{} = {} = {} = {} = {}|".format(Study.weapon, Hallway1.weapon, Hall.weapon, Hallway2.weapon, Lounge.weapon))
		print("|{:10}           {:10}            {:10}|".format("||", "||", "||"))
		print("|{}        {}        {}|".format(Hallway3.name, Hallway4.name, Hallway5.name))
		print("|{}        {}        {}|".format(Hallway3.players, Hallway4.players, Hallway5.players))
		# print("|{}        {}        {}|".format(Hallway3.weapon, Hallway4.weapon, Hallway5.name))
		print("|||        ||        |||")
		print("|{:^15} = {:^20}= {:^15} = {:^20} = {:^13}|".format(Library.name, Hallway6.name, Billiard_Room.name, Hallway7.name, Dining_Room.name))
		print("|{}   {}   {}   {}   {}|".format(Library.players, Hallway6.players, Billiard_Room.players, Hallway7.players, Dining_Room.players))
		# print("|{} = {} = {} = {} = {}|".format(Library.weapon, Hallway6.weapon, Billiard_Room.weapon, Hallway7.weapon, Dining_Room.weapon))
		print("|||        ||        |||")
		print("|{}        {}        {}|".format(Hallway8.name, Hallway9.name, Hallway10.name))
		print("|{}        {}        {}|".format(Hallway8.players, Hallway9.players, Hallway10.players))
		# print("|{}        {}        {}|".format(Hallway8.weapon, Hallway9.weapon, Hallway10.name))
		print("|||        ||        |||")
		print("|{:^15} = {:^20} = {:^15} = {:^20} = {:^15}    |".format(Conservatory.name, Hallway11.name, Ballroom.name, Hallway12.name, Kitchen.name))
		print("|{}   {}   {}   {}   {}|".format(Conservatory.players, Hallway11.players, Ballroom.players, Hallway12.players, Kitchen.players))
		# print("|{} = {} = {} = {} = {}|".format(Conservatory.weapon, Hallway11.weapon, Ballroom.weapon, Hallway12.weapon, Kitchen.weapon))
		print("|_________________________________________________________________________________________________________|")

