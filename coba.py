def isPalindrome(x): 
   if x < 0: return False
   x = str(x)

   mid = len(x) // 2 
   l = r = 0 
   if len(x) % 2: # odd 
      l = r = mid 
   else: # even 
      l = mid - 1
      r = mid 
   while l >= 0 and r < len(x): 
      if x[l] != x[r]: return False 
      l -= 1 
      r += 1 
   return True