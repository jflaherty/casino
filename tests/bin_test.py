'''
Created on Aug 31, 2011

@author: jflaherty
'''
import unittest
from roulette.outcome import Outcome
from roulette.bin import Bin

class Test(unittest.TestCase):


    def setUp(self):
        self.five = Outcome("00-0-1-2-3", 6)
        self.zero = Bin(Outcome("0", 35), self.five)
        self.zerozero = Bin(Outcome("00", 35), self.five)

    def test_bin(self):
        local_five = Outcome("00-0-1-2-3", 6)
        self.assertTrue(self.five in self.zero.outcomes, "%s is in %s" % (self.five, self.zero.outcomes))
        self.assertTrue(local_five in self.zero.outcomes, "%s is in %s" % (local_five, self.zero.outcomes))
        self.assertTrue(self.five in self.zerozero.outcomes, "%s is in %s" % (self.five, self.zerozero.outcomes))
        self.assertTrue(local_five in self.zerozero.outcomes, "%s is in %s" % (local_five, self.zerozero.outcomes))
        self.assertTrue(len(self.zero.outcomes) == 2, "set zero has %d members" % (len(self.zero.outcomes)))
        self.assertTrue(len(self.zerozero.outcomes) == 2, "set zerozero has %d members" % (len(self.zero.outcomes)))
    
    def test_add_bin(self):
        self.zero.add(self.five)
        self.assertTrue(len(self.zero.outcomes) == 2, "set zero still has %d members" % (len(self.zero.outcomes)))
        one = Outcome("1", 1)
        bin_one = Bin(one)
        self.assertTrue(len(bin_one.outcomes) == 1, "set bin_one has %d members" % (len(bin_one.outcomes)))
        bin_one.add(self.five)
        self.assertTrue(len(bin_one.outcomes) == 2, "set bin_one has %d members" % (len(bin_one.outcomes)))
        self.assertTrue(one in bin_one.outcomes, "%s is in %s" % (one, bin_one))
        self.assertTrue(self.five in bin_one.outcomes, "%s is in %s" % (self.five, bin_one))

if __name__ == "__main__":
    unittest.main()
