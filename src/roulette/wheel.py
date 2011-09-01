'''
Created on Sep 1, 2011

@author: jflaherty
'''
from roulette.bin import Bin

class Wheel(object):
    '''
    classdocs
    '''

    def __init__(self, rng):
        self.rng - rng
        self.bins = tuple(Bin() for i in range(38))
        
    def add_outcome(self, number, outcome):
        self.bins[number].add(outcome)
    
    def next(self):
        return self.rng.choice(self.bins)
    
    def get(self, bin):
        return self.bins[bin]

        
