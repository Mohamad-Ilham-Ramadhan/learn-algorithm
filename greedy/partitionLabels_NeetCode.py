"""
	(Greedy) 763. Partition Labels (medium)

	Link: https://leetcode.com/problems/partition-labels/
    
	Tags:  Hash Table, Two Pointers, String, Greedy

	Constraints:
        - 1 <= s.length <= 500
        - s consists of lowercase English letters.
	======================================================================

	Submissions: 
		runtime: 37 ms, beats 93.83%
		memory: 16.13 MB, beats 89.94%
"""

# NeetCode's solution 
def partitionLabels(s):
    lastIndex = {} # char -> last index in s 

    for i, c in enumerate(s):
        lastIndex[c] = i
    
    res = []
    size, end = 0, 0
    for i, c in enumerate(s):
        size += 1
        end = max(end, lastIndex[c])

        if i == end:
            res.append(size)
            size = 0
    return res

s1 = 'ababcbacadefegdehijhklij' # [9,7,8]
s2 = 'eccbbbbdec' # [10]

print('RESULT: ', partitionLabels(s2))