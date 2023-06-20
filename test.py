import unittest
import time
from coba import canJump2, n9, n10

n1 = [2,3,1,1,4] # true
n2 = [3,2,1,0,4] # false
n3 = [5,8,2,3,1,0,0,2,3,1] # true
n4 = [0] # true 
n5 = [1,0] # true
n6 = [2,0,0] # true, output false
n7 = [3,0,8,2,0,0,1] # true, output false
n8 = [3,11,0,8,2,0,0,1,2,1,4,0,1] # true, output false
 

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
    
    def tearDown(self) -> None:
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_xxx(self):
        self.assertEqual(canJump2(n1), True) 
        self.assertEqual(canJump2(n2), False) 
        self.assertEqual(canJump2(n3), True) 
        self.assertEqual(canJump2(n4), True) 
        self.assertEqual(canJump2(n5), True) 
        self.assertEqual(canJump2(n6), True) 
        self.assertEqual(canJump2(n7), True) 
        self.assertEqual(canJump2(n8), True) 
        self.assertEqual(canJump2(n9), False) 
        self.assertEqual(canJump2(n10), True) 


if __name__ == "__main__":
    unittest.main()
