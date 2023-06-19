import unittest
import time
from coba import maxSubarray

n1 = [-2,1,-3,4,-1,2,1,-5,4] # expect: 6
n2 = [1] # expect: 1
n3 = [5,4,-1,7,8] # expect: 23
n4 = [-2,-4,-1,-3] # expect: -1
n5 = [0,0,4,55,-78,-2,100,3,-20] # expect: 103

 

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
    
    def tearDown(self) -> None:
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_xxx(self):
        self.assertEqual(maxSubarray(n1), 6) 
        self.assertEqual(maxSubarray(n2), 1) 
        self.assertEqual(maxSubarray(n3), 23) 
        self.assertEqual(maxSubarray(n4), -1) 
        self.assertEqual(maxSubarray(n5), 103) 
        


if __name__ == "__main__":
    unittest.main()
