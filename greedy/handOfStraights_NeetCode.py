"""
	(Greedy) 846. Hand of Straights (medium)

	Link: https://leetcode.com/problems/hand-of-straights/
    
	Tags:  Array, Greedy

	Constraints:
        - 1 <= hand.length <= 10^4
        - 0 <= hand[i] <= 10^9
        - 1 <= groupSize <= hand.length
	======================================================================

	Submissions: 
		runtime: 177 ms, beats 72.95%
		memory: 17.97 MB, beats 81.57%
"""
import heapq
# neetcode's solution
def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize: 
        return False 
    
    count = {}
    for n in hand: 
        count[n] = 1 + count.get(n, 0)
    
    minH = list(count.keys())
    heapq.heapify(minH)
    while minH:
        first = minH[0]

        for i in range(first, first + groupSize):
            if i not in count: 
                return False 
            count[i] -= 1
            if count[i] == 0:
                if i != minH[0]:
                    return False 
                heapq.heappop(minH)

    return True


h1 = [1,2,3,6,2,3,4,7,8]; g1 = 3 # True
h2 = [1,2,3,7,2,3,4,6,8]; g2 = 3 # True
h3 = [1,4,2,3,6,9,8,7]; g3 = 4 # True
h4 = [1,4,2,5,3, 7,11,9,10,8]; g4 = 5 # True
h5 = [1,1,2,2,3,3]; g5 = 2 # False
print('RESULT: ', isNStraightHand(h5, g5))
''' 
    {
        1: 0,
        4: 1,
        5: 1
    }
    [1,2] [3,4]
'''


