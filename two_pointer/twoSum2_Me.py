'''
   (two pointer) leetcode: 167. Two Sum II - Input Array Is Sorted (medium)

   Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 < numbers.length`.

   Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

   The tests are generated such that there is exactly one solution. You may not use the same element twice.

   Your solution must use only constant extra space.

   

   Example 1:
      Input: numbers = [2,7,11,15], target = 9
      Output: [1,2]
      Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

   Example 2:
      Input: numbers = [2,3,4], target = 6
      Output: [1,3]
      Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

   Example 3:
      Input: numbers = [-1,0], target = -1
      Output: [1,2]
      Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
      

   Constraints:
      - 2 <= numbers.length <= 3 * 104
      - -1000 <= numbers[i] <= 1000
      - numbers is sorted in non-decreasing order.
      - -1000 <= target <= 1000
      - The tests are generated such that there is exactly one solution.

   Solution by myself
      using hashmap. O(n * 2) simplified O(n)

   Leetcode submission:
      #1
         runtime: 137 ms, beats 73.85%
         memory: 17.3 MB, beats 17.63%
      #3 (hashmap progression, one loop only.)
         runtime: 135 ms, beats 81.11%
         memory: 17.4 MB, beats 17.63%
      #4 (two pointers)
         runtime: 134 ms, beats 84.13%
         memory: 17.3 MB, beats 17.63%


'''
# attempt 1 using hasmap. O(n * 2)
def twoSum(numbers, target):
   map = {} 
   for i in range(len(numbers)):
      map[numbers[i]] = i

   for i in range(len(numbers)):
      n = numbers[i]
      if target - n in map: 
         print('we find it', i, map[target - n])
         return [i + 1, map[target - n] + 1]
      
# attempt 2 using two pointer. (fail)
import math
def twoSum2(numbers, target):
   j = 1 
   for i in range(len(numbers)):
      n1 = numbers[i]
      n2 = numbers[j]
      print('for ',i,j, n1, n2)
      if n1 + n2 == target:
         return [i+1, j+1]
      if n1 + n2 > target: 
         j = i
         n2 = numbers[j]
         print('sum greater than target', n1, n2)
      if n1 + n2 <= target:
         while j < len(numbers) - 1:
            j += 1
            n2 = numbers[j]
            print('while ',i,j, n1, n2)
            if n1 + n2 == target: 
               return [i+1, j+1]
            if n1 + n2 > target:
               break 
            
# attempt 3 hashmap progression. Time and space: O(N)
def twoSum3(numbers, target):
   map = {numbers[0]: 0} 
   for i in range(1, len(numbers)):
      n = numbers[i]
      d = target - n
      if d in map: 
         return [map[d] + 1, i + 1]
      map[n] = i 

# attempt 4 after watched NeetCode explanation using two pointers
def twoSum4(numbers, target):
   l, r = 0, len(numbers) - 1

   while True: 
      n1 = numbers[l]
      n2 = numbers[r]
      print(n1, n2)
      sum = n1 + n2
      if sum == target:
         return [l + 1, r + 1]
      if sum > target: 
         r -= 1
      elif sum < target: 
         l += 1


n1 = [2,7,11,15]; t1 = 9 # [1,2]
n2 = [2,3,4]; t2 = 6 # [1,3]
n3 = [-1,0]; t3 = -1 # [1,2]
n4 = [-9,-7,-1,4,8,11]; t4 = 2 # [1,6]
n5 = [-9,-7,-1,4,8,10]; t5 = -5 # [1,4]
n6 = [-9,-7,-1,4,8,10]; t6 = 12 # [4,5]
n7 = [-9,-7,-1,4,8,10]; t7 = 7 # [3,5]
n8 = [-9,-7,-1,4,8,13]; t8 = 1 # [2,5]
n9 = [1,2,3,4,4,9,56,90]; t9 = 8 # [4,5]
n10 = [1,3,4,5,7,10,11]; t10 = 9 # [3,4]

# print('RESULT :', twoSum2(n9, t9))

import unittest
import time

class TestCalc(unittest.TestCase):
   def setUp(self):
      self.startTime = time.time()
   
   def tearDown(self) -> None:
      t = time.time() - self.startTime
      print('%s: %.3f' % (self.id(), t))

   def test_xxx(self):
      self.assertEqual(twoSum3(n1, t1), [1,2]) 
      self.assertEqual(twoSum3(n2, t2), [1,3]) 
      self.assertEqual(twoSum3(n3, t3), [1,2]) 
      self.assertEqual(twoSum3(n4, t4), [1,6]) 
      self.assertEqual(twoSum3(n5, t5), [1,4]) 
      self.assertEqual(twoSum3(n6, t6), [4,5]) 
      self.assertEqual(twoSum3(n7, t7), [3,5]) 
      self.assertEqual(twoSum3(n8, t8), [2,5]) 
      self.assertEqual(twoSum3(n9, t9), [4,5]) 
      self.assertEqual(twoSum3(n10, t10), [3,4]) 

if __name__ == "__main__":
   unittest.main()
