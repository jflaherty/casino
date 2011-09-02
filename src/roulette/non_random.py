'''
Created on Sep 1, 2011

@author: jflaherty
'''
from random import Random, random

class NonRandom(Random):
    '''
    classdocs
    '''
    def __new__(cls, *args, **kwargs):
        return super (NonRandom, cls).__new__ (cls, random())

    def __init__(self, min, max):
        self.min = min
        self.max = max
    
    def set_seed(self, value): 
        self.value = value
    
    def choice(self, sequence):
        return sequence[self.value]
        
    
