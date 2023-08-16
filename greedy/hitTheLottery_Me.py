"""
	(Greedy) codeforces: A. Hit the Lottery (800)

	Link:https://codeforces.com/problemset/problem/996/A
    
	Tags: dp, greedy, *800

	Constraints:
		- n (1 ≤ n ≤ 10^9).
	======================================================================

	Submissions: 
		runtime: 62 ms, memory: 0 KB
"""

'''

	n =24 (20+1+1+1+1)
'''
n = int(input())
dollars = [1, 5, 10, 20, 100]

c = n # current remains
ans = 0
for i in range(len(dollars)-1, -1, -1): 
	d = dollars[i]
	if d > c: 
		continue 
	elif c % d < c: 
		ans += (c - (c % d)) / d
		c = c % d
print(int(ans))
