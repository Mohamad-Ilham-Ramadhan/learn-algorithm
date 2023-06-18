import unittest
from coba import maxProduct

n1 = [2,3,-2,4] # expect: 6
n2 = [-2,0,-1]  # expect: 0
n3 = [-1,2,-1,8] # expect: 16
n4 = [-2,-3,-1,-5,-10,-6,-7] # expect: 6300
n5 = [-2,10,2,1,-3] # expect: 120
n6 = [-3] # expect: -3
n7 = [2,-5,-2,-4,3] # expect: 24, output: 20

class TestCalc(unittest.TestCase):
    def test_xxx(self):
        self.assertEqual(maxProduct(n1), 6) 
        self.assertEqual(maxProduct(n2), 0) 
        self.assertEqual(maxProduct(n3), 16) 
        self.assertEqual(maxProduct(n4), 6300) 
        self.assertEqual(maxProduct(n5), 120) 
        self.assertEqual(maxProduct(n6), -3) 
        self.assertEqual(maxProduct(n7), 24) 


if __name__ == "__main__":
    unittest.main()
