'''
Created on Aug 30, 2011

@author: jflaherty
'''

class Outcome(object):
    '''
    classdocs
    '''


    def __init__(self, name, odds):
        '''
        Constructor
        '''
        self.name = name
        self.odds = odds
    
    def win_amount(self, amount):
        return self.odds * amount
    
    def __str__(self):
        return "%s (%d:1) [%d]" % (self.name, self.odds, self.__hash__())

    def __eq__(self, other):
        return (self.name, self.odds) == (other.name, other.odds)
    
    def __ne__(self, other):
        return (self.name, self.odds) != (other.name, other.odds)
    
    def __hash__(self):
        return hash((self.name, self.odds))




    
