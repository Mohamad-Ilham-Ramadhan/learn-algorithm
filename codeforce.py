'''
6
10 A
9 BC
11 CA
4 A
5 B
3 C

output: 15
'''

# O(n^3) solution
# n = int(input())
# juicesMask = [0] * n
# juicesPrice = [0] * n
# for i in range(n):
#    [price, vits] = input().split(' ')
#    juicesPrice[i] = int(price)
#    # A = 0, B = 10, C = 100 (binary)
#    for vit in vits:
#       bit = ord(vit) - ord('A')
#       juicesMask[i] += pow(2, bit)

# ans = float('inf')
# # O( (n^3)/3 + (n/3) ) -> simplified to O(n^3) but faster, if n = 6, O(n^3) == 36 but the O( (n^3)/3 + (n/3) ) == 21
# x = 0
# for i in range(n):
#    x += 1
#    price1 = juicesPrice[i]
#    if juicesMask[i] == 7:
#       ans = min(ans, price1)

#    for j in range(i+1, n):
#       x += 1
#       if juicesMask[i] | juicesMask[j] == juicesMask[i]: # same vitamin
#          continue
#       price2 = juicesPrice[j]
#       if (juicesMask[i] | juicesMask[j]) == 7:
#          ans = min(ans, price1 + price2)

#       for k in range(j+1,n):
#          x += 1
#          price3 = juicesPrice[k]
#          print('total', price1 + price2 + price3)
#          if (juicesMask[i] | juicesMask[j] | juicesMask[k]) == 7:
#             ans = min(ans, price1 + price2 + price3)
            


# print('ans', ans, 'x', x)
'''
   dp[1] = {a: inf, b: inf, c: 5}
   dp[2] = {a: inf, b: 6, c: 5}, 
   dp[3] = {a: 16, b: 6, c: 5}, ans = 16
   dp[4] = {a: 4, b: 6, c: 5}, ans = 15
'''
# my dynamic programming bitmask approach
# n = int(input())
# juicesMask = [0] * n
# juicesPrice = {'A': float('inf'), 'B': float('inf'), 'C': float('inf')} # {a: min(price), b: min(price), c: min(price)}
# for i in range(n):
#    [price, vits] = input().split(' ')
#    # A = 0, B = 10, C = 100 (binary)
#    for vit in vits:
#       bit = ord(vit) - ord('A')
#       juicesMask[i] += pow(2, bit)

# ans = float('inf')
'''
   {
      0: inf, # 
      1: 4, # A
      2: 6, # B
      3: inf, # AB
      4: 5, # C
      5: inf, # CA
      6: inf, # CB
      7: 16, # ABC
   }
'''

n = int(input())
inf = float('inf')
mask = [inf] * 8 # 8 because we use 3 combination 'ABC' 2^3 = 8

for i in range(n):
   [price, vits] = input().split(' ')
   index = 0
   for vit in vits: 
      bit = pow(2, ord(vit) - ord('A')) # if vit = 'C' then pow(2, 2) == 4, if vit = 'A' then pow(2,0) == 1
      index += bit 
   if int(price) < mask[index]: # update value(price) on the mask 
      mask[index] = int(price)

def solve(mask):
   x = 0
   ans = float('inf')
   for i in range(1,8): # i = bit
      x += 1
      if i == 7: 
         # print('try i', mask[i])
         ans = min(ans, mask[i])
      for j in range(i+1, 8):
         x += 1
         # print(mask[i], mask[j], (i | j), ans)
         if (i | j) == 7:
            # print('try j', mask[i] + mask[j])
            ans = min(ans, mask[i] + mask[j])
            continue
         for k in range(j+1, 8):
            x += 1
            if(i | j | k) == 7:
               # print('try k', i,j,k, mask[i] + mask[j] + mask[k])
               ans = min(ans, mask[i] + mask[j] + mask[k])

   print(ans if ans < float('inf') else -1)

solve(mask)

# all input to maks for testing
inf = float('inf')
mask1 = [0, 4,6,inf,5,inf,inf,16] # index as bit and value as price
mask2 = [0,inf,inf,10,inf,inf,inf,inf]
mask3 = [0,4,5,inf,inf,11,9,inf]
mask4 = [0,100,180,inf,inf,160,150,355]
mask5 = [0,inf,inf,5,inf,inf,11,inf]
mask6 = [0,3,4,2,16,7,9,1]

# Colin Galen Solution
# n = int(input())
# f = [[0] * 8 for i in range(n+1)]
# inf = 1e17
# for i in range(n+1):
#    for j in range(8):
#       f[i][j] = inf

# f[0][0] = 0

# for i in range(n):
#    [cost, s] = input().split(' ')
#    cost = int(cost)
#    string_mask = 0
#    for pos in range(3):
#       c = chr(ord('C') - 0)
#       have = 0
#       for d in s:
#          if c == d:
#             have = 1
#       if have: 
#          string_mask += 1 << pos
   
#    for mask in range(8):
#       f[i+1][mask] = min(f[i+1][mask], f[i][mask])
#       f[i+1][mask] = 0
# ans = inf 

# Let's take a problem, given a set, count how many subsets have sum of elements greater than or equal to a given value.
