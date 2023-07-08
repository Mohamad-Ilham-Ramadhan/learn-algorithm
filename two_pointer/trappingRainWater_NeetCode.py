'''
   (two pointers) leetcode: 42. Trapping Rain Water (hard). Companies (Google)

   Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

 

   Example 1:   
      3                       __
      2           __         |  |__    __
      1    __    |  |__    __|  |  |__|  |__
      0   |  |   |  |  |  |  |  |  |  |  |  |
      

      Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
      Output: 6
      Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

   Example 2:

      Input: height = [4,2,0,3,2,5]
      Output: 9
   

   Constraints:
      - n == height.length
      - 1 <= n <= 2 * 10^4
      - 0 <= height[i] <= 10^5
   
   Related Topics: 
      (Array) (Two Pointers) (Dynamic Programming) (Stack) (Monotonic Stack)

   ======================================================================= 

   Solution by NeetCode

   Leetcode submission:
      runtime: 140 ms, beats 50.35%
      memory: 18.3 MB, beats beats 80.98%

'''
# 
def trap(height):
   if not height: return 0 

   l, r = 0, len(height) - 1
   leftMax, rightMax = height[l], height[r]
   res = 0 

   while l < r: 
      if leftMax < rightMax: 
         l += 1
         leftMax = max(leftMax, height[l])
         res += leftMax - height[l]
      else: 
         r -= 1 
         rightMax = max(rightMax, height[r])
         res += rightMax - height[r]
   
   return res

h1 = [0,1,0,2,1,0,1,3,2,1,2,1] # 6
'''
   [2,1]
   0, 0, 1, 1, [1], 2, 2 
'''
h2 = [4,2,0,3,2,5] # 9
'''
   [1,3]
'''
h3 = [4,2,0,3,2,3] # 5
h4 = [3,0,3,0,3,0,3] # 9
h5 = [3,0,3,0,3,0,1,0,1,0,2,0,0] # 14
h6 = [9,1] # 0
h7 = [9,3,7] # 4
h8 = [0,2,0] # 0
h9 = [4,2,0,3,2,1,5,9] # 12
h10 = [5,4,1,2] # 1, output: -1
h11 = [0,1,2,0,3,0,1,2,0,0,4,2,1,2,  5,0,1,2,0,2] # 26, output: 25
'''
   2+
'''
h12 = [9,6,8,8,5,6,3] # 3, output: 2
h14 = [100000,0,99999,0,99998,0,99997,0,99996,0,99995,0,99994,0,99993,0,99992,0,99991,0,99990,0,99989,0,99988,0,99987,0,99986,0,99985,0,99984,0,99983,0,99982,0,99981,0,99980,0,99979,0,99978,0,99977,0,99976,0,99975,0,99974,0,99973,0,99972,0,99971,0,99970,0,99969,0,99968,0,99967,0,99966,0,99965,0,99964,0,99963,0,99962,0,99961,0,99960,0,99959,0,99958,0,99957,0,99956,0,99955,0,99954,0,99953,0,99952,0,99951,0,99950,0,99949,0,99948,0,99947,0,99946,0,99945,0,99944,0,99943,0,99942,0,99941,0,99940,0,99939,0,99938,0,99937,0,99936,0,99935,0,99934,0,99933,0,99932,0,99931,0,99930,0,99929,0,99928,0,99927,0,99926,0,99925,0,99924]

import time
startTime = time.time()
print('RESULT :', trap(h1))
t = time.time() - startTime
print('%s: %.3f' % ('Runtime: ', t))
# 20
# print('RESULT :', trap(h12))

# import unittest
# import time
# class TestCalc(unittest.TestCase):
#     def setUp(self):
#         self.startTime = time.time()
    
#     def tearDown(self) -> None:
#         t = time.time() - self.startTime
#         print('%s: %.3f' % (self.id(), t))

#     def test_xxx(self):
#         self.assertEqual(trap(h1), 6) 
#         self.assertEqual(trap(h2), 9) 
#         self.assertEqual(trap(h3), 5) 
#         self.assertEqual(trap(h4), 9) 
#         self.assertEqual(trap(h5), 14) 
#         self.assertEqual(trap(h6), 0) 
#         self.assertEqual(trap(h7), 4) 
#         self.assertEqual(trap(h8), 0) 
#         self.assertEqual(trap(h9), 12) 
#         self.assertEqual(trap(h10), 1) 
#         self.assertEqual(trap(h11), 26) 
#         self.assertEqual(trap(h12), 3) 

# if __name__ == "__main__":
#     unittest.main()
