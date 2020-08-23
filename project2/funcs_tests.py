import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test_update_acc1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)
   def test_update_acc2(self):
      self.assertAlmostEqual(updateAcceleration(9.8, 7),3.92)
   def test_update_acc3(self):
      self.assertAlmostEqual(updateAcceleration (5.5, 9) , 4.4)
   def test_update_alt1(self):
      self.assertAlmostEqual(updateAltitude(10, 7, 5) , 19.5)
   def test_update_alt2(self):
       self.assertAlmostEqual(updateAltitude(30,2, 11), 37.5)
   def test_update_vel1(self):
       self.assertEqual(updateVelocity (10,10), 20)
   def test_update_vel2(self):
       self.assertAlmostEqual(updateVelocity(11.5, 12), 23.5)
   def test_update_fuel(self):
       self.assertEqual(updateFuel(15, 10), 5)
   def test_update_fuel2(self):
       self.assertEqual(updateFuel(22,7),15)
    #Run the unit tests.
if __name__ == '__main__':
   unittest.main()
