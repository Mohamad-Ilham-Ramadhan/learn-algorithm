'''
   (Greedy) leetcode: 53. Maximum Subarray (medium)

   Given an integer array `nums`, find the subarray with the largest sum, and return its sum.
   

   Example 1:
      Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
      Output: 6
      Explanation: The subarray [4,-1,2,1] has the largest sum 6.

   Example 2:
      Input: nums = [1]
      Output: 1
      Explanation: The subarray [1] has the largest sum 1.

   Example 3:
      Input: nums = [5,4,-1,7,8]
      Output: 23
      Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
   

   Constraints:
      - 1 <= nums.length <= 105
      - -104 <= nums[i] <= 104
   

   Follow up: 
      If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

   ===============================================================
   
   Solution by myself:
      base case is greedy[0] = [nums0] and result = nums[0]

      loop over nums:
         gd0 = max of ...greedy[0] + nums[i]
         greedy[i] = [gd0, nums[i]]
         result = max(result, gd0, n)
      
      return result

   Leetcode submission:
      attempt #1
         runtime: 1047 ms, beats 5.1%
         memory: 35.1 MB, beats 15%
      
      attempt #2 
         runtime: 913 ms, beats 5.1%
         memory: 30.6 MB, beats 78.17%

'''
# attempt #2
def maxSubArray(nums):
    if len(nums) == 1: return nums[0]

    greedy = [nums[0]]
    res = nums[0]

    for i in range(1, len(nums)): 
        n = nums[i]
        gd0 = float('-inf')
        for gdn in greedy: 
            gd0 = max(gd0, gdn + n)

        res = max(res, gd0, n)
        greedy = [gd0, n] 

    return res

'''
    [-2,1,-3,4,-1,2,1,-5,4]
    [-1, 1] [-2, -3] [2, 4] [3, -1] [5, 2] [6, 1] [1, -5] [5, 4]

    [5,4,-1,7,8]
    [5] [9, 4] [8, -1] [15, 7] [23, 8]

    [-2, -4, -1, -3]
    [-2] [-6, -4] [-5, -1] [-4, -3]
'''
# attempt #1
def maxSubarray(nums): 
    if len(nums) == 1: return nums[0]

    greedy = [float('-inf')] * len(nums)
    greedy[0] = [nums[0]]
    res = nums[0]
    print('greedy', greedy)

    for i in range(1, len(nums)): 
        print('i', i, 'prev greedy', greedy[i-1])
        n = nums[i]
        gd = greedy[i-1]
        gd0 = float('-inf')
        for gdn in gd: 
            gd0 = max(gd0, gdn + n)
        greedy[i] = [gd0, n] 
        print('res', res, 'gd0', gd0, 'n', n)
        res = max(res, gd0, n)

    return res

n1 = [-2,1,-3,4,-1,2,1,-5,4] # expect: 6
n2 = [1] # expect: 1
n3 = [5,4,-1,7,8] # expect: 23
n4 = [-2,-4,-1,-3] # expect: -1
n5 = [-1,-2] # expect: -1, output -2

print('RESULT :', maxSubarray(n5))
'''
    [-2,1,-3,4,-1,2,1,-5,4]
    [-1, 1] [-2, -3] [2, 4] [3, -1] [5, 2] [6, 1] [1, -5] [5, 4]

    [5,4,-1,7,8]
    [5] [9, 4] [8, -1] [15, 7] [23, 8]

    [-2, -4, -1, -3]
    [-2] [-6, -4] [-5, -1] [-4, -3]
'''