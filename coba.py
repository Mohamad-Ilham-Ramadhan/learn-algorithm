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
		runtime: 1902 ms, beats 13.15%
		memory: 60.75 MB, beats 96.73%
"""

def mergeTriplets(triplets, target):
    trues = [False, False, False]
    for t in triplets: 
        trueIndexes = []
        for i in range(0, len(target)):
            if target[i] == t[i]:
                trueIndexes.append(i)
            if t[i] > target[i]: 
                trueIndexes = []
                break 
        for index in trueIndexes:
            trues[index] = True 

    for isTrue in trues: 
        if not isTrue: 
            return False
    return True

# solution 2 is needed return true when 3 target trues already acquired
tr1 = [[2,5,3],[1,8,4],[1,7,5]]; ta1 = [2,7,5] # true 
tr2 = [[3,4,5],[4,5,6]]; ta2 = [3,2,5] # false 
tr3 = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]; ta3 = [5,5,5] # true 
print('RESULT: ', mergeTriplets(tr3, ta3))
'''
    [2,7,3] [1,8,4] [1,5,5]
'''
