'''
    (2D dynamic programming) Leetcode: 300. Longest Increasing Subsequence (medium)

    Link: https://leetcode.com/problems/longest-increasing-subsequence/

    Tags: Array, Binary Search, Dynamic Programming

    Constraints:
        - 1 <= nums.length <= 2500
        - -10^4 <= nums[i] <= 10^4

    ======================================================================

    Submissions: 
        runtime: 2423 ms, beats 63.73%
        memory: 16.82 MB, beats 10.41%

'''

def lengthOfLIS(nums):
    dp = [1] * len(nums)
    result = 1
    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(dp)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])

        result = max(result, dp[i])
    print('dp', dp)
    return result

n2 = [0,1,0,3,2,3] # 4
n3 = [7,7,7,7,7,7,7] # 1
n4 = [-10,4,0,3,-1,8,-4,-2,3,6] # 5
n7 = [1,2,6,5,4,3,2,1] # 3
n1 = [10,9,2,5,3,7,101,18] # 4
n6 = [1,2,3,4,5,6,1,2,3,7,4,5,8,9] # 9 (1,2,3,4,5,6,7,8,9)
n5 = [1,2,3,7,4,5,8,9] # 7
print('RESULT: ', lengthOfLIS(n1))
'''
    dp [
        [9,8,5,4,3,2,1], [7,3,2,1], 
    ]
    [9,8,6,5,4]

    [3,7,8,9,7]
    dp[
        [[18,1]],
        [[101,1]],
        [[7, 2]],
        [[3, 3]],
        [[5, 3]],
        [[2, 4]],
        [[9, 2]],
        [[10, 2]]
    ]
'''
    