'''
    leetcode: 152. Maximum Product Subarray (medium)

    Given an integer array `nums`, find a subarray that has the largest product, and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.



    Example 1:
        Input: nums = [2,3,-2,4]
        Output: 6
        Explanation: [2,3] has the largest product 6.

    Example 2:
        Input: nums = [-2,0,-1]
        Output: 0
        Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


    Constraints:
        - 1 <= nums.length <= 2 * 104
        - -10 <= nums[i] <= 10
        - The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    Solution by NeetCode:
        keep the min and max at dp[i]
    
    Leetcode submission:
        runtime: 101 ms, beats 33.96% 
        memory: 17 MB, beats 23.95%
'''

# attempt #1
def maxProduct(nums):
    res = max(nums)
    curMin, curMax = 1,1 

    for n in nums: 
        if n == 0: 
            curMin, curMax = 1, 1
            continue 
        tmp = curMax * n 
        curMax = max(tmp, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res

n1 = [2,3,-2,4] # expect: 6
n2 = [-2,0,-1]  # expect: 0
n3 = [-1,2,-1,8] # expect: 16
n4 = [-2,-3,-1,-5,-10,-6,-7] # expect: 6300
n5 = [-2,10,2,1,-3] # expect: 120
n6 = [-3] # expect: -3
n7 = [2,-5,-2,-4,3] # expect: 24, output: 20
n8 = [0,2] # expect: 2, output: 0
n9 = [0,-4,9,-2] # expect: 72
n10 = [0,-4,9,-2,9,-1] # expect: 648
n11 = [1,2,-4,0,8,3] # expect: 24
# print('RESULT: ', maxProduct(n7))

print(max(*[12,3,666,4,5], 100))
'''
    [1,2,-4,0,8,3]
    [1] [2] [-8] [0] [8] [24]

    [0,-4,9,-2,9,-1]
    [0] [-4]

    [0,-4,9,-2]
    [0] [0,-4] [0, -36] [0, 72]

    [2,-5,-2,-4,3]
    [2] [-10] [20,-2] [-80, 8]

    [2,3,-2,4]
    [6] [-12, -2] [-8, 4]
    [-6] [3, -6] [6, -12]

    [-1,2,-1,8]
    [-2, 2] [2, -2] [16]

    [-2,10,2,1,-3]
    120
    [-2] [-20, 10] [-40, 20] [-40, 20] [120, -60]

    [-2,-3,-1,-5,-10,-6,-7]
    12600
    [-2] [6, -3] [-6, 3] [30, -15] [-300, 150] [1800, -900] [-12600, 6300]
'''
arr = [4,5,11,3,7,1,2,3]
arr2 = [77,999,33]
print('zero == minus zero', 0 == -0)