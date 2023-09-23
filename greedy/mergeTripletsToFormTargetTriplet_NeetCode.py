"""
	(Greedy) 1899. Merge Triplets to Form Target Triplet (medium)

	Link: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
    
	Tags:  Array, Greedy

	Constraints:
        - 1 <= triplets.length <= 10^5
        - triplets[i].length == target.length == 3
        - 1 <= ai, bi, ci, x, y, z <= 1000
	======================================================================

	Submissions: 
		runtime: 1756 ms, beats 80.16%
		memory: 61.52 MB, beats 61.05%
"""
# NeetCode's solution
def mergeTriplets(triplets, target):
    good = set()

    for t in triplets:
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue 
            
        for i, v in enumerate(t):
            if v == target[i]:
                good.add(i)
    return len(good) == 3

# solution 2 is needed return true when 3 target trues already acquired
tr1 = [[2,5,3],[1,8,4],[1,7,5]]; ta1 = [2,7,5] # true 
tr2 = [[3,4,5],[4,5,6]]; ta2 = [3,2,5] # false 
tr3 = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]; ta3 = [5,5,5] # true 
tr4 = [[3,1,7],[1,5,10]]; ta4 = [3,5,7] # False
print('RESULT: ', mergeTriplets(tr4, ta4))
'''
    [2,7,3] [1,8,4] [1,5,5]
'''
