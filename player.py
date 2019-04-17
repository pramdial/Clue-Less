# P. Lin 04/17/2019

from casefile import *


# NOTE:
#   1. player_turn type boolean instead of Player
#   2. current_location type string instead of int
#   3. make_suggestion() returns a list of strings

# class: Player
# attributes: player_name(string), active(boolean), turn_count(int), cards(List<Card>),
#               player_turn(boolean), current_location(string)
# function: make_accusation(CaseFile), make_suggestion()
class Player:
    def __init__(self, player_name, active, turn_count, cards, player_turn, current_location):
        self.playerName = player_name
        self.active = active
        self.turnCount = turn_count
        self.cards = cards
        self.playerTurn = player_turn
        self.currentLocation = current_location

    def make_accusation(self, person, room, weapon, casefile):
        if person.lower() == casefile.person and \
                room.lower() == casefile.room and \
                weapon.lower() == casefile.weapon:
            return True
        else:
            return False

    def make_suggestion(self, person, room, weapon):
        return [person.lower(), room.lower(), weapon.lower()]


# test case
test = CaseFile("Patrick", "Library", "Knife")
answer = test.show_case_file()
print(answer)

place_holder = ["place", "holder"]
myPlayer = Player("Patrick", True, 1, place_holder, True, "kitchen")

incorrect_guess = myPlayer.make_accusation("Mark", "Library", "Knife", test)
print(incorrect_guess)

correct_guess = myPlayer.make_accusation("patrick", "Library", "Knife", test)
print(correct_guess)
