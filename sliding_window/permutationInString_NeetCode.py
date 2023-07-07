'''
   (sliding window) leetcode: 567. Permutation in String (medium). Companies [Microsoft]

   Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or false otherwise.

   In other words, return true if one of s1's permutations is the substring of `s2`.

   

   Example 1:
      Input: s1 = "ab", s2 = "eidbaooo"
      Output: true
      Explanation: s2 contains one permutation of s1 ("ba").

   Example 2:
      Input: s1 = "ab", s2 = "eidboaoo"
      Output: false
   

   Constraints:
      - 1 <= s1.length, s2.length <= 10^4
      - s1 and s2 consist of lowercase English letters.

   Related Topics:
      (Hash Table) (Two Pointers) (String) (Sliding Window)

   ======================================================= 

   Solution by NeetCode
   
   Leetcode submission:
      runtime: 92 ms, beats 56.9%
      memory: 16.4 MB, beats 59.56%
'''
def checkInclusion(s1, s2):
   if len(s1) > len(s2): return False 

   s1Count, s2Count = [0] * 26, [0] * 26
   for i in range(len(s1)): 
      s1Count[ord(s1[i]) - ord('a')] += 1
      s2Count[ord(s2[i]) - ord('a')] += 1

   matches = 0 
   for i in range(26): 
      matches += (1 if s1Count[i] == s2Count[i] else 0)
   
   l = 0 
   for r in range(len(s1), len(s2)):
      if matches == 26: return True 

      index = ord(s2[r]) - ord('a')
      s2Count[index] += 1 
      if s1Count[index] == s2Count[index]: 
            matches += 1 
      elif s1Count[index] + 1 == s2Count[index]: 
            matches -= 1 
      
      index = ord(s2[l]) - ord('a')
      s2Count[index] -= 1
      if s1Count[index] == s2Count[index]: 
            matches += 1 
      elif s1Count[index] - 1 == s2Count[index]: 
            matches -= 1 

      l += 1
   return matches == 26
s11 = 'ab'; s21 = 'eidbaooo' # True
s12 = 'ab'; s22 = 'eidboaoo' # False
s13 = 'abbb'; s23 = 'eidbabboo' # True
s14 = 'adc'; s24 = 'dcda' # True
s15 = 'adc'; s25 = 'dcdcdcda' # True
s16 = 'abac'; s26 = 'a' # False 
s17 = 'abac'; s27 = 'baaacbc' # True


print('RESULT :', checkInclusion(s17, s27))