/*
    Codeforces: (dynamic programming) B. Covered Path (1400)
    link: https://codeforces.com/problemset/problem/534/B
    Tags: dynamic programming, greedy, math, *1400

===========================================================

    submission:
        runtime: 15 ms, memory: 800 KB
*/

#include <bits/stdc++.h>
using namespace std;


int main()
{
   typedef long long ll;
   int start, end;
   cin >> start >> end;
   int n, d;
   cin >> n >> d; 

   const ll  inf = 1e17;
   ll dp[n][1000];

   for (ll i = 0; i < n; i++) {
      for (ll j = 0; j < 1000; j++) {
         dp[i][j] = -inf;
      }
   }

   dp[0][start] = 0;

   for (ll i = 0; i < n-1; i++) {
      for (ll j = 0; j < 1000; j++) {
         for (ll k = -d; k <= d; k++) {
            if (j + k >= 0 && j + k < 1000) {
               dp[i + 1][j + k] = max( dp[i + 1][j + k], dp[i][j] + j);
            }
         }
      }
   }
   cout << dp[n - 1][end] + end;
   return 0;
}

/**
 
   cek semua kombinasi dengan menggunakan binary
   kombinasinya jika 1 maka tambah jika 0 maka kurang

   n 3; 10 20 30

   mask each iteration:
   000 ==> -10 -20 -30 == 60 "NO"
   001
   010 ==> -10 +20 -30 == -20 "NO"
   011 ==> +10 +20 -30 == 0 "YES"
   100
   101
   110
   111

*/