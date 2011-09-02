'''
Created on Sep 1, 2011

@author: jflaherty
'''
import unittest
from roulette.outcome import Outcome
from roulette.bin import Bin
from roulette.wheel import Wheel    
from roulette.non_random import NonRandom

class Test(unittest.TestCase):


    def setUp(self):
        self.five = Outcome("00-0-1-2-3", 6)
        self.zero = Outcome("0", 35)
        self.zerozero = Outcome("00", 35)
        self.wheel = Wheel(NonRandom().set_seed(1))
        
    def test_populate_wheel(self):
        self.wheel.add_outcome(0, self.five)
        self.wheel.add_outcome(0, self.zero)
        self.wheel.add_outcome(0, self.zero)
        assert
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
