"""
	(Greedy) 846. Hand of Straights (medium)

	Link: https://leetcode.com/problems/hand-of-straights/
    
	Tags:  Array, Hash Table, Greedy, Sorting

	Constraints:
        - 1 <= hand.length <= 10^4
        - 0 <= hand[i] <= 10^9
        - 1 <= groupSize <= hand.length
	======================================================================

	Submissions: 
		runtime: 189 ms, beats 44.46%
		memory: 18.14 MB, beats 47.47%
"""
def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize > 0: return False
    hand.sort() 
    print('sorted hand', hand)
    hm = {}
    for i in range(0, len(hand)):
        if hand[i] not in hm: hm[hand[i]] = 1
        else: hm[hand[i]] += 1
    print('hashmap', hm)
    
    x = 0
    while x < len(hand) / groupSize:
        g = 0
        n = -10
        zeroKey = [] # key with zero count value
        for key in hm:
            print('key', key)
            if n + 1 != key and g > 0: 
                return False 
            n = key 
            hm[key] -= 1
            g += 1
            if hm[key] == 0: zeroKey.append(key)
            if g == groupSize: 
                break 
        print('zeroKey', zeroKey)
        for key in zeroKey: 
            del hm[key]
        print('newHm', hm)
        x += 1

    if len(hm) > 0: return False 
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


