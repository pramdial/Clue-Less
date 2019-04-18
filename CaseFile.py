#!/usr/bin/env python

#===============================================================================
# - Documentation
#===============================================================================
# P. Lin 04/17/2019
# P. Ramdial - Modified to take Card Objects 04/18/2019

# NOTE:
#   1. show_case_file() returns a list of strings


#==============================================================================
# - Class
#============================================================================== 
# class: CaseFile
# attributes: who(Card), where(Card), weapon(Card)
# function: show_case_file()
class CaseFile(object):
    def __init__(self, room, suspect, weapon):
        self.room = room  # Card Object
        self.suspect = suspect  # Card Object
        self.weapon = weapon  # Card Object

    def show_case_file(self):
        # print("Showing Case File: Room: {}, Suspect: {}, Weapon: {}".format(self.room.name, self.suspect.name, self.weapon.name))
        return([self.room.name, self.suspect.name, self.weapon.name])

