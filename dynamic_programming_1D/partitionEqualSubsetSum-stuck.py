'''
    (1D dynamic programming) leetcode: 416. Partition Equal Subset Sum (medium)

    Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

    Example 1:

        Input: nums = [1,5,11,5]
        Output: true
        Explanation: The array can be partitioned as [1, 5, 5] and [11].

    Example 2:

        Input: nums = [1,2,3,5]
        Output: false
        Explanation: The array cannot be partitioned into equal sum subsets.
    

    Constraints:
        - 1 <= nums.length <= 200
        - 1 <= nums[i] <= 100
'''

def canPartition(nums): 
    nums.sort()
    total = sum(nums)
    if nums % 2: return False 



n1 = [1,5,11,5] # true
n2 = [1,2,3,5] # false
n3 = [2,6,7,8,11,12] # true
n4 = [2,2,1,1] # true [1,2] [1,2]
n5 = [1,1,4,9,4,13,3,18,16,17] # true
n6 = [16,18,7,16,4,20,16,15,9,4] # false
n7 = [17,9,27,23,25,24,16,5,23,20,20,24,25,8,5,19,1,21,19,27] # true
n8 = [1,2,5] # false
# print('RESULT: ', canPartition(n4))
'''
    [1, 5, 5, 8, 9, 16, 17, 19, 19, 20, 20, 21, 23, 23, 24, 24, 25, 25, 27, 27] 
    total = 358
    half = 179
    [1,5,8,9,16,17,19,19,20,20,21,24] [5,23,23,24,25,25,27,27]

    [1, 2, 3, 3, 4, 5, 5, 8, 8, 14, 14, 15, 18, 21, 23] # true
    total = 144
    half = 72
    

'''
nok = [5,14,3,8,3,15,8,14,18,4,21,2,23,5,1]
nok.sort()
print('nok',nok, sum(nok))
