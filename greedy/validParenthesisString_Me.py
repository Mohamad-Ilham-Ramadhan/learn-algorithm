"""
	(Greedy) 678. Valid Parenthesis String (medium)

	Link: https://leetcode.com/problems/valid-parenthesis-string/
    
	Tags: String, Dynamic Programming, Stack, Greedy

	Constraints:
        - 1 <= s.length <= 100
        - s[i] is '(', ')' or '*'.
	======================================================================

	Submissions: 
		runtime: 37 ms, beats 89.13%
		memory: 16.19 MB, beats 89.13%
"""

# NeetCode's solution 
def checkValidString(s):
    if s[0] == ')': return False

    open = []
    star = []
    close = []
    for i in range(0, len(s)):
        if s[i] == '(':
            open.append(i)
        elif s[i] == '*':
            star.append(i)
        else: 
            if len(open) > 0:
                open.pop()
            else:
                close.append(i)
    
    print('open', open)
    print('star', star.copy())
    print('close', close)

    # if len(close) == 0:
    starIndex = 0
    for i in range(0, len(open)):
        if starIndex >= len(star): return False
        while star[starIndex] < open[i]:
            starIndex += 1
            print('startIndex++', starIndex)
            if starIndex >= len(star): return False 
        star = star[:starIndex] + star[starIndex+1 : ]
        # starIndex += 1
    
    # return True
    open = []

    # if len(open) == 0:
    starIndex = len(star) - 1
    for i in range(len(close)-1, -1, -1):
        if starIndex < 0: return False
        print('close[i]', close[i])
        print('starIndex', starIndex)
        while star[starIndex] > close[i]:
            starIndex -= 1
            print('startIndex--', starIndex)
            if starIndex < 0: return False 
        star = star[:starIndex] + star[starIndex+1 :]
        starIndex -= 1
    
    # return True
    close = [] 

    print('open', open)
    print('star', star)
    print('close', close)

    if len(open) == 0 and len(close) == 0: return True 
    return False

s1 = '()' # true
s2 = '(*)' # true
s3 = '(*))' # true
s4 = '()(*()()(*)' # true 
s5 = '((*(()))))' # true
s6 = '((*((( )))))' # true
s7 = ')(' # false
s8 = "((*)" # true
s9 = '(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())' # false (true)
s10 = '((((((()(((((((((()())()()()(((()())))))))))(())(()))())((()()(((()((()(())*(()**)()(())' # false
s11 = '(*)(()(*' # False (true)
s12 = "(((((()*)(*)*))())())(()())())))((**)))))(()())()" # False (true)
s13 = "((()))()(())(*()()())**(())()()()()((*()*))((*()*)" # True
s14 = "((*)" # true
s15 = "()()()()()**)))**" # False
s16 = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()" # True
s17 = "(((((()*)(*)*))())())(()())())))((**)))))(()())()" # 
'''
open =  [3,]
star =  [1,]
close = []
0 1 2 3 4 5 6 7
*****)*)(****
'''
print('RESULT: ', checkValidString(s17))