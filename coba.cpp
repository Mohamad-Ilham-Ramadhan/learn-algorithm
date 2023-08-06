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
   typedef long long ll;
   // vector<int> a;
   // vector<int> b;
   int a[3000];
   int b[3000];
   ll n;
   ll k;
   ll p;
   cin >> n >> k >> p;

   for  (ll i = 0; i < n; i++) {
      // ll x;
      // cin >> x;
      // a.push_back(x);
      cin >> a[i];
   }
   sort(a, a+n);
   for  (ll i = 0; i < k; i++) {
      // ll x;
      // cin >> x;
      // b.push_back(x);
      cin >> b[i];
   }
   sort(b, b + k);

   const ll inf = 1e17;

   for (ll i = 0; i < n; i++) {
      cout << "person: " << a[i] << "\n";
   }
   for (ll i = 0; i < k; i++) {
      cout << "key: " << b[i] << "\n";
   }
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