'''
   (1D dynamic programming) codeforces: Codeforces Round 566 (Div. 2), A. Filling Shapes (1000)

   time limit per test1 second
   memory limit per test256 megabytes
   inputstandard input
   outputstandard output

   You have a given integer `n`. Find the number of WAYS to fill all `3 x n` tiles with the shape described in the picture below. Upon filling, no empty spaces are allowed. Shapes cannot overlap.

            [][][][]
   [][]     [][][][]
     []     [][][][]

   This picture describes when n=4. The left one is the shape and the right one is `3 x n` tiles.
   
   Input
      The only line contains one integer n (1 ≤ n ≤ 60 ) — the length.

   Output
      Print the number of ways to fill.

   Examples
      input #1
         4
         output
         4

      input #2
         1
      output
         0

   Note
   In the first example, there are 4 possible cases of filling.

   In the second example, you cannot fill the shapes in 3 x 1 tiles.

   ===================================================================

   runtime: 77ms, memory: 0kb
'''
n = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 0
for i in range(2, n+1):
   dp[i] = 2 * dp[i-2]

print(dp[n])
