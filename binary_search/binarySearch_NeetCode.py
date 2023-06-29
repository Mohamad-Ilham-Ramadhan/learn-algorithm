'''
   (binary search) leetcode: 704. Binary Search (easy)

   Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

   You must write an algorithm with `O(log n)` runtime complexity.

   

   Example 1:
      Input: nums = [-1,0,3,5,9,12], target = 9
      Output: 4
      Explanation: 9 exists in nums and its index is 4

   Example 2:
      Input: nums = [-1,0,3,5,9,12], target = 2
      Output: -1
      Explanation: 2 does not exist in nums so return -1

   Constraints:
      - 1 <= nums.length <= 10^4
      - -10^4 < nums[i], target < 10^4
      - All the integers in nums are unique.
      - nums is sorted in ascending order.
   
   Related topics: 
      (Array) (Binary Search)
   
   ==================================================
   Solution by NeetCode

   Leetcode solution: 
      runtime: 248 ms, beats 50.91%
      memory: 17.9 MB, beats 30.94%
'''
import math

def search(nums, target): 
   l, r = 0, len(nums) - 1 

   while l <= r: 
      m = (l + r) // 2 # `//` =  floor division
      if nums[m] > target: 
         r = m - 1
      elif nums[m] < target: 
         l = m + 1 
      else: 
         return m 
   return -1

n1 = [-1,0,3,5,9,12]; t1 = 9 # 4
n2 = [-1,0,3,5,9,12]; t2 = 2 # -1
n3 = [-1,0,3,5,9,12,13,14,15]; t3 = 3 # 2
n4 = [-1,0,3,5,9,12,13,14,15]; t4 = 15 # 8
n5 = [-6,-1,0,3,5,9,12,13,14,15]; t5 = -6 # 0
n6 = [2,4]; t6 = 2 # 0
n7 = [2,4]; t7 = 4 # 1
t8 = 999 # 999
n9 = [2,4]; t9 = 3 # -1
n10 = [2,4]; t10 = 0 # -1
n11 = [2,4]; t11 = 5 # -1
n12 = [3]; t12 = 3 # 0
n13 = [9]; t13 = 3 # -1
n14 = [9]; t14 = 33 # -1
print('RESULT :', search(n1, t1))
print('RESULT :', search(n2, t2))
print('RESULT :', search(n3, t3))
print('RESULT :', search(n4, t4))
print('RESULT :', search(n5, t5))
print('RESULT :', search(n6, t6))
print('RESULT :', search(n7, t7))
print('RESULT :', search(n9, t9))
print('RESULT :', search(n10, t10))
print('RESULT :', search(n11, t11))
print('RESULT :', search(n12, t12))
print('RESULT :', search(n13, t13))
print('RESULT :', search(n14, t14))


# for t in n8: 
#    print('t', t)
#    if search(n8, t) != t:
#       print('FALSE')
#       break 
# print('TRUE')
   
# print('RESULT :', search(n1, t1))
# print('RESULT :', search(n2, t2))
# print('RESULT :', search(n3, t3))
# print('RESULT :', search(n4, t4))
# print('RESULT :', search(n5, t5))
# print('RESULT :', search(n6, t6))
# print('RESULT :', search(n7, t7))
# print('RESULT :', search(n8, t8))