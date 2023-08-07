/*
    Codeforces: (dynamic programming) B. Covered Path (1400)
    link: https://codeforces.com/problemset/problem/534/B
    Tags: dynamic programming, greedy, math, *1400

===========================================================

    submission:
        runtime: 15 ms, memory: 0 KB
*/

#include <bits/stdc++.h>
using namespace std;


int main()
{
   typedef long long ll;
   int v1, v2;
   cin >> v1 >> v2;
   int t, d;
   cin >> t >> d; 

   int result = 0;
   int bonus = 0;
   int dp[t-1];
   for (int i = 0; i < (t-1); i++) {
      result += v1 + bonus;
      dp[i] = v1 + bonus; 
      bonus += d;
   }

   result += v2;
   int lastSpeed = v2;
   for (int i = (t-2); i >= 0; i--) {
      int diff = abs(lastSpeed - dp[i]) - d;
      if (diff > 0) {
         result -= diff;
         dp[i] -= diff;
      } else {
         break;
      }
      lastSpeed = dp[i];
   }
   cout << result;
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