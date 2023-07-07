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

   ======================================================= 

   Solution by myself: 
      #1
         using hashmap to store the count of a character 
         sliding window 
   
   Leetcode submission:
      #1
         runtime: 4607 ms, beats 7.26%
         memory: 16.5 MB, beats 59.33%
      #2
         runtime: 79 ms, beats 84.26%
         memory: 16.4 MB, beats 88.95%
'''
#1
def checkInclusion(s1, s2):
   hm = {}

   for c in s1: 
      if c in hm: 
         hm[c] += 1
      else: 
         hm[c] = 1
   
   i = 0 # left pointer
   r = 0
   while i < len(s2): 
      c = s2[i]
      print('c', c)
      if c in hm: 
         r = i + len(s1)
         if r > len(s2): 
            return False 

         hm2 = {}
         isContinue = False
         for j in range(i, r):
            c2 = s2[j]
            if c2 not in hm: 
               i = j+1
               isContinue = True
               break

            if c2 in hm2: 
               hm2[c2] += 1
            else: 
               hm2[c2] = 1
         
         if isContinue:
            continue

         # check count
         isTrue = True
         for key in hm: 
            if key not in hm2 or hm[key] != hm2[key]:
               isTrue = False 
               break 
         
         if isTrue: 
            return True
      i += 1

   return False

   print('hm', hm)

#2
def solution2(s1, s2):
   hm = {} 
   total = 0
   for c in s1: 
      total += 1
      if c in hm: 
         hm[c] += 1 
      else: 
         hm[c] = 1

   hm2 = {}
   total2 = 0
   l = r = 0
   while r < len(s2): 
      c = s2[r]
      print('c', c, hm2, total2)
      if c not in hm: 
         r += 1
         l = r 
         hm2 = {}
         total2 = 0
         continue

      total2 += 1
      if c in hm2: 
         hm2[c] += 1 
      else: 
         hm2[c] = 1
      
      print('here', hm2, total2, total)

      # if count char in hashmap2 is larger than hashmap1 then remove(shift left pointer) until meet the char
      if hm2[c] > hm[c]: 
         print('CHAR COUNT EXEEDED')
         pass # remove until c char
         while True: 
            c2 = s2[l]
            hm2[c2] -= 1
            total2 -= 1
            l += 1 
            if c2 == c: 
               break


      if total2 == total:
         print('SAME TOTAL')
         return True 

      r += 1
   return False


s11 = 'ab'; s21 = 'eidbaooo' # True
s12 = 'ab'; s22 = 'eidboaoo' # False
s13 = 'abbb'; s23 = 'eidbabboo' # True
s14 = 'adc'; s24 = 'dcda' # True
s15 = 'adc'; s25 = 'dcdcdcda' # True
s16 = 'abac'; s26 = 'a' # False 
s17 = 'abac'; s27 = 'baaacbc' # True


print('RESULT :', solution2(s16, s26))