'''
   (heap) leetcode: 295. Find Median from Data Stream (hard). Companies (microsoft)

   The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

      - For example, for arr = [2,3,4], the median is 3.
      - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

   Implement the MedianFinder class:

      - MedianFinder() initializes the MedianFinder object.
      - void addNum(int num) adds the integer num from the data stream to the data structure.
      - double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
   

   Example 1:
      Input
         ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
         [[], [1], [2], [], [3], []]
      Output
         [null, null, null, 1.5, null, 2.0]

      Explanation
         MedianFinder medianFinder = new MedianFinder();
         medianFinder.addNum(1);    // arr = [1]
         medianFinder.addNum(2);    // arr = [1, 2]
         medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
         medianFinder.addNum(3);    // arr[1, 2, 3]
         medianFinder.findMedian(); // return 2.0
   

   Constraints:
      - -10^5 <= num <= 10^5
      - There will be at least one element in the data structure before calling findMedian.
      - At most 5 * 10^4 calls will be made to addNum and findMedian.
   

   Follow up:
      - If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
      - If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
   
   ===================================================================================================================

   Solution by myself:
      # solution 1
      create list of num
      binary search addition 

      # solution 2 (after see a hint from neetcode)
         using min heap and max heap 
         max heap for the left part 
         min heap for the right part
   
   leetcode submission: 
      solution #1
         runtime: 1608 ms, beats 10.16%
         memory: 38.4 MB, beats 53.16%
      solution #2
         runtime: 466 ms, beats 95.49%
         memory: 38.3 MB, beats 53.16%

'''
from heapq import heapify, heappush, heappop
class MedianFinder:

   def __init__(self):
      self.sl = [] # sorted list

   def addNum(self, num: int) -> None:
      if len(self.sl):
         # binaryAdd 
         l = 0 
         r = len(self.sl) - 1 
         while l <= r: 
            m = (l+r) // 2
            if num >= self.sl[m]:
               l = m + 1
            else: 
               r = m - 1
         self.sl.insert(l, num)
      else: 
         self.sl.append(num)

   def findMedian(self) -> float:
      if len(self.sl) % 2: # odd 
         return float(self.sl[self.len(self.sl) // 2])
      else: # even 
         mid = self.len(self.sl) // 2
         return (self.sl[mid - 1] + self.sl[mid]) / 2


class MedianFinder2:

   def __init__(self):
      self.maxH = [] # the left part
      self.minH = [] # the right part
      heapify(self.maxH); heapify(self.minH)

   # O(log n) * 2
   def addNum(self, num: int) -> None:
      if len(self.maxH) == 0: heappush(self.maxH, -num); return;

      if num <= -self.maxH[0]:
         heappush(self.maxH, -num)
         if (len(self.maxH) - len(self.minH)) > 1: 
            popped = -heappop(self.maxH)
            heappush(self.minH, popped)
      # elif num <= self.minH[0]: 
      else:
         heappush(self.minH, num)
         if len(self.minH) > len(self.maxH): 
            popped = heappop(self.minH)
            heappush(self.maxH, -popped)

   # O(1)
   def findMedian(self) -> float:
      if len(self.maxH) > len(self.minH): # Odd
         return -float(self.maxH[0])
      else: 
         return (-self.maxH[0] + self.minH[0]) / 2 # Even
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# mf = MedianFinder2() 
# mf.addNum(-5)
# mf.addNum(5)
# mf.addNum(0)
# mf.addNum(5)
# mf.addNum(1)
# mf.addNum(3)
# mf.addNum(9)
# mf.addNum(-10)
# mf.addNum(4)
# mf.addNum(-1)
# mf.addNum(3)
# print('medi', -mf.maxH[0], mf.minH[0])
# print('medi', len(mf.maxH), len(mf.minH) )
# print('result :', mf.findMedian())

'''
   [-10, -5, -1, 0, 1, (3), 3, 4, 5, 5, 9]
   [-5,5,0,5,1,3,9,-10,4,-1,3]
   [-10,-5,-1,0,1,3] [3,4,5,5,9]

   [-5, -3, -3, 1, 2, (4), 6, 7, 8, 9, 10]
   [8,-3,10,7,9,2,1,-3,4,-5,6]
   [-5,-3,-3,1,2,4] [6,7,8,9,10]

   [-5, -4, -3, 0, 3, (3), 3, 5, 5, 6, 6]
   [3,5,-4,-3,3,6,6,-5,3,5,0,]
   [-inf,3] [inf]
'''
mf = MedianFinder2() 
mf.addNum(1)
mf.addNum(2)
print('medi', -mf.maxH[0], mf.minH[0])
print('medi', len(mf.maxH), len(mf.minH) )
print('median [1,2]', mf.findMedian())
mf.addNum(3)
print('medi', -mf.maxH[0], mf.minH[0])
print('medi', len(mf.maxH), len(mf.minH) )
print('median [1,2]', mf.findMedian())
