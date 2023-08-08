/*
    Codeforces: (dynamic programming) 548B Mike and Fun (1400)
    link: https://codeforces.com/problemset/problem/548/B
    Tags: brute force, dp, greedy, implementation, *1400

===========================================================

    submission:
        runtime: 218 ms, memory: 1100 KB
*/

#include <bits/stdc++.h>
using namespace std;

/*
5 4 5
0 1 1 0
1 0 0 1
0 1 1 0
1 0 0 1
0 0 0 0
1 1
1 4
1 1
4 2
4 3
output: 
3
4
3
3
4

input #2:
2 2 10
1 1
0 1
1 1
2 1
1 1
2 2
1 1
2 1
2 2
2 2
1 1
1 1
output: 
1
2
2
2
1
1
1
1
2
1
*/

typedef long long ll;
ll n, m, k, q, l, r, x, y, z;
const ll template_array_size = 1e6 + 4967;
ll a[template_array_size];
ll b[template_array_size];
ll c[template_array_size];
string s, t;
ll ans = 0;

ll best[505];
ll mat[505][505];

void solve_row(ll i) {
   ll f[m + 1];
   f[0] = 0;

   ll ans = 0;
   for (ll j = 1; j <= m; j++) {
      if (mat[i][j - 1] == 0) {
         f[j] = 0;
      } else {
         f[j] = f[j - 1] + 1;
      }
      ans = max(ans, f[j]);
   }
   cout << "ans: " << ans << '\n';
   best[i] = ans;
};

void solve(int tc = 0) {
   memset(best, 0, sizeof(best));

   cin >> n >> m >> q;

   for (ll i = 0; i < n; i++) {
      for (ll j = 0; j < m; j++) {
         cin >> mat[i][j];
      }
   }

   for (ll i = 0; i < n; i++) solve_row(i);
   cout << "\n";
   for (ll i = 0; i < q; i++) {
      ll r, c;
      cin >> r >> c;
      --r; --c;
      mat[r][c] ^= 1;

      solve_row(r);

      ll ans = 0;
      for (ll j = 0; j < n; j++) ans = max(ans, best[j]);
      cout << ans << '\n';
   }
}
int main()
{
   solve();
   // int n, m, q;
   // cin >> n >> m >> q;
   // vector<vector<int>> grid;
   // int dp[n];

   // for (int i = 0; i < n; i++) {
   //    vector<int> row;
   //    grid.push_back(row);
   //    int cm = 0; // current max length of consecutive 1
   //    int total = 0; // current length of consecutive 1
   //    for (int j = 0; j < m; j++) {
   //       int z;
   //       cin >> z;
   //       grid[i].push_back(z);
   //       if (z == 1) {
   //          total++;
   //       } else {
   //          cm = max(cm, total);
   //          total = 0;
   //       }
   //    }
   //    cm = max(cm, total);
   //    dp[i] = cm;
   // }

   // // query
   // for (int k = 0; k < q; k++) {
   //    int i,j;
   //    cin >> i >> j;
   //    i--; j--;

   //    grid[i][j] ^= 1;
   //    // recalculate queried row
   //    int cm = 0;
   //    int total = 0;
   //    for (int c = 0; c < m; c++) {
   //       if (grid[i][c] == 1) {
   //          total++;
   //       } else {
   //          cm = max(cm, total);
   //          total = 0;
   //       }
   //    }
   //    cm = max(cm, total);
   //    dp[i] = cm;

   //    for (int v = 0; v < n; v++) {
   //       cm = max(cm, dp[v]);
   //    }
   //    cout << cm << "\n";
   // }
   
   return 0;
}
