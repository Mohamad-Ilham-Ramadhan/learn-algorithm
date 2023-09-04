"""
	(1D Dynamic Programming) 96. Unique Binary Search Trees II (medium)

	Link: https://leetcode.com/problems/unique-binary-search-trees-ii
    
	Constraints:
		- 1 <= n <= 8
	
	Tags: Dynamic Programming, Backtracking, Tree, Binary Search Tree, Binary Tree
	======================================================================
   
   Submission:
		runtime: 61 ms, beats 29.64%
      memory: 18.56 MB, beats 5.55%

"""

'''
1 2 5 14 42 132 429 1430
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
def numTrees(n):
	pass
n1=1 # 1
n2=2 # 2
n3=3 # 5
n4=4 # 14 
n5=5 # 42 
n6=6 # 132 
n7=7 # 429 
n8=8 # 1430 #
n9=19 # 1767263190
# print('RESULT: ', numTrees(19))
'''
11440 + 3003 + 792 + 210 + 56 + 15 + 4 + 1
	n8
	7 = 429 * 2 = 858
	6 = 132 * 2 = 264
	5 = (42 * 2) * 2 = 168
	4 = (14 * 5) * 2 = 140
'''

root1 = TreeNode(1)
root2 = TreeNode(2,TreeNode(1))
root3 = TreeNode(1,None, TreeNode(2))

def treePrint(root, parVal):
	if root == None:
		print('Null', parVal)
		return 
	print('root.val', root.val)
	treePrint(root.left, root.val)
	treePrint(root.right, root.val)

def treeDp(n):
	dp = [
            [],
            [TreeNode(1)]
            # [root1],
            # [root2, root3],
            # []
        ]

	def switchTree(root, rightRoot, n):
		if rightRoot == None: return
		root.val = n - (rightRoot.val - 1)
		if rightRoot.left: 
				root.right = TreeNode(0)
				switchTree(root.right, rightRoot.left, n)
		if rightRoot.right:
				root.left = TreeNode(0)
				switchTree(root.left, rightRoot.right, n)

	for i in range(2, n+1):
		h = i // 2
		dp.append([])
		for j in range(i, i-h, -1):
				for tree in dp[j-1]:
					# dp.append([]) # current dp is j
					ct = TreeNode(j, tree) # current added tree 
					# add the right node
					r = i - j
					if r > 0:
						for mTree in dp[r]: # 
								ct = TreeNode(j, tree) # current added tree 
								ct.right = TreeNode(0)
								switchTree(ct.right, mTree, i)
								dp[i].append(ct) # because prev root.val is lower so add as left node
					else: 
						dp[i].append(ct) # because prev root.val is lower so add as left node
		
		# return dp[n]

		reverseTrees = []
		for t in dp[-1]:
				# continue
				ct = TreeNode((i - t.val) + 1)
				if t.right: 
					ct.left = TreeNode(0)
					switchTree(ct.left, t.right, i)
				if t.left: 
					ct.right = TreeNode(0)
					switchTree(ct.right, t.left, i)
				reverseTrees.append(ct)

		dp[-1].extend(reverseTrees)
		# i -= 1
		if i % 2: # if n is odd
				for tree in dp[h]: 
					for mTree in dp[h]: 
						ct = TreeNode(h+1, tree) 
						ct.right = TreeNode(0)
						switchTree(ct.right, mTree, i)
						dp[i].append(ct)
	return dp[n]

# uniqueTrees = treeDp(5)
# for t in uniqueTrees:
# 	print('==============')
# 	print('result tree')
# 	treePrint(t, 0)

# dp = [[]]
# for i in range(1, 1, -1):
# 	print('i', i)
# for j in dp[0]:
# 	print('j', j)

def odd(): 
	def switchTree(root, rightRoot, n):
		if rightRoot == None: return
		root.val = n - (rightRoot.val - 1)
		if rightRoot.left: 
			root.right = TreeNode(0)
			switchTree(root.right, rightRoot.left, n)
		if rightRoot.right:
			root.left = TreeNode(0)
			switchTree(root.left, rightRoot.right, n)

	dp = [
		[],
		[TreeNode(1)],
		[TreeNode(2, TreeNode(1)), TreeNode(1, None, TreeNode(2))],
		[]
	]
	for tree in dp[2]: 
		for t in dp[2]: 
			ct = TreeNode(3, tree) 
			ct.right = TreeNode(0)
			switchTree(ct.right, t, 5)
			dp[3].append(ct)
	return dp[3]

uniqueTrees = odd()
for t in uniqueTrees:
	print('==============')
	print('result tree')
	treePrint(t, 0)

dp = [ [TreeNode(2, TreeNode(1))] ]
et = TreeNode(3, 
		TreeNode(2, TreeNode(1)),
		TreeNode(0)
)

# print('original tree')
# treePrint(dp[0][0], 0)
# print('=============')
'''
	Switching value mechanic 
	for example n = 5 
	so:
		val 1 = 5
		val 2 = 4
		val 3 = 3
	if n = 8
	so:
		val 1 = 8
		val 2 = 7
		val 3 = 6
		val 4 = 5
'''

n4 = 4 # [[1,null,2,null,3,null,4],[1,null,2,null,4,3],[1,null,3,2,4],[1,null,4,2,null,null,3],[1,null,4,3,null,2],[2,1,3,null,null,null,4],[2,1,4,null,null,3],[3,1,4,null,2],[3,2,4,1],[4,1,null,null,2,null,3],[4,1,null,null,3,2],[4,2,null,1,3],[4,3,null,1,null,null,2],[4,3,null,2,null,1]]

# output: [[4,3,null,2,null,1],[4,3,null,1,null,null,2],[4,1,null,null,2,null,3],[4,1,null,null,3,2],[4,2,null,1,3],[4,2,4,1],[4,1,4,null,2],[1,null,2,null,3,null,4],[1,null,2,null,4,3],[1,null,4,3,null,2],[1,null,4,2,null,null,3],[1,null,3,2,4],[1,1,3,null,null,null,4],[1,1,4,null,null,3]]

print(len([[5,4,None,3,None,2,None,1],[5,4,None,3,None,1,None,None,2],[5,4,None,1,None,None,2,None,3],[5,4,None,1,None,None,3,2],[5,4,None,2,None,1,3],[5,3,None,2,4,1],[5,3,None,1,4,None,2],[5,1,None,None,2,None,3,None,4],[5,1,None,None,2,None,4,3],[5,1,None,None,4,3,None,2],[5,1,None,None,4,2,None,None,3],[5,1,None,None,3,2,4],[5,2,None,1,3,None,None,None,4],[5,2,None,1,4,None,None,3],[4,3,5,2,None,None,None,1],[4,3,5,1,None,None,None,None,2],[4,1,5,None,2,None,None,None,3],[4,1,5,None,3,None,None,2],[4,2,5,1,3],[1,None,2,None,3,None,4,None,5],[1,None,2,None,3,None,5,4],[1,None,2,None,5,4,None,3],[1,None,2,None,5,3,None,None,4],[1,None,2,None,4,3,5],[1,None,3,2,4,None,None,None,5],[1,None,3,2,5,None,None,4],[1,None,5,4,None,3,None,2],[1,None,5,4,None,2,None,None,3],[1,None,5,2,None,None,3,None,4],[1,None,5,2,None,None,4,3],[1,None,5,3,None,2,4],[1,None,4,3,5,2],[1,None,4,2,5,None,3],[2,1,3,None,None,None,4,None,5],[2,1,3,None,None,None,5,4],[2,1,5,None,None,4,None,3],[2,1,5,None,None,3,None,None,4],[2,1,4,None,None,3,5],[3,2,5,1,None,4],[3,2,5,1,None,4],[3,1,5,None,2,4],[3,1,5,None,2,4]]))

# n6's expect: [[1,null,2,null,3,null,4,null,5,null,6],[1,null,2,null,3,null,4,null,6,5],[1,null,2,null,3,null,5,4,6],[1,null,2,null,3,null,6,4,null,null,5],[1,null,2,null,3,null,6,5,null,4],[1,null,2,null,4,3,5,null,null,null,6],[1,null,2,null,4,3,6,null,null,5],[1,null,2,null,5,3,6,null,4],[1,null,2,null,5,4,6,3],[1,null,2,null,6,3,null,null,4,null,5],[1,null,2,null,6,3,null,null,5,4],[1,null,2,null,6,4,null,3,5],[1,null,2,null,6,5,null,3,null,null,4],[1,null,2,null,6,5,null,4,null,3],[1,null,3,2,4,null,null,null,5,null,6],[1,null,3,2,4,null,null,null,6,5],[1,null,3,2,5,null,null,4,6],[1,null,3,2,6,null,null,4,null,null,5],[1,null,3,2,6,null,null,5,null,4],[1,null,4,2,5,null,3,null,6],[1,null,4,2,6,null,3,5],[1,null,4,3,5,2,null,null,6],[1,null,4,3,6,2,null,5],[1,null,5,2,6,null,3,null,null,null,4],[1,null,5,2,6,null,4,null,null,3],[1,null,5,3,6,2,4],[1,null,5,4,6,2,null,null,null,null,3],[1,null,5,4,6,3,null,null,null,2],[1,null,6,2,null,null,3,null,4,null,5],[1,null,6,2,null,null,3,null,5,4],[1,null,6,2,null,null,4,3,5],[1,null,6,2,null,null,5,3,null,null,4],[1,null,6,2,null,null,5,4,null,3],[1,null,6,3,null,2,4,null,null,null,5],[1,null,6,3,null,2,5,null,null,4],[1,null,6,4,null,2,5,null,3],[1,null,6,4,null,3,5,2],[1,null,6,5,null,2,null,null,3,null,4],[1,null,6,5,null,2,null,null,4,3],[1,null,6,5,null,3,null,2,4],[1,null,6,5,null,4,null,2,null,null,3],[1,null,6,5,null,4,null,3,null,2],[2,1,3,null,null,null,4,null,5,null,6],[2,1,3,null,null,null,4,null,6,5],[2,1,3,null,null,null,5,4,6],[2,1,3,null,null,null,6,4,null,null,5],[2,1,3,null,null,null,6,5,null,4],[2,1,4,null,null,3,5,null,null,null,6],[2,1,4,null,null,3,6,null,null,5],[2,1,5,null,null,3,6,null,4],[2,1,5,null,null,4,6,3],[2,1,6,null,null,3,null,null,4,null,5],[2,1,6,null,null,3,null,null,5,4],[2,1,6,null,null,4,null,3,5],[2,1,6,null,null,5,null,3,null,null,4],[2,1,6,null,null,5,null,4,null,3],[3,1,4,null,2,null,5,null,null,null,6],[3,1,4,null,2,null,6,null,null,5],[3,1,5,null,2,4,6],[3,1,6,null,2,4,null,null,null,null,5],[3,1,6,null,2,5,null,null,null,4],[3,2,4,1,null,null,5,null,null,null,6],[3,2,4,1,null,null,6,null,null,5],[3,2,5,1,null,4,6],[3,2,6,1,null,4,null,null,null,null,5],[3,2,6,1,null,5,null,null,null,4],[4,1,5,null,2,null,6,null,3],((([4,1,6,null,2,5,null,null,3]))),[4,1,5,null,3,null,6,2],((([4,1,6,null,3,5,null,2]))),[4,2,5,1,3,null,6],((([4,2,6,1,3,5]))),[4,3,5,1,null,null,6,null,2],((([4,3,6,1,null,5,null,null,2]))),[4,3,5,2,null,null,6,1],(([4,3,6,2,null,5,null,1])),[5,1,6,null,2,null,null,null,3,null,4],[5,1,6,null,2,null,null,null,4,3],[5,1,6,null,3,null,null,2,4],[5,1,6,null,4,null,null,2,null,null,3],[5,1,6,null,4,null,null,3,null,2],[5,2,6,1,3,null,null,null,null,null,4],[5,2,6,1,4,null,null,null,null,3],[5,3,6,1,4,null,null,null,2],[5,3,6,2,4,null,null,1],[5,4,6,1,null,null,null,null,2,null,3],[5,4,6,1,null,null,null,null,3,2],[5,4,6,2,null,null,null,1,3],[5,4,6,3,null,null,null,1,null,null,2],[5,4,6,3,null,null,null,2,null,1],[6,1,null,null,2,null,3,null,4,null,5],[6,1,null,null,2,null,3,null,5,4],[6,1,null,null,2,null,4,3,5],[6,1,null,null,2,null,5,3,null,null,4],[6,1,null,null,2,null,5,4,null,3],[6,1,null,null,3,2,4,null,null,null,5],[6,1,null,null,3,2,5,null,null,4],[6,1,null,null,4,2,5,null,3],[6,1,null,null,4,3,5,2],[6,1,null,null,5,2,null,null,3,null,4],[6,1,null,null,5,2,null,null,4,3],[6,1,null,null,5,3,null,2,4],[6,1,null,null,5,4,null,2,null,null,3],[6,1,null,null,5,4,null,3,null,2],[6,2,null,1,3,null,null,null,4,null,5],[6,2,null,1,3,null,null,null,5,4],[6,2,null,1,4,null,null,3,5],[6,2,null,1,5,null,null,3,null,null,4],[6,2,null,1,5,null,null,4,null,3],[6,3,null,1,4,null,2,null,5],[6,3,null,1,5,null,2,4],[6,3,null,2,4,1,null,null,5],[6,3,null,2,5,1,null,4],[6,4,null,1,5,null,2,null,null,null,3],[6,4,null,1,5,null,3,null,null,2],[6,4,null,2,5,1,3],[6,4,null,3,5,1,null,null,null,null,2],[6,4,null,3,5,2,null,null,null,1],[6,5,null,1,null,null,2,null,3,null,4],[6,5,null,1,null,null,2,null,4,3],[6,5,null,1,null,null,3,2,4],[6,5,null,1,null,null,4,2,null,null,3],[6,5,null,1,null,null,4,3,null,2],[6,5,null,2,null,1,3,null,null,null,4],[6,5,null,2,null,1,4,null,null,3],[6,5,null,3,null,1,4,null,2],[6,5,null,3,null,2,4,1],[6,5,null,4,null,1,null,null,2,null,3],[6,5,null,4,null,1,null,null,3,2],[6,5,null,4,null,2,null,1,3],[6,5,null,4,null,3,null,1,null,null,2],[6,5,null,4,null,3,null,2,null,1]]

# n6' output: [[6,5,null,4,null,3,null,2,null,1],[6,5,null,4,null,3,null,1,null,null,2],[6,5,null,4,null,1,null,null,2,null,3],[6,5,null,4,null,1,null,null,3,2],[6,5,null,4,null,2,null,1,3],[6,5,null,3,null,2,4,1],[6,5,null,3,null,1,4,null,2],[6,5,null,1,null,null,2,null,3,null,4],[6,5,null,1,null,null,2,null,4,3],[6,5,null,1,null,null,4,3,null,2],[6,5,null,1,null,null,4,2,null,null,3],[6,5,null,1,null,null,3,2,4],[6,5,null,2,null,1,3,null,null,null,4],[6,5,null,2,null,1,4,null,null,3],[6,4,null,3,5,2,null,null,null,1],[6,4,null,3,5,1,null,null,null,null,2],[6,4,null,1,5,null,2,null,null,null,3],[6,4,null,1,5,null,3,null,null,2],[6,4,null,2,5,1,3],[6,1,null,null,2,null,3,null,4,null,5],[6,1,null,null,2,null,3,null,5,4],[6,1,null,null,2,null,5,4,null,3],[6,1,null,null,2,null,5,3,null,null,4],[6,1,null,null,2,null,4,3,5],[6,1,null,null,3,2,4,null,null,null,5],[6,1,null,null,3,2,5,null,null,4],[6,1,null,null,5,4,null,3,null,2],[6,1,null,null,5,4,null,2,null,null,3],[6,1,null,null,5,2,null,null,3,null,4],[6,1,null,null,5,2,null,null,4,3],[6,1,null,null,5,3,null,2,4],[6,1,null,null,4,3,5,2],[6,1,null,null,4,2,5,null,3],[6,2,null,1,3,null,null,null,4,null,5],[6,2,null,1,3,null,null,null,5,4],[6,2,null,1,5,null,null,4,null,3],[6,2,null,1,5,null,null,3,null,null,4],[6,2,null,1,4,null,null,3,5],[6,3,null,2,4,1,null,null,5],[6,3,null,2,5,1,null,4],[6,3,null,1,4,null,2,null,5],[6,3,null,1,5,null,2,4],[5,4,6,3,null,null,null,2,null,1],[5,4,6,3,null,null,null,1,null,null,2],[5,4,6,1,null,null,null,null,2,null,3],[5,4,6,1,null,null,null,null,3,2],[5,4,6,2,null,null,null,1,3],[5,3,6,2,4,null,null,1],[5,3,6,1,4,null,null,null,2],[5,1,6,null,2,null,null,null,3,null,4],[5,1,6,null,2,null,null,null,4,3],[5,1,6,null,4,null,null,3,null,2],[5,1,6,null,4,null,null,2,null,null,3],[5,1,6,null,3,null,null,2,4],[5,2,6,1,3,null,null,null,null,null,4],[5,2,6,1,4,null,null,null,null,3],[4,3,6,2,null,5,null,1],[4,3,6,2,null,5,null,1],[4,3,6,1,null,5,null,null,2],[4,3,6,1,null,5,null,null,2],[4,1,6,null,2,5,null,null,3],[4,1,6,null,2,5,null,null,3],[4,1,6,null,3,5,null,2],[4,1,6,null,3,5,null,2],[4,2,6,1,3,5],[4,2,6,1,3,5],[1,null,2,null,3,null,4,null,5,null,6],[1,null,2,null,3,null,4,null,6,5],[1,null,2,null,3,null,6,5,null,4],[1,null,2,null,3,null,6,4,null,null,5],[1,null,2,null,3,null,5,4,6],[1,null,2,null,4,3,5,null,null,null,6],[1,null,2,null,4,3,6,null,null,5],[1,null,2,null,6,5,null,4,null,3],[1,null,2,null,6,5,null,3,null,null,4],[1,null,2,null,6,3,null,null,4,null,5],[1,null,2,null,6,3,null,null,5,4],[1,null,2,null,6,4,null,3,5],[1,null,2,null,5,4,6,3],[1,null,2,null,5,3,6,null,4],[1,null,3,2,4,null,null,null,5,null,6],[1,null,3,2,4,null,null,null,6,5],[1,null,3,2,6,null,null,5,null,4],[1,null,3,2,6,null,null,4,null,null,5],[1,null,3,2,5,null,null,4,6],[1,null,6,5,null,4,null,3,null,2],[1,null,6,5,null,4,null,2,null,null,3],[1,null,6,5,null,2,null,null,3,null,4],[1,null,6,5,null,2,null,null,4,3],[1,null,6,5,null,3,null,2,4],[1,null,6,4,null,3,5,2],[1,null,6,4,null,2,5,null,3],[1,null,6,2,null,null,3,null,4,null,5],[1,null,6,2,null,null,3,null,5,4],[1,null,6,2,null,null,5,4,null,3],[1,null,6,2,null,null,5,3,null,null,4],[1,null,6,2,null,null,4,3,5],[1,null,6,3,null,2,4,null,null,null,5],[1,null,6,3,null,2,5,null,null,4],[1,null,5,4,6,3,null,null,null,2],[1,null,5,4,6,2,null,null,null,null,3],[1,null,5,2,6,null,3,null,null,null,4],[1,null,5,2,6,null,4,null,null,3],[1,null,5,3,6,2,4],[1,null,4,3,5,2,null,null,6],[1,null,4,2,5,null,3,null,6],[1,null,4,3,6,2,null,5],[1,null,4,2,6,null,3,5],[2,1,3,null,null,null,4,null,5,null,6],[2,1,3,null,null,null,4,null,6,5],[2,1,3,null,null,null,6,5,null,4],[2,1,3,null,null,null,6,4,null,null,5],[2,1,3,null,null,null,5,4,6],[2,1,4,null,null,3,5,null,null,null,6],[2,1,4,null,null,3,6,null,null,5],[2,1,6,null,null,5,null,4,null,3],[2,1,6,null,null,5,null,3,null,null,4],[2,1,6,null,null,3,null,null,4,null,5],[2,1,6,null,null,3,null,null,5,4],[2,1,6,null,null,4,null,3,5],[2,1,5,null,null,4,6,3],[2,1,5,null,null,3,6,null,4],[3,1,4,null,2,null,5,null,null,null,6],[3,1,4,null,2,null,5,null,null,null,6],[3,1,4,null,2,null,6,null,null,5],[3,1,4,null,2,null,6,null,null,5],[3,1,6,null,2,5,null,null,null,4],[3,1,6,null,2,5,null,null,null,4],[3,1,6,null,2,4,null,null,null,null,5],[3,1,6,null,2,4,null,null,null,null,5],[3,1,5,null,2,4,6],[3,1,5,null,2,4,6]]