''' 
   (heap) leetcode: 215. Kth Largest Element in an Array (medium). Companies (Microsoft)

   Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

   Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

   Can you solve it without sorting?

   

   Example 1:
      Input: nums = [3,2,1,5,6,4], k = 2
      Output: 5

   Example 2:
      Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
      Output: 4
   

   Constraints:
      - 1 <= k <= nums.length <= 105
      - -104 <= nums[i] <= 104

   Related topics:
      (Array) (Divide and conquer) (Sorting) (Heap (Priority Queue)) (Quickselect)

   ===========================================================================================

   Solution by Neetcode:
      QuickSelect algorithm: avarage time O(n), worst time O(n^2)

   Leetcode submission: 
      runtime: 538 ms, beats 57.23%
      memory: 30.1 MB, beats 30.38%
'''
def findKthLargest(nums, k):
   k = len(nums) - k 

   def quickSelect(l, r): 
      pivot, p = nums[r], l 
      for i in range(l, r): 
         if nums[i] <= pivot: 
            nums[p], nums[i] = nums[i], nums[p]
            p += 1
      nums[p], nums[r] = nums[r], nums[p]

      if p > k: return quickSelect(l, p - 1)
      elif p < k: return quickSelect(p + 1, r)
      else: return nums[p]