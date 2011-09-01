'''
Created on Sep 1, 2011

@author: jflaherty
'''
from random import Random

class NonRandom(Random):
    '''
    classdocs
    '''
    def __init__(self):
        Random.__init__(self)
    
    def set_seed(self, value): 
        self.value = value
    
    def choice(self, sequence):
        return sequence[self.value]
        
    
