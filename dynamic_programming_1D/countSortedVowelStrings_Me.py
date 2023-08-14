"""
	(1D dynamic programming) Leetcode: 1641. Count Sorted Vowel Strings (medium)

	Link: https://leetcode.com/problems/count-sorted-vowel-strings/description/
	Tags: Math, Dynamic Programming, Combinatorics

	Constraints:
		- 1 <= n <= 50 
	======================================================================

	Submissions: 
		#1 1D dynamic programming
			runtime: 40 ms, beats 78.49%
			memory: 16.28 MB, beats 72.48%

"""


# O(n^2)
def dp1D(n):
	"""
	dp = [
			[1,1,1,1,1, 5],
			[5,4,3,2,1, 15],
			[15,10,6,3,1, 35],
			[35,20,10,4,1, 70]
	]
	"""
	dp = [1] * 5
	dp.append(5)
	for i in range(1, n):
		total = dp[5]
		pp = dp[0] # j-1, i-1 val
		dp[0] = total
		p = total # j-1, i
		for j in range(1, 5):
				next = p - pp
				pp = dp[j] # j, i-1 val
				dp[j] = next
				p = next
				total += next
		dp[5] = total

	return dp[5]


dp1D(50)

"""
	n=1 -> ['a', 'e', 'i', 'o', 'u']
	n=2 -> ['aa', 'ae', 'ai', 'ao', 'au', 'ee', 'ei', 'eo', 'eu', 'ii', 'io', 'iu', 'oo', 'ou', 'uu']
	n=3 -> ['aaa', 'aae', 'aai', 'aao', 'aau', 'aee', 'aei', 'aeo', 'aeu', 'aii', 'aio', 'aiu', 'aoo', 'aou', 'auu', 'eee', 'eei', 'eeo', 'eeu', 'eii', 'eio', 'eiu', 'eoo', 'eou', 'euu', 'iii', 'iio', 'iiu', 'ioo', 'iou', 'iuu', 'ooo', 'oou', 'ouu', 'uuu']
	n=4 -> ['aaaa', 'aaae', 'aaai', 'aaao', 'aaau', 'aaee', 'aaei', 'aaeo', 'aaeu', 'aaii', 'aaio', 'aaiu', 'aaoo', 'aaou', 'aauu', 'aeee', 'aeei', 'aeeo', 'aeeu', 'aeii', 'aeio', 'aeiu', 'aeoo', 'aeou', 'aeuu', 'aiii', 'aiio', 'aiiu', 'aioo', 'aiou', 'aiuu', 'aooo', 'aoou', 'aouu', 'auuu', 'eeee', 'eeei', 'eeeo', 'eeeu', 'eeii', 'eeio', 'eeiu', 'eeoo', 'eeou', 'eeuu', 'eiii', 'eiio', 'eiiu', 'eioo', 'eiou', 'eiuu', 'eooo', 'eoou', 'eouu', 'euuu', 'iiii', 'iiio', 'iiiu', 'iioo', 'iiou', 'iiuu', 'iooo', 'ioou', 'iouu', 'iuuu', 'oooo', 'ooou', 'oouu', 'ouuu', 'uuuu']
	
	n1 { a: 1, e: 1, i: 1, o: 1, u: 1} = 5
	n2 { a: 5, e: 4, i: 3, o: 2, u: 1} = 15
	n3 { a: 15, e: 10, i: 6, o: 3, u: 1} = 35
	n4 { a: 35, e: 20, i: 10, o: 4, u: 1} = 70
	n5 { a: 70, e: 35, i: 15, o: 5, u: 1} = 126
	n6 { a: 126, e: 56, i: 21, o: 6, u: 1} = 210
	n7 { a: 210, e: 84, i: 28, o: 7, u: 1} = 330

	dp = [
		[1,1,1,1,1, 5],
		[5,4,3,2,1, 15],
		[15,10,6,3,1, 35],
		[35,20,10,4,1, 70]
	]
	
	a 4, 10, 20, 35, 56, 84
	b 3, 6, 10, 15, 21, 28

	a e i o u
1  1 1 1 1 1
2  5 4 3 2 1
3  25 	

"""
