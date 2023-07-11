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

   Solution by NeetCode:
      using min heap and max heap 
      max heap for the left part 
      min heap for the right part
   
   leetcode submission: 
      runtime: 541 ms, beats 40.64%
      memory: 38.9 MB, beats 12.29%

'''
from heapq import heapify, heappush, heappop
class MedianFinder:

   def __init__(self):
      self.small, self.large = [], []
   def addNum(self, num: int) -> None:
      heappush(self.small, -1 * num)

      # make sure every num in small is <= every num in large 
      if self.small and self.large and (-1 * self.small[0]) > self.large[0]: 
         val = -1 * heappop(self.small)
         heappush(self.large, val)
      
      # uneven size?
      if len(self.small) > len(self.large) + 1: 
         val = -1 * heappop(self.small)
         heappush(self.large, val)
      if len(self.large) > len(self.small) + 1: 
         val = heappop(self.large)
         heappush(self.small, -1 * val)

   def findMedian(self) -> float:
      if len(self.small) > len(self.large): 
         return -1 * self.small[0]
      if len(self.large) > len(self.small): 
         return self.large[0]

      return (-1 * self.small[0] + self.large[0]) / 2
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
mf = MedianFinder() 
mf.addNum(1)
mf.addNum(2)
print('medi', -mf.maxH[0], mf.minH[0])
print('medi', len(mf.maxH), len(mf.minH) )
print('median [1,2]', mf.findMedian())
mf.addNum(3)
print('medi', -mf.maxH[0], mf.minH[0])
print('medi', len(mf.maxH), len(mf.minH) )
print('median [1,2]', mf.findMedian())
