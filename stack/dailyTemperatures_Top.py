'''
   (stack) leetcode: 739. Daily Temperatures (medium)

   Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

 

   Example 1:
      Input: temperatures = [73,74,75,71,69,72,76,73]
      Output: [1,1,4,2,1,1,0,0]

   Example 2:
      Input: temperatures = [30,40,50,60]
      Output: [1,1,1,0]

   Example 3:
      Input: temperatures = [30,60,90]
      Output: [1,1,0]

   
   Constraints:
      - 1 <= temperatures.length <= 105
      - 30 <= temperatures[i] <= 100

   ===============================================================

   Solution by top answer/solution

   Leetcode submission:
      runtime: 1244 ms, beats 99.87%
      memory: 30.5 MB, beats 76.91%

'''

def dailyTemperatures(temperatures):
   n = len(temperatures)
   hottest = 0 
   out = [0] * n 

   for curr_d in range(n-1, -1, -1):
      curr_t = temperatures[curr_d]
      print('out', out, 'curr_t', curr_t)
      if curr_t >= hottest: 
         hottest = curr_t
         continue 

      check_d = curr_d + 1 
      print('temperatures[check_d]', temperatures[check_d])
      while temperatures[check_d] <= curr_t:
         print('check_d before', check_d, 'out[check_d]', out[check_d])
         check_d += out[check_d]
         print('check_d after', check_d)
      out[curr_d] = check_d - curr_d
   return out
t1 = [73,74,75,71,69,72,76,73] # [1,1,4,2,1,1,0,0]
t2 = [30,40,50,60] # [1,1,1,0]
t3 = [30,60,90] # [1,1,0]
t4 = [30,29,28,27,26,25,24,23,22,23,24,25,26,27,28,29,30,31]
'''
   [76,73]
'''
import time
start = time.time()
print('RESULT :', dailyTemperatures(t1))
# print(len(t5))
# time.sleep(1)
t = time.time() - start
print('%s: %.3f' % (666, t))
