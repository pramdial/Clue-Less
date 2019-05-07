#!/usr/bin/env python

#===============================================================================
# - Documentation
#===============================================================================
# - P. Ramdial 04/16/19

#==============================================================================
# - Class
#============================================================================== 
class Card(object):
    '''
    This is the Card Class
    Attributes:
        - value:     int
        - card_type: String
        - name:      String
    Behaviors:
        - __repr__(): String representation of the Card object
        - get_type(): Get the type of the card
    '''
    def __init__(self, value, card_type, name):
        self.value = value
        self.card_type = card_type
        self.name = name

    def __repr__(self):
        return("Value: {}, Type: {}, Name: {}".format(self.value, self.card_type, self.name))

    def get_type(self):
        return(self.card_type)