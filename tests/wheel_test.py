'''
Created on Sep 1, 2011

@author: jflaherty
'''
import unittest
from roulette.outcome import Outcome
from roulette.wheel import Wheel    
from roulette.non_random import NonRandom

class Test(unittest.TestCase):


    def setUp(self):
        self.five = Outcome("00-0-1-2-3", 6)
        self.zero = Outcome("0", 35)
        self.zerozero = Outcome("00", 35)
        rng = NonRandom(0, 1)
        rng.set_seed(5);
        self.wheel = Wheel(rng)
        
    def test_populate_wheel(self):
        self.wheel.add_outcome(5, self.five)
        self.wheel.add_outcome(0, self.zero)
        self.wheel.add_outcome(37, self.zerozero)
        self.assertEqual(len(self.wheel.bins), 38, "Number of bins == %d" % (len(self.wheel.bins)))
        bin0 = self.wheel.bins[0]
        bin5 = self.wheel.bins[5]
        bin00 = self.wheel.bins[37]
        self.assertTrue(self.zero in bin0.outcomes, "%s is in %s" % (self.zero, bin0))
        self.assertTrue(self.five in bin5.outcomes, "%s is in %s" % (self.five, bin5))
        self.assertTrue(self.zerozero in bin00.outcomes, "%s is in %s" % (self.zerozero, bin0))
        self.assertTrue(bin0 in self.wheel.bins)
        self.assertTrue(bin5 in self.wheel.bins)
        self.assertTrue(bin00 in self.wheel.bins)
    
    def test_random_bin(self):
        self.wheel.add_outcome(5, self.five)
        self.wheel.add_outcome(0, self.zero)
        self.wheel.add_outcome(37, self.zerozero)
        random_bin = self.wheel.next()
        self.assertTrue(self.five in random_bin.outcomes)        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
