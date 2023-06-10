"""
  Leetcode: 647. Palindromic Substrings (medium)

  Given a string `s`, return the number of palindromic substrings in it.

  A string is a palindrome when it reads the same backward as forward.

  A substring is a contiguous sequence of characters within the string.
  

  Example 1:
    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".

  Example 2:
    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
  

  Constraints:
    - 1 <= s.length <= 1000
    - s consists of lowercase English letters.

  solution by myself
    pattern n = result of n - 1 + n
    1(0 + 1) 3(2 + 1) 6(3 + 3) 10(6 + 4) 15(10 + 5) 21(15 + 6) 28(21 + 7) 36(28 + 8) 45(36 + 9)

    for example 'aaaa'
    n1 = 'a' = 0 + 1 = 1 -> 'a'
    n2 = 'aa' = 1 + 2 = 3 -> 'a' + 'a', 'aa'
    n3 = 'aaa' = 3 + 3 = 6 -> 'a' 'a' 'aa' + 'a'[2] 'aa'[1,2] 'aaa'[0,2]
    n4 = 'aaaa' = 6 + 4 = 10 => 'a' 'a' 'aa' 'a' 'aa' 'aaa' + 'a'[3] 'aa'[2,3] 'aaa'[1,3] 'aaaa'[0,3]

    and count found palindrome with char in the mid part and left/right side is different for example: 'xyyx', 'aba' not 'aaa' as one:
      xaaxyy
      found palindrome is xaax
      x = 1
      aa = 3
      x = 1
      yy = 3
      xaax = 1

      total = 9


  Leetcode submission:
    #2 (using dynamic programming), newCountSubstrings
      Runtime: 46 ms, beats 99.42%
      Memory: 16.3 MB, beats 64.8%
"""

# using dynamic programming, time complexity O(n). convert from javascript second solution
def countSubstrings(s):
    s += ' '
    result = 0
    prevTwo = [None, -1] # [char, index]
    prevOne = [None, -1] # [char, index]
    count = 0
    countChars = 0

    for i in range(len(s)):
        c = s[i]
        prevC = s[i - 1] if i - 1 >= 0 else None

        if prevC != c:
            prevTwo = prevOne
            prevOne = [prevC, i - 1]
            result += count
            count = 0
            countChars = 0

            # palindromic count
            l = prevTwo[1]
            r = i
            while c != prevOne[0] and s[l] == s[r] and l >= 0 and r < len(s):
                result += 1
                l -= 1
                r += 1

        countChars += 1
        count = count + countChars

    return result


print('RESULT: ', countSubstrings('caaac'))