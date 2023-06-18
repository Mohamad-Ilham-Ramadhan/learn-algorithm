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

    Solution by myself
        using bottom up dynamic programming
        store the smallest negative number and biggest positive number in prev DP cache
        and check max() product in every iteration
    
    leetcode submission:
        attempt #1
            runtime: 129 ms, beats: 5.32%
            memory: 19.3 MB, beats: 6.74%
        attempt #2
            runtime: 84 ms, beats: 93.47%
            memory: 19.8 MB, beats 6.74%
'''

# attempt #1
def maxProduct(nums):
    m = nums[0] # max
    dp = [[] for n in nums]
    dp[0] = [nums[0]]
    # print('dp', dp)
    for i in range(1, len(nums)): 
        n = nums[i]
        for d in dp[i-1]:
            # print('n', n, 'dp loop', dp)
            if len(dp[i]) == 0:
                dp[i].append(d * n)
            elif dp[i][0] < 0 and (d * n) < 0:
                dp[i] = [min(d * n, dp[i][0])]
            elif dp[i][0] > 0 and (d * n) > 0: 
                dp[i] = [max(dp[i][0], d * n)]
            else: 
                dp[i].append(d * n)
            m = max(m, n, d * n)
        
        # print('dp after loop', dp[i])
        isAppend = True
        for j in range(len(dp[i])):
            dpn = dp[i][j]
            if dpn > 0 and n > 0: 
                dp[i][j] = max(n, dpn)
                isAppend = False
            elif dpn < 0 and n < 0: 
                dp[i][j] = min(n, dpn)
                isAppend = False
        if isAppend:
            dp[i].append(n) # append if in array only one kind (minus/plus)
    # print('dp after', dp)
    return m

# attempt #2, decrease the number of if/else statement which result in faster runtime.
def maxProduct2(nums):
    m = nums[0] # max
    dp = [[] for n in nums]
    dp[0] = [nums[0]]
    for i in range(1, len(nums)): 
        # print('dp', dp)
        n = nums[i]
        for d in dp[i-1]:
            dp[i].append(d * n)
            
        if len(dp[i]) == 1:
            if (dp[i][0] > 0 and n < 0) or (dp[i][0] < 0 and n > 0) or dp[i][0] == 0:
                dp[i].append(n)
        
        # print('dp[i] after loop', dp[i])

        m = max(*dp[i], m)

        if len(dp[i]) == 2 and dp[i][0] == 0: 
            dp[i] = [dp[i][1]]
        
    return m

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
# print('result: ', maxProduct(n7))
print('RESULT : ', maxProduct2(n11))
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