"""
   (backtracking) leetcode: 17. Letter Combinations of a Phone Number (medium)

   Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

   A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


      2 = abc  3 = def  4 = ghi 
      5 = jkl  6 = mno  7 = pqrs
      8 = tuv  9 = wxyz

   Example 1:
      Input: digits = "23"
      Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

   Example 2:
      Input: digits = ""
      Output: []

   Example 3:
      Input: digits = "2"
      Output: ["a","b","c"]
   

   Constraints:
      - 0 <= digits.length <= 4
      - digits[i] is a digit in the range ['2', '9'].

   Related Topics

   ===================================================================

   Solutioni by myself
      backtracking
   
   LeetCode submisison:
      #1
         runtime: 33 ms, beats 98.74% 
         memory: 16.50 MB, beats 19.38%
"""


# append to result
def letterCombinations(digits):
    result = []
    if not digits:
        return result
    buttons = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
    }

    def backtrack(digit, combination):
        if len(combination) == len(digits):
            result.append(combination)
            return
        num = int(digits[digit])
        for char in buttons[num]:
            backtrack(digit + 1, combination + char)

    # positions = [0] * len(digits)
    backtrack(0, "")
    return result


d1 = "23"  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
d2 = ""  # []
d3 = "456"  # ["gjm","gjn","gjo","gkm","gkn","gko","glm","gln","glo","hjm","hjn","hjo","hkm","hkn","hko","hlm","hln","hlo","ijm","ijn","ijo","ikm","ikn","iko","ilm","iln","ilo"]

# print('RESULT: ', letterCombinations(d1))
if "":
    print("true")
else:
    print("fasle")
