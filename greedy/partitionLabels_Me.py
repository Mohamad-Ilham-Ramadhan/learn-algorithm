"""
	(Greedy) 763. Partition Labels (medium)

	Link: https://leetcode.com/problems/partition-labels/
    
	Tags:  Hash Table, Two Pointers, String, Greedy

	Constraints:
        - 1 <= s.length <= 500
        - s consists of lowercase English letters.
	======================================================================

	Submissions: 
		runtime: 42 ms, beats 77.24%
		memory: 16.01 MB, beats 99.24%
"""


def partitionLabels(s):
    res = []
    lastIndex = 0
    count = 0
    for i in range(0, len(s)):
        lo = s.rfind(s[i]) # last occurence index
        if lo > lastIndex: 
            lastIndex = lo 

        count += 1
        if i == lastIndex: 
            res.append(count)
            lastIndex = i 
            count = 0 

    print('res', res, 'count', count)
    return res
s1 = 'ababcbacadefegdehijhklij' # [9,7,8]
s2 = 'eccbbbbdec' # [10]

print('RESULT: ', partitionLabels(s2))