"""
	(Greedy) 678. Valid Parenthesis String (medium)

	Link: https://leetcode.com/problems/valid-parenthesis-string/
    
	Tags: String, Greedy

	Constraints:
        - 1 <= s.length <= 100
        - s[i] is '(', ')' or '*'.
	======================================================================

	Submissions: 
		runtime: 44 ms, beats 27.17%
		memory: 16.23 MB, beats 66.99%
"""

# NeetCode's solution 
def checkValidString(s):
    leftMin = 0; leftMax = 0;

    for c in s: 
        if c == '(':
            leftMin, leftMax = leftMin + 1, leftMax + 1
        elif c == ')':
            leftMin, leftMax = leftMin -1, leftMax - 1 
        else: 
            leftMin, leftMax = leftMin -1, leftMax + 1
        if leftMax < 0:
            return False
        if leftMin < 0: # s = '(*)('
            leftMin = 0

    return leftMin == 0

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