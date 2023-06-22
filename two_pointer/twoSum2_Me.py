'''
   (two pointer) leetcode: 167. Two Sum II - Input Array Is Sorted (medium)

   Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 < numbers.length`.

   Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

   The tests are generated such that there is exactly one solution. You may not use the same element twice.

   Your solution must use only constant extra space.

   

   Example 1:
      Input: numbers = [2,7,11,15], target = 9
      Output: [1,2]
      Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

   Example 2:
      Input: numbers = [2,3,4], target = 6
      Output: [1,3]
      Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

   Example 3:
      Input: numbers = [-1,0], target = -1
      Output: [1,2]
      Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
      

   Constraints:
      - 2 <= numbers.length <= 3 * 104
      - -1000 <= numbers[i] <= 1000
      - numbers is sorted in non-decreasing order.
      - -1000 <= target <= 1000
      - The tests are generated such that there is exactly one solution.

   Solution by myself
      using hashmap. O(n * 2) simplified O(n)

   Leetcode submission:
      #1
         runtime: 137 ms, beats 73.85%
         memory: 17.3 MB, beats 17.63%
'''
# attempt 1 using hasmap. O(n * 2)
def twoSum(numbers, target):
   map = {} 
   for i in range(len(numbers)):
      map[numbers[i]] = i

   for i in range(len(numbers)):
      n = numbers[i]
      if target - n in map: 
         print('we find it', i, map[target - n])
         return [i + 1, map[target - n] + 1]

n1 = [2,7,11,15]; t1 = 9 # [1,2]
n2 = [2,3,4]; t2 = 6 # [1,3]
n3 = [-1,0]; t3 = -1 # [1,2]

print('RESULT :', twoSum(n3, t3))
