'''
   (backtracking) 131. Palindrome Partitioning (medium)

   Given a string s, partition s such that every substring [A substring is a contiguous non-empty sequence of characters within a string.] of the partition is a palindrome [A palindrome is a string that reads the same forward and backward.]. Return all possible palindrome partitioning of s.


   Example 1:
      Input: s = "aab"
      Output: [["a","a","b"],["aa","b"]]

   Example 2:
      Input: s = "a"
      Output: [["a"]]
   

   Constraints:
      - 1 <= s.length <= 16
      - s contains only lowercase English letters.

   Related Topics: 
      (String) (Dynamic Programming) (Backtracking)
   ============================================================================

   Solution by myself: 
      backtracking 

   Leetcode runtime: 
      runtime: 709 ms, beats 15.62%
      memory: 35 MB, beats 11.74%
'''
def partition(s): 
   # using this function this is not really optimal way
   def isPalindrome(s): 
      l = r = 0
      if len(s) % 2: # odd 
         l = r = len(s) // 2
      else: # even 
         l = (len(s) // 2) - 1
         r = len(s) // 2

      while l >= 0 and r < len(s): 
         if s[l] == s[r]: 
            l -= 1
            r += 1 
         else: 
            return False 
      return True
   # the optimal way is to use dynamic programing when checking the palindrome

   partitions = [] 
   def dfs(i, arr, length): 
      if length == len(s):
         partitions.append(arr)
      
      cs = ''

      for j in range(i, len(s)): 
         c = s[j]
         cs += c 
         if isPalindrome(cs): 
            dfs(j+1, [*arr,cs],length+len(cs))

   dfs(0,[],0)
   return partitions

s1 = 'aab'
s2 = 'a'
s3 = 'aabaa'
print('RESULT :', partition(s3))
'''
   [["a","a","b","a","a"],["a","a","b","aa"],["a","aba","a"],["aa","b","a","a"],["aa","b","aa"],["aabaa"]]
   
   [[aabaa],[a,a,b,aa],[a,a,b,a,a],[a,aba,a],[aa,b,a,a],[aa,b,aa]]
   [[aabaa],[a,a,b,aa],[a,a,b,a,a],[a,aba,a],[aa,b,aa],[aa,b,a,a]]
   cs = a
   0
      
'''