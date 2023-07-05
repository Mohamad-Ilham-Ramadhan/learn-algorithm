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

   Solution by neetcode
   
   Leetcode submission: 
      runtime: 593 ms, beats 89.33%
      memory: 31 MB, beats 83.9%
'''

# attempt #1: time O(n) space O(1)
def findDuplicate(nums):
   slow, fast = 0, 0 
   while True: 
      slow = nums[slow]
      fast = nums[nums[fast]]
      if slow == fast:
         break 
   
   slow2 = 0 
   while True:
      slow = nums[slow]
      slow2 = nums[slow2]
      if slow == slow2: 
         return slow

n1 = [1,3,4,2,2]
n2 = [2,2,2,2,2]

print('RESULT :', findDuplicate(n1))

'''
   slow 3
   fast 3
'''