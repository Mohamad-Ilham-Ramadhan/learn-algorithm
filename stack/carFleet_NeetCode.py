'''
   (stack) leetcode: 853. Car Fleet (medium)

   There are n cars going to the same destination along a one-lane road. The destination is `target` miles away.

   You are given two integer array `position` and `speed`, both of length `n`, where `position[i]` is the position of the `ith` car and `speed[i]` is the speed of the `ith` car (in miles per hour).

   A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

   A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

   If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

   Return the number of car fleets that will arrive at the destination.

   

   Example 1:
      Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
      Output: 3
      Explanation:
      The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
      The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
      The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
      Note that no other cars meet these fleets before the destination, so the answer is 3.

   Example 2:
      Input: target = 10, position = [3], speed = [3]
      Output: 1
      Explanation: There is only one car, hence there is only one fleet.

   Example 3:
      Input: target = 100, position = [0,2,4], speed = [4,2,1]
      Output: 1
      Explanation:
      The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
      Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
   

   Constraints:
      - n == position.length == speed.length
      - 1 <= n <= 10^5
      - 0 < target <= 10^6
      - 0 <= position[i] < target
      - All the values of position are unique.
      - 0 < speed[i] <= 106

   Related Topics:
      (Array) (Stack) (Sorting) (Monotonic Stack)

   ==========================================================================

   Solution by NeetCode
   
   LeetCode submission: 
      runtime: 1059 ms, beats 20.76%
      memory: 36.3 MB, beats 75.99%
   

'''
def carFleet(target, position, speed):
   pair = [[p,s] for p, s in zip(position, speed)]

   stack = [] 
   for p, s in sorted(pair)[::-1]: # Reverse sorted order 
      stack.append( (target - p) / s)
      if len(stack) >= 2 and stack[-1] <= stack[-2]: 
         stack.pop()
   
   return len(stack)

t1 = 12; p1 = [10,8,0,5,3]; s1 = [2,4,1,1,3] 
t2 = 10; p2 = [3]; s2 = [3]
t3 = 100; p3 = [0,2,4]; s3 = [4,2,1]
t4 = 14; p4 = [10,8,0,5,3,7,6]; s4 = [2,4,1,1,3,5,6]
t5 = 14; p5 = [8,0,5,3,7,6,10]; s5 = [4,1,1,3,5,6,2]
t6 = 10; p6 = [9,8,7,6]; s6 = [4,5,3,4] # 3
t7 = 12; p7 = [10,8,6]; s7 = [1,12,3] # 2
t8 = 10; p8 = [0,4,2]; s8 = [2,1,3] # 1,
t9 = 21; p9 = [1,15,6,8,18,14,16,2,19,17,3,20,5]; s9 = [8,5,5,7,10,10,7,9,3,4,4,10,2] # 7, output 8
# print('RESULT :', carFleet2(21, [20,19], [10,20]))


