import unittest
import time
from coba import maxProduct

n1 = [2,3,-2,4] # expect: 6
n2 = [-2,0,-1]  # expect: 0
n3 = [-1,2,-1,8] # expect: 16
n4 = [-2,-3,-1,-5,-10,-6,-7] # expect: 6300
n5 = [-2,10,2,1,-3] # expect: 120
n6 = [-3] # expect: -3
n7 = [2,-5,-2,-4,3] # expect: 24, output: 20
n8 = [0,2] # expect: 2, output: 0
n9 = [0,-4,9,-2] # expect: 72
n10 = [0,-4,9,-2,9,-1] # expect: 648
n11 = [1,2,-4,0,8,3] # expect: 24

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
    
    def tearDown(self) -> None:
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_xxx(self):
        # time.sleep(1)
        self.assertEqual(maxProduct(n1), 6) 
        self.assertEqual(maxProduct(n2), 0) 
        self.assertEqual(maxProduct(n3), 16) 
        self.assertEqual(maxProduct(n4), 6300) 
        self.assertEqual(maxProduct(n5), 120) 
        self.assertEqual(maxProduct(n6), -3) 
        self.assertEqual(maxProduct(n7), 24) 
        self.assertEqual(maxProduct(n8), 2) 
        self.assertEqual(maxProduct(n9), 72) 
        self.assertEqual(maxProduct(n10), 648) 
        self.assertEqual(maxProduct(n11), 24) 
        


if __name__ == "__main__":
    unittest.main()
