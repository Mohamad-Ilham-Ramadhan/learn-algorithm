/*
    Codeforces: Hello 2019: B. Petr and a Combination Lock (1200)

    link: https://codeforces.com/problemset/problem/1097/B
    
    Problem tags:
        [bitmask, brute force, dp, *1200]
    =============================================

    Submission:
        # bitmask
            rutnime: 15 ms, memory: 0 KB
*/

#include <bits/stdc++.h>
using namespace std;


int main()
{
   // if ( 1 & (1 << 0) ) {
   //    cout << "true\n";
   // } else {
   //    cout << "false\n";
   // }

   // if (1 & 0) {
   //    cout << "true\n";
   // } else {
   //    cout << "false\n";
   // }
   // cout << (1 << 8);

   // int n = 5;
   // string s = bitset< 32 >(n).to_string();
   // cout << "bnary: " << s;

   int n;
   cin >> n;

   vector<int>a(n);
   for (int i = 0; i < n; i++) cin >> a[i];

   for (int mask = 0; mask < (1 << n); mask++) {
      // cout << "mask : " << mask << "\n";
      int sum = 0;
      for (int i = 0; i < n; i++ ) {
         if (mask & (1 << i) ) {
            sum += a[i];
         } else {
            sum -= a[i];
         }
         // cout << "sum: " << sum << "\n";
      }
      string s = bitset< 32 >(mask).to_string();
      // cout << "binary mask: " << s;
      if (sum % 360 == 0) {
         cout << "YES";
         return 0;
      }
   }
   cout << "NO";
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