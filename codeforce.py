

# Colin Galen Solution

n = int(input())
f = [[0] * 8 for i in range(n+1)]
# f = []
inf = 1e17
for i in range(n+1):
   # f.append([])
   for j in range(8):
      f[i][j] = inf
      # f[i].append(inf)

f[0][0] = 0

for i in range(n):
   [cost, s] = input().split(' ')
   cost = int(cost)
   string_mask = 0
   for pos in range(3):
      c = chr(ord('C') - pos)
      have = 0
      for d in s:
         if c == d:
            have = 1
      if have: 
         string_mask += (1 << pos) # 2 ^ pos
   for mask in range(8):
      # print('f[i][mask]', f[i][mask], 'f[i+1][mask]', f[i+1][mask])
      f[i+1][mask] = min(f[i+1][mask], f[i][mask])
      # print('i', i, 'mask', mask, 'f[i+1][mask]', f[i+1][mask])
      f[i+1][mask | string_mask] = min(f[i+1][mask | string_mask], f[i][mask] + cost)

ans = f[n][7]
if ans == inf: ans = -1
print(ans)
print('f', f) 
# print('ans', ans)
'''
5
10 A
9 BC
11 CA
4 A
5 B

   string_mask = 0b010 or 2
   mask = 0 or 0b000
   mask | string_mask = 5
   f = [
      [0,inf,inf,inf,inf,inf,inf,inf],
      [0,inf,inf,inf,10,inf,inf,inf],
      [0,inf,inf,9,10,inf,inf,19],
      [0,inf,inf,9,10,11,inf,20],
      [0,inf,inf,9,4,11,inf,13],
      [0,inf,5,9,4,11,9,13],
      
      [0,c,b,bc,a,ac,ab,abc]
   ]


   c = 1
   b = 2
   a = 4
   string_mask = 2
   f = [
      [0,inf,inf,inf,inf,inf,inf,inf],
      [0,5,inf,inf,inf,inf,inf,inf],
      [0,5,6,11,inf,inf,inf,inf],
      [0,5,6,11,inf,inf,inf,11],
      [0,5,6,11,4,9,10,11],

      [0,c,b,bc,a,ac,ab,abc]
   ]

   4
   5 C
   6 B
   16 BAC
   4 A

4
5 C
6 B
11 BAC
4 A
'''
# Let's take a problem, given a set, count how many subsets have sum of elements greater than or equal to a given value.
