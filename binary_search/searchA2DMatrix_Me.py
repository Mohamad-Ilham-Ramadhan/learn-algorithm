'''
   (binary search) leetcode: 74. Search a 2D Matrix (medium)
   
   You are given an `m x n` integer matrix `matrix` with the following two properties:
      - Each row is sorted in non-decreasing order.
      - The first integer of each row is greater than the last integer of the previous row.

   Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

   You must write a solution in `O(log(m * n))` time complexity.

   

   Example 1:
      Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
      Output: true

   Example 2:
      Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
      Output: false
   

   Constraints:
      - m == matrix.length
      - n == matrix[i].length
      - 1 <= m, n <= 100
      - -10^4 <= matrix[i][j], target <= 10^4
   
   Related Topics: 
      (Array) (Binary Search) (Matrix)
   
   ====================================================

   Solution by myself: 
   
   leetcode runtime: 
      runtime: 67 ms, beats 16.18%,
      memory: 16.9, beats 63.91%
'''  

def searchMatrix(matrix, target): 
   cols = len(matrix[0]) 
   rows = len(matrix)
   totalLength = cols * rows

   l = 0 
   r = totalLength - 1
   while l <= r: 
      print('l', l, 'r', r)
      mid = (l + r) // 2
      print('mid', mid)
      midRow = mid // cols
      midN = float('inf')
      if midRow == 0:
         midN = matrix[midRow][mid]
         pass
      else:
         midCol = mid % (midRow * cols)
         midN = matrix[midRow][midCol]

      if target > midN: 
         l = mid + 1
      elif target < midN: 
         r = mid - 1
      else: 
         return True
      print('midN', midN)
   return False
m1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; t1 = 3 # true
m2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; t2 = 13 # false 
m3 = [[2]]; t3 = 3 # false 
m4 = [[1,2,3,4,5]]; t4 = 4 # True
m5 = [[2]]; t5 = 2 # True 
m6 = [[2]]; t6 = 1 # False 
print('RESULT: ', searchMatrix(m3, t3))