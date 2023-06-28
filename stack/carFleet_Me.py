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

   Solution by myself:
      make list of cars [position, its speed]
      sort -> large to small

      result = 1

      loop sorted cars start with index of 1

      use two pointer to compare prev and current speed 
      calculate car's steps to finish (lower is faster)

      if current cars steps > prev cars steps :
         then current cars never catch up (add result +1)
         prev cars index = current cars index
   
   LeetCode submission: 
      #1 fail 
      #2 (carFleet2)
         runtime: 896 ms, beats 80.45%
         memory: 36 MB, beats 86.30%
   

'''
# fail
def carFleet(target, position, speed):

   # sort car position based on position and make each element [pos, index of speed]
   cars = [[position[i], speed[i]] for i in range(len(position))]
   cars.sort(key=lambda c: c[0], reverse=True)
   # move car and regroup and check is finished
   x = 1
   result = 1
   while x < 4 and len(cars) > 1:
      x += 1
      newCars1 = []
      print('start cars', cars)
      for i in range(len(cars)):
         c = cars[i]
         print('c',c)
         if c[0] >= target: 
            result += 1
            continue
         cars[i] = [c[0] + c[1], c[1]]
         print('cars[i]',cars[i])
         if cars[i][0] > target: 
            result += 1
            continue 
         newCars1.append(cars[i])

      # check fleet 
      newCars2 = []
      print('check fleet newCars1', newCars1)
      l = 0 # new cars last
      for r in range(1, len(newCars1)):
         cl = newCars1[l]
         cr = newCars1[r]
         if cr[0] >= cl[0]: 
            if cr[1] < cl[1]:
               l = r 
         else:
            newCars2.append(cl) 
            l = r
         print('cl', cl,'cr', cr)
      
      print('end', 'cl', cl,'cr', cr)
      if cr[0] >= cl[0]: 
         if cr[1] < cl[1]:
            newCars2.append(cr) 
         else:
            newCars2.append(cl) 
      else: 
         newCars2.append(cr)
      print('newCars2', newCars2, 'result', result)
      cars = newCars2
      print('====================== \n')
               
   return result

# success
def carFleet2(target, position, speed): 
   # sort car position based on position and make each element [pos, index of speed]
   cars = [[position[i], speed[i]] for i in range(len(position))]
   cars.sort(key=lambda c: c[0], reverse=True)
   print('cars', cars)
   result = 1 
   j = 0
   for i in range(1, len(cars)):
      print('-------------')
      cj = cars[j]
      ci = cars[i]
      ciSteps = (target - ci[0]) / ci[1]
      cjSteps = (target - cj[0]) / cj[1]
      print('ci', ci, 'cjSteps', cjSteps, 'ciSteps', ciSteps, (target - ci[0]))
      if ciSteps > cjSteps: 
         print('add 1')
         j = i
         result += 1

   return result

t = 11; p = [10,8,0,5,3]; s = [2,4,1,1,3] 
t1 = 12; p1 = [10,8,0,5,3]; s1 = [2,4,1,1,3] 
'''
   [[10, 2], [8, 4], [5, 1], [3, 3], [0, 1]]
   [  [1],    [1],     [7],   [3],      [12] ]
'''
t2 = 10; p2 = [3]; s2 = [3]
t3 = 100; p3 = [0,2,4]; s3 = [4,2,1]
t4 = 14; p4 = [10,8,0,5,3,7,6]; s4 = [2,4,1,1,3,5,6]
'''
   [[10, 2], [8, 4], [7, 5], [6, 6], [5, 1], [3, 3], [0, 1]]
   [  [2],    [1.5],  [1.4],  [1.3],   [9],   [3.6],  [14]]
'''
t5 = 14; p5 = [8,0,5,3,7,6,10]; s5 = [4,1,1,3,5,6,2]
t6 = 10; p6 = [9,8,7,6]; s6 = [4,5,3,4] # 3
t7 = 12; p7 = [10,8,6]; s7 = [1,12,3] # 2
t8 = 10; p8 = [0,4,2]; s8 = [2,1,3] # 1,
t9 = 21; p9 = [1,15,6,8,18,14,16,2,19,17,3,20,5]; s9 = [8,5,5,7,10,10,7,9,3,4,4,10,2] # 7, output 8
'''
[[4, 1], [2, 3], [0, 2]]
   [5]    [5]

   []
   res = 8
'''
print('RESULT :', carFleet2(21, [20,19], [10,20]))
