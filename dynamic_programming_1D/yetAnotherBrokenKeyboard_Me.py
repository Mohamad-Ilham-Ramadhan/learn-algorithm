'''
   (1D Dynamic Programming) Codeforces: round 605 (div 3), C. Yet Another Broken Keyboard (1200)

   time limit per test2 seconds
   memory limit per test256 megabytes
   input: standard input
   output: standard output


   Recently, Norge found a string s=s1s2…sn consisting of n lowercase Latin letters. As an exercise to improve his typing speed, he decided to type all substrings of the string s. Yes, all n*(n+1)/2 of them!

   A substring of s is a non-empty string x=s[a…b]=sasa+1…sb (1 ≤ a ≤ b ≤ n). For example, "auto" and "ton" are substrings of "automaton".

   Shortly after the start of the exercise, Norge realized that his keyboard was broken, namely, he could use only k Latin letters c1,c2,…,ck out of 26.

   After that, Norge became interested in how many substrings of the string she could still type using his broken keyboard. Help him to find this number.

   Input
   The first line contains two space-separated integers n and k
   (1 ≤ n ≤ 2*10^5, 1 ≤ k ≤ 26 ) — the length of the string s and the number of Latin letters still available on the keyboard.

   The second line contains the string s consisting of exactly n lowercase Latin letters.

   The third line contains k space-separated distinct lowercase Latin letters c1,c2,…,ck — the letters still available on the keyboard.

   Output
   Print a single number — the number of substrings of s that can be typed using only available letters c1,c2,…,ck.

   Examples
   input
      7 2
      abacaba
      a b

      output: 12

   input
      10 3
      sadfaasdda
      f a d

      output: 21

   input
      7 1
      aaaaaaa
      b

      output: 0
   Note
   In the first example Norge can print substrings s[1…2], s[2…3], s[1…3], s[1…1], s[2…2], s[3…3], s[5…6], s[6…7], s[5…7], s[5…5], s[6…6], s[7…7].

   Tags: (combinatorics) (dp) (implementation)
====================================================
   Solution by myself 

   submission: 
      # substring formula
         runtime: 61 ms, memory: 1904 KB
      # dynamic programming
         runtime: 6` ms, memory: 3500 KB
'''

[n,k] = input().split(' ')
s = input()
letters = set(input().split(' '))

# input #1 
# n,k = 7,2
# s = 'abacaba'
# letters = set(['a', 'b']) # 12

# input #2
# n,k = 10,3
# s = 'sadfaasdda'
# letters = set(['f', 'a', 'd']) # # 21

# input #3
# n,k = 7,1
# s = 'aaaaaaa'
# letters = set(['b']) # 0

# input #4
# n,k = 1,1
# s = 'a'
# letters = set(['a']) # 1

# No Dynamic Programming, using substring formula: (n*(n+1)) / 2
# count = 0 
# res = 0
# for c in s: 
#    if c in letters: 
#       count += 1 
#       continue 
#    res += (count * (count + 1)) / 2
#    count = 0
# res += (count * (count + 1)) / 2
# print(int(res))

# with Dynamic programming
dp = [0] * (len(s)+1)
res = 0
i = 0
for c in s: 
   if c in letters: 
      i += 1 
      dp[i] = i + dp[i-1]
      continue 
   res += dp[i]
   i = 0
res += dp[i]
print(res)

# x = 10 # string's length
# substrNums = [0] * (x+1)
# for i in range(x):
#    substrNums[i+1] = substrNums[i] + (i+1)
# print('substrNums', substrNums, (x*(x+1)) / 2)
'''
substrNums [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55] 55.0
'''