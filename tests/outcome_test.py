'''
Created on Aug 30, 2011

@author: jflaherty
'''
import unittest
from roulette.outcome import Outcome

class OutcomeTest(unittest.TestCase):


    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """
        self.first = Outcome("red", 1)
        self.second = Outcome("red", 1)
        self.third = Outcome("5 way", 6)

    def test_equal(self):
        self.assertEquals(self.first, self.second, "%s is equal to %s" % (self.first, self.second))
        self.assertEquals(self.second, self.first, "%s is equal to %s" % (self.second, self.first))
        
    def test_unequal(self):
        self.assertNotEqual(self.first, self.third, "%s is not equal to %s" % (self.first, self.third))
        self.assertNotEqual(self.second, self.third, "%s is not equal to %s" % (self.second, self.third))

    def test_hash(self):
        self.assertTrue(self.first.__hash__() == self.second.__hash__(), "%d is equal to %d" % (self.first.__hash__(), self.second.__hash__()))
        self.assertFalse(self.first.__hash__() == self.third.__hash__(), "%d is not equals to %d" % (self.first.__hash__(), self.third.__hash__()))
        self.assertFalse(self.second.__hash__() == self.third.__hash__(), "%d is not equals to %d" % (self.second.__hash__(), self.third.__hash__()))
     
    def test_payout(self):
        self.assertTrue(self.first.win_amount(10) == 10);
        self.assertTrue(self.second.win_amount(5) == 5);
        self.assertTrue(self.third.win_amount(10) == 60);
           
if __name__ == "__main__":
    unittest.main()
