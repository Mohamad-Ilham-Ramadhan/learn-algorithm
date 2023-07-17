''' 
   (two pointers) leetcode: 16. 3Sum Closest (medium)

   Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.

   Return the sum of the three integers.

   You may assume that each input would have exactly one solution.



   Example 1:

      Input: nums = [-1,2,1,-4], target = 1
      Output: 2
      Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
      
   Example 2:

      Input: nums = [0,0,0], target = 1
      Output: 0
      Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
   

   Constraints:
      3 <= nums.length <= 500
      -1000 <= nums[i] <= 1000
      -10^4 <= target <= 10^4
   
   Related topics: 
      (array) (two pointers) (sorting)
   
   Solution by myself
      sort
      two pointers
   leetcode submission: 
      runtime: 898 ms, beats 62.58%
      memory: 16.27 MB, beats 98.40%
'''
# fail
def threeSumClosest(nums, target): 
    nums.sort()
    l = 0
    r = len(nums) -1 
    total = float('inf')
    s = set()
    while (l+1) < r: 
        lInside = l+1
        rInside = r-1
        sumLR = nums[l] + nums[r]
        # s.add(nums[l]); s.add(nums[r])
        need = target - sumLR
        print('need', need, nums[l], nums[r])
        # if need < nums[l]: 
        #     l -= 1
        # if need > nums[r]:
        #     r += 1

        while lInside <= rInside: 
            mid = (lInside + rInside) // 2
            if nums[mid] > need: 
                rInside = mid - 1
            elif nums[mid] < need: 
                lInside = mid + 1
            else: 
                lInside = mid 
                break
        newTotal = 0
        print('sumLR', sumLR, 'nums[lInside]', nums[lInside], 'nums[lInside-1]', nums[lInside-1])
        if abs(need - nums[lInside]) <= abs(need - nums[lInside-1]) or lInside-1 <= l:
            print('lInside')
            newTotal = sumLR + nums[lInside]
        else: 
            print('lInside-1')
            newTotal = sumLR + nums[lInside-1]

        print('newTotal', newTotal, abs(target-newTotal))
        if nums[lInside] != need: 
            print('total before', total)
            if abs(target-newTotal) < abs(target-total):
                total = newTotal
            print('total after', total)
        else: 
            return target 

        if newTotal < target: 
            l += 1
        else: 
            r -= 1
        print('==============================')
    return total

# succed N^2   
def solution2(nums, target): 
    nums.sort()
    total = float('inf')
    prevN = float('inf')
    for i in range(len(nums)): 
        n = nums[i]
        if n == prevN: 
            continue
        need = target - n
        l = i + 1
        r = len(nums)-1 
        while l < r: 
            sumLR = nums[l] + nums[r];
            if sumLR == need: return target 
            if sumLR < need: 
                l += 1 
            else: 
                r -= 1
            
            total = sumLR+n if abs(target - (sumLR+n)) < abs(target - total) else total 
    
    return total
n2 = [1,2,3,4,5,6,9,10,11,12]
t2 = 7 # 7 (1+2+4) = 7
n3 = [-5,-2,-1,0,1,3,5,6,9,10,13,14,17,19,20]
t3 = 13 # 13 
n1 = [-4,-1,1,2]
t1 = 1
n4 = [-20,-11,-6,-5,-1,3,4,7,8,11,15,18,20]
t4 = 27 # 27
n5 = [-22,-20,-11,-6,-1,4,11,18,22,30,37]
t5 = 30 # 30
n6 = [0,1,2]; t6 = -111 # 0
n7 = [4,0,5,-5,3,3,0,-4,-5]; t7 = -2 # -2
n8 = [1,1,1,5,5,5,5,5,5]; t8 = 14
n9 = [0,1,2]; t9 = 0 # 3
n10 = [0,3,97,102,200]; t10 = 300 # 300

# print('RESULT :', threeSumClosest(n10, t10))
print('RESULT :', solution2(n8, t8))
# n7.sort() 
# print(n7)

'''
    [-4,-1,1,2] t = 1
    num = -1
    total = 2
        need = 2
        l = 1, r = 2 sum = 3, 


    [-5, -5, -4, 0, 0, 3, 3, 4, 5]; t = -2

    nums = -5
    need = 3
    l = -5
    r = 3
    sum = -2

    [0, 3, 97, 102, 200] t = 300
    r = 5
    l = -5
    sum = 0
    need = 100
        then need >= nums[l] and need <= nums[r]
    
    combination = 0 + 200 + 97 = 2 < 1

    target = 27
    l=-20, r=20 combination = -20 + 20 + 18 = 18 < target move left to right one
    l=-11, r=20 combination = -11 + 20 + 18 = 27 == target
    
    target = 9
    l=-20, r=20 combination = -20 + 20 + 8 = 8 < target move left to right one
    l=-11, r=18 combination = -11 + 18 + 3 = 10 > target move right to left one
    l=-11, r=15 combination = -11 + 15 + 4 = 8 > target move left to right one
    l=-6, r=15 combination = -6 + 15 + -1 = 8 > target move left to right one
    l=-5, r=15 combination = -5 + 15 + -1 = 9 == 9 final


'''