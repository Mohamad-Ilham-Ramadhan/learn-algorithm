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

   Leetcode submission: 
      runtime: 538 ms, beats 57.23%
      memory: 30.1 MB, beats 30.38%
'''
# using heap: time O((n+k) log(n+k))
from heapq import heapify, heappush, heappop
def findKthLargest(nums, k):
   hp = []
   heapify(hp) 
   for n in nums:
      heappush(hp, -n)
   for i in range(k-1):
      heappop(hp)
   return -hp[0]