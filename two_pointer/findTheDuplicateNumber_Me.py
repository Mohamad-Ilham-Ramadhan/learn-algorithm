'''
   (linked list) leetcode: 287. Find the Duplicate Number (medium)

   Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

   There is only one repeated number in `nums`, return this repeated number.

   You must solve the problem without modifying the array `nums` and uses only constant extra space.


   Example 1:
      Input: nums = [1,3,4,2,2]
      Output: 2

   Example 2:
      Input: nums = [3,1,3,4,2]
      Output: 3
   

   Constraints:
      - 1 <= n <= 10^5
      - nums.length == n + 1
      - 1 <= nums[i] <= n
      - All the integers in `nums` appear only once except for precisely one integer which appears two or more times.

      
   Follow up:
      - How can we prove that at least one duplicate number must exist in nums?
      - Can you solve the problem in linear runtime complexity?

   Related Topics:
      (Array) (Two Pointers) (Binary Search) (Bit Manipulation)
   
   =======================================================================

   Solution by myself:
      using set to store number 
      and check if there is number in the set then return the duplicate number 
   
   Leetcode submission: 
      runtime: 587 ms, beats 93.24%
      memory: 32.4 MB, beats 21.24%
'''

# attempt #1: time O(n) space O(n)
def findDuplicate(nums):
   s = set()
   for n in nums: 
      if n in set: 
         return n 
      s.add(n)


n1 = [1,3,4,2,2]
n2 = [2,2,2,2,2]

print('RESULT :', findDuplicate(n1))