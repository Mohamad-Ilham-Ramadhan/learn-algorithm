'''
   (binary search): 4. median of two sorted arrays (hard)

   Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

   The overall run time complexity should be O(log (m+n)).


   Example 1:
      Input: nums1 = [1,3], nums2 = [2]
      Output: 2.00000
      Explanation: merged array = [1,2,3] and median is 2.

   Example 2:
      Input: nums1 = [1,2], nums2 = [3,4]
      Output: 2.50000
      Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
   

   Constraints:
      - nums1.length == m
      - nums2.length == n
      - 0 <= m <= 1000
      - 0 <= n <= 1000
      - 1 <= m + n <= 2000
      - -10^6 <= nums1[i], nums2[i] <= 10^6

   Related Topics: 
      (Array) (Binary Search) (Divide and Conquer)
   
   ===============================================

   Solution by Myself: 
      merge sort O(n+m)

   Leetcode submission: 
      runtime: 118 ms, beats 14.96% 
      memory: 16.8 MB, beats 10.92%
'''

'''

   A=[4,5,6,12,13] B=[1,2,3,7,10,11]  # 6

'''
# O(n+m)
def findMedianSortedArrays(nums1, nums2):
   st = [] # sorted

   # merge sort
   while len(nums1) and len(nums2): 
      if nums1[-1] >= nums2[-1]:
         st.append(nums1.pop())
      else: 
         st.append(nums2.pop())
   nums = nums1 if len(nums1) else nums2 
   while len(nums): 
      st.append(nums.pop())
   
   mid = len(st) // 2
   if len(st) % 2: # odd
      return float(st[mid])
   else: # even 
      return (st[mid-1] + st[mid])/2

n11 = [1,3]; n21 = [2] # 2.000 
n12 = [1,2]; n22 = [3,4] # 2.5
n13 = [1,3,5,7]; n23 = [2,4,6] # 4
n14 = [1,3,5,7]; n24 = [2,10,24] # 5
n15 = [5,50,100]; n25 = [2,3,4,51,66,77]
n16 = []; n26 = [1]
n17 = [1,3]; n27 = [2,4,5]
n18 = [2,3]; n28 = [1,4,5,6]

print(findMedianSortedArrays(n17,n27)) #