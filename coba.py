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
      f[i+1][mask] = min(f[i+1][mask], f[i][mask])
      f[i+1][mask | string_mask] = min(f[i + 1][mask | string_mask], f[i][mask] + cost)

ans = f[n][7]
if ans == inf: ans = -1
print(ans)
'''

'''