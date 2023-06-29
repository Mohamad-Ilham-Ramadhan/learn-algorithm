'''
   (stack) leetcode: 84. Largest Rectangle in Histogram (hard)

   Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

   Example 1:
               [ ]                     [ ]                  
            [ ][ ]                  [ 10 ]      
            [ ][ ]                  [    ]      
            [5][6]   [ ] --->       [    ]   [ ]
      [2]   [ ][ ][2][3]      [2]   [    ][2][3]
      [ ][1][ ][ ][ ][ ]      [ ][1][    ][ ][ ]

      Input: heights = [2,1,5,6,2,3]
      Output: 10
      Explanation: The above is a histogram where width of each bar is 1.
      The largest rectangle is shown in the red area, which has an area = 10 units.

   Example 2:
         [ ]         [ ]
         [ ]         [ ]
      [2][4] ---> [  4 ]
      [ ][ ]      [    ]

      Input: heights = [2,4]
      Output: 4
   

   Constraints:
      - 1 <= heights.length <= 10^5
      - 0 <= heights[i] <= 10^4

   Related Topics:
      (Array) (Stack) (Monotonic Stack) 

   ============================================================ 

   Solution by Myself:
      use stack and hashmap

   Leetcode submission: 
      runtime: 976 ms, beats 36.87%
      memory: 31.3 MB, beats 55.76%

'''
def largestRectangleArea(heights):
   result = heights[0]
   stack = [0] # height's index
   m = {} # index: left volume
   for i in range(1, len(heights)): 
      # print('loop stack', stack)
      h = heights[i]
      ph = heights[i - 1] # prev current height
      if h < ph: 
         while len(stack) > 0: 
            j = stack[len(stack) - 1]
            hj = heights[j]
            # print('hj', hj)
            if hj < h:
               # print('add left volume break the stack loop') 
               m[i] = ((i - j) - 1) * h
               break
            volumeJtoCurrent = (i - j) * hj
            if j in m: 
               result = max(result, m[j] + volumeJtoCurrent)
            else:   
               result = max(result, volumeJtoCurrent)

            stack.pop()
         
         if len(stack) == 0: 
            m[i] = i * h
            result = max(result, (i+1) * h)
      
      stack.append(i)

   # print('stack remain', stack, '\n')
   # print('left volume map', m)
   # calculate volumne in stack remain 
   for i in stack: 
      h = heights[i]
      volumeFromItoLast = h * (len(heights) - i)
      # print('h', h, volumeFromItoLast)
      if i in m: 
         result = max(result, m[i] + volumeFromItoLast)
      else:
         result = max(result, volumeFromItoLast)
   
   return result

hh = [1,2,4,5,6,3,4,5,6,3] # 24
'''      
               [6]         [6]
            [5][ ]      [5][ ]
         [4][ ][ ]   [4][ ][ ]
         [ ][ ][ ][3][ ][ ][ ][3]
      [2][ ][ ][ ][ ][ ][ ][ ][ ]
   [1][ ][ ][ ][ ][ ][ ][ ][ ][ ] 

   result = max(12, 6, 10, 12)
   [[1,0,0],[2,0,0],[3,9,0],[4,0,0],[5,0,0],[6,0,0],[3,0,0]]
'''
h3 = [2,2,5,6,2,3] # 12
h1 = [2,1,5,6,2,3] # 10
'''
               [ ]                     [ ]                  
            [ ][ ]                  [ 10 ]      
            [ ][ ]                  [    ]      
            [5][6]   [ ] --->       [    ]   [ ]
      [2]   [ ][ ][2][3]      [2]   [    ][2][3]
      [ ][1][ ][ ][ ][ ]      [ ][1][    ][ ][ ]

   if next <= than current don't add current
[i,h,v]
[0,1,6]  [2,2,6] [5,3,3]
'''
h2 = [2,4] # 4
'''
   if next <= than current don't add current
   if height same choose the lowest index

   [i,h,v]

   [0,2,10] [2,2,6] []
'''
h4 = [3,3,7,7,7,3] # 21
'''
   next < cannot replace
   next >= replace
   [0,3,15] [2,7,21] [5,3,3]
'''
h5 = [5,2,7,7,8,5,3,9,5,1,8] # 21
'''
   keep up current height largest so there is no unecessary lower volume with same height
   [1,1,11] [10,8,8]
   res -> max() = 21
'''
h6 = [1,2,3,4,5,6,7,8,9,10] # 30
'''
   [0,1,10] [1,2,18] [2,3,24] [3,4,28] [4,5,30] [5,6,30] [6,7,28] [7,8,24] [8,9,18] [9,10,10]
   res -> max() = 30
'''
h7 = [10,9,8,7,6,5,4,3,2,1] # 30
'''
   [10]
   [  ][9] 
   [  ][ ][8] 
   [  ][ ][ ][7] 
   [  ][ ][ ][ ][6] 
   [  ][ ][ ][ ][ ][5] 
   [  ][ ][ ][ ][ ][ ][4] 
   [  ][ ][ ][ ][ ][ ][ ][3] 
   [  ][ ][ ][ ][ ][ ][ ][ ][2] 
   [  ][ ][ ][ ][ ][ ][ ][ ][ ][1]
'''
h8 = [970,741,652,369,530,775,793,421,341,446,626] # 3751
import time
startTime = time.time()
print('RESULT: ', largestRectangleArea(h7)) # 
t = time.time() - startTime
print('%s: %.3f' % ('runtime', t))