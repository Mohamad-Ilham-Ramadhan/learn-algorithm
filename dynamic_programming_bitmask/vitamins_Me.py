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
      runtime: 93 ms, memory: 3572 KB
'''

n = int(input())
inf = float('inf')
mask = [inf] * 8 # 8 because we use 3 combination 'ABC' 2^3 = 8. [index(bit): value(price)]
'''
mask:
{
   0: inf, # 
   1: inf, # A    0001
   2: inf, # B    0010
   3: inf, # AB   0011
   4: inf, # C    0100
   5: inf, # CA   0101
   6: inf, # CB   0110
   7: inf, # ABC  0111
}
'''

# collecting bitmask and update the price if it's lower
for i in range(n):
   [price, vits] = input().split(' ')
   index = 0
   for vit in vits: 
      bit = pow(2, ord(vit) - ord('A')) # if vit = 'C' then pow(2, 2) == 4, if vit = 'A' then pow(2,0) == 1
      index += bit 
   if int(price) < mask[index]: # update value(price) on the mask 
      mask[index] = int(price)

# brute force
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