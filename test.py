import unittest
import time
from coba import numDecodings

s1 = '12' # expect: 2 -> 'AB' (1 2) or 'L' (12)
s2 = '226' # expect: 3 -> 'BZ' (2 26) or 'VF' (22 6) or 'BBF' (2 2 6)
s3 = '06' # expect: 0
s4 = '1847624' # expect: 4
s5 = '8473627' # expect: 1
s6 = '122341' # expect: 5
s7 = '121021' # expect: 4
s8 = '2012260' # expect: 0
s9 = '201226' # expect  5
s10 = '1212021' # expect: 6
s11 = '12234192' # expect: 10
s12 = '1212121212' # expect: 89
s13 = '12620' # expect: 3
s14 = '126200121212' # expect: 0
s15 = '121012101' # expect: 4

 

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
    
    def tearDown(self) -> None:
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_xxx(self):
        self.assertEqual(numDecodings(s1), 2) 
        self.assertEqual(numDecodings(s2), 3) 
        self.assertEqual(numDecodings(s3), 0) 
        self.assertEqual(numDecodings(s4), 4) 
        self.assertEqual(numDecodings(s5), 1) 
        self.assertEqual(numDecodings(s6), 5) 
        self.assertEqual(numDecodings(s8), 0) 
        self.assertEqual(numDecodings(s9), 5) 
        self.assertEqual(numDecodings(s10), 6) 
        self.assertEqual(numDecodings(s11), 10) 
        self.assertEqual(numDecodings(s12), 89) 
        self.assertEqual(numDecodings(s13), 3) 
        self.assertEqual(numDecodings(s14), 0) 
        self.assertEqual(numDecodings(s15), 4) 
        


if __name__ == "__main__":
    unittest.main()
