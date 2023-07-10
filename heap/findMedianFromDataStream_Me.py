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
      create list of num
      binary search addition 
   
   leetcode submission: 
      runtime: 1608 ms, beats 10.16%
      memory: 38.4 MB, beats 53.16%

'''
class MedianFinder:

   def __init__(self):
      self.sl = [] # sorted list

   # O(log n)
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

   # O(1)
   def findMedian(self) -> float:
      mid = self.len(self.sl) // 2
      if len(self.sl) % 2: # odd 
         return float(self.sl[mid])
      else: # even 
         return (self.sl[mid - 1] + self.sl[mid]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

mf = MedianFinder() 
mf.addNum(5)
mf.addNum(1)
mf.addNum(3)
mf.addNum(8)
mf.addNum(12)
print('list', mf.list)