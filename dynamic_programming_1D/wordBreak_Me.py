"""
	(1D Dynamic Programming) leetcode: 139. Word Break (medium)

	Link: https://leetcode.com/problems/word-break/
    
	Tags: Array, Hash Table, String, Dynamic Programming, Trie, Memoization

	Constraints:
		- 1 <= s.length <= 300
		- 1 <= wordDict.length <= 1000
		- 1 <= wordDict[i].length <= 20
		- s and wordDict[i] consist of only lowercase English letters.
		- All the strings of wordDict are unique.
	======================================================================

	Submissions: 
		runtime: 44 ms, beats 71.37%
		memory: 16.49 MB, beats 59.74%

"""

'''
 cabaabb = [cab, aabb]
'''

'''
		'catcatcatccccatcatcatccc'
	catsandog'; wd3 = ["cats","dog","sand","and","cat"]
	      c a t s a n d o g
	dp [t f f T T f f T f f]
	{

	}
	aaabbaa
	aabbaa
	a a a a a a a 		[aaaa aaa]
 t f f f f f f f
	{
		aaaa: aa
		aaa: aa
	}
	c a t c a t c a t c a t c a t c a t c a t catcatcatccc
 t f f t f f t f f t f f t f f t f f t f f t ffffffffffff
'''
# log(n * m * k) n = s's length, m = wordDict's length, k = wordDict[i]'s length
# No trie, pull DP
def wordBreak(s, wordDict):
	dp = [False] * (len(s) + 1)
	dp[0] = True
	lastMatch = -1
	for i in range(len(s)):
		for j in range(len(wordDict)):
			word = wordDict[j]
			# print('i', i, 's[i]', s[i], 'word', word, 'dp[i]', dp[i])
			isMatch = False # if there is no match in wordDict and last end match index is < than current letter index then return False
			if s[i] == word[0] and dp[i]: 
				k = 0 # if length of the word is 1
				isWordMatch = True
				for k in range(1, len(word)):
					if i+k >= len(s) or s[i+k] != word[k]:
						isWordMatch = False
						break
					# print('s[i+k]', s[i+k], 'word[k]', word[k])
				# print('True', i + k + 1)
				if i + k + 1 <= len(s) and isWordMatch:
					dp[i + k + 1] = True # +1 because dp[1] is equal to s[0]
					lastMatch = max(i + k + 1, lastMatch)
					isMatch = True
			
		# print('i', i, 'isMatch', isMatch, 'lastMatch', lastMatch)
		if not isMatch and i > lastMatch: 
			# print('dp', dp)
			return False
	# print('dp', dp)
	return dp[len(s)]
s1 = 'leetcode'; wd1 = ['leet', 'code'] # true
s2 = 'applepenapple'; wd2 = ["apple","pen"] # true
s3 = 'catsandog'; wd3 = ["cats","dog","sand","and","cat"] # false
s4 = 'cars'; wd4 = ["car", 'ca', 'rs'] # true
s5 = 'bb'; wd5 = ["a","b","bbb","bbbb"] # true
s6 = 'aaaaaaa'; wd6 = ["aaaa","aaa"] # true
s7 =  'catcatcatcatcatcatcatcatcatcatccc'; wd7 = ["cat","catcatcatccc"] # true
s8 = 'ccbb'; wd8 =  ['bc', 'cb'] # false
s9 = 'aebbbbs'; wd9 = ["a","aeb","ebbbb","s","eb"] # true

print('RESULT: ', wordBreak(s9, wd9))
