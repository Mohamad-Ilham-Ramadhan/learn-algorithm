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

int main()
{

   cout << __popcount(31) << "\n";
   cout << log2(31);
   return 0;
}
