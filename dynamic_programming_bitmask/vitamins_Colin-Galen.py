'''
   (bitmask dynamic programming) codeforces C. Vitamins (1200)

   time limit per test2 seconds
   memory limit per test256 megabytes
   inputstandard input
   outputstandard output

   Berland shop sells n kinds of juices. Each juice has its price c. Each juice includes some set of vitamins in it. There are three types of vitamins: vitamin "A", vitamin "B" and vitamin "C". Each juice can contain one, two or all three types of vitamins in it.

   Petya knows that he needs all three types of vitamins to stay healthy. What is the minimum total price of juices that Petya has to buy to obtain all three vitamins? Petya obtains some vitamin if he buys at least one juice containing it and drinks it.

   Input
      The first line contains a single integer n (1 ≤ n ≤ 1000) — the number of juices.

      Each of the next n lines contains an integer ci (1 ≤ ci ≤ 100000) and a string si — the price of the i-th juice and the vitamins it contains. String si contains from 1 to 3 characters, and the only possible characters are "A", "B" and "C". It is guaranteed that each letter appears no more than once in each string si. The order of letters in strings si is arbitrary.

Output
   Print -1 if there is no way to obtain all three vitamins. Otherwise print the minimum total price of juices that Petya has to buy to obtain all three vitamins.

Examples
   input #1
      4
      5 C
      6 B
      16 BAC
      4 A
      
      output 15

   input #1
      2
      10 AB
      15 BA

      output -1
      
   input #1
      5
      10 A
      9 BC
      11 CA
      4 A
      5 B

      output 13

   input #1
      6
      100 A
      355 BCA
      150 BC
      160 AC
      180 B
      190 CA

      output 250

   input #1
      2
      5 BA
      11 CB
      
      output 16

   Note
      In the first example Petya buys the first, the second and the fourth juice. He spends 5+6+4=15 and obtains all three vitamins. He can also buy just the third juice and obtain three vitamins, but its cost is 1, which isn't optimal.

      In the second example Petya can't obtain all three vitamins, as no juice contains vitamin "C".

   Tags:
      (bitmask) (brute force) (dynamic programming) (implementation)

   =============================================================================

   submission:
      runtime: 140 ms, memory: 8100 KB
'''

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
      f[i+1][mask] = min(f[i+1][mask], f[i][mask])
      f[i+1][mask | string_mask] = min(f[i + 1][mask | string_mask], f[i][mask] + cost)

ans = f[n][7]
if ans == inf: ans = -1
print(ans)
# print('f', f) 
# print('ans', ans)
'''
   c = 1
   b = 2
   a = 4
'''
# Let's take a problem, given a set, count how many subsets have sum of elements greater than or equal to a given value.
