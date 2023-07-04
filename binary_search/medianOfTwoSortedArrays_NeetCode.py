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

   Solution by NeetCode: 

   Leetcode submission: 
      runtime: 91 ms, beats 98.35% 
      memory: 16.6 MB, beats 76.30%
'''

'''
   A=[4,5,6,12,13] B=[1,2,3,7,10,11]  # 6

'''
   

def findMedianSortedArrays(nums1, nums2):
   A, B = nums1, nums2 
   total = len(nums1) + len(nums2)
   half = total // 2

   if len(B) < len(A): 
      A, B = B, A 
   
   l, r = 0, len(A) - 1 
   while True: 
      i = (l + r) // 2 # A
      j = half - i - 2 # B

      Aleft = A[i] if i >= 0 else float('-inf')
      Aright = A[i+1] if (i+1) < len(A) else float('inf')
      Bleft = B[j] if j >= 0 else float('-inf')
      Bright = B[j+1] if (j+1) < len(B) else float('inf')
      
      # partition is correct
      if Aleft <= Bright and Bleft <= Aright:
         # odd 
         if total % 2: 
            return min(Aright, Bright)
         # even
         return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
      elif Aleft > Bright:
         r = i - 1 
      else: 
         l = i + 1

n11 = [1,3]; n21 = [2] # 2.000 
n12 = [1,2]; n22 = [3,4] # 2.5
n13 = [1,3,5,7]; n23 = [2,4,6] # 4
n14 = [1,3,5,7]; n24 = [2,10,24] # 5
n15 = [5,50,100]; n25 = [2,3,4,51,66,77]
n16 = []; n26 = [1]
n17 = [1,3]; n27 = [2,4,5]
n18 = [2,3]; n28 = [1,4,5,6]

print(findMedianSortedArrays(n11,n21)) #
# print('infinity', float('inf') > 10000)
