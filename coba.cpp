#include <bits/stdc++.h>
using namespace std;


int main()
{
   // vector<int> subset = {2,4,7,8}; x
   // int w = 14; int n = 4;
   /*
      {
         0: true
         1: false
         2: true
         3: false
         4: true
         5: false
         6: true
         7: true
         8: true
         9: false
         10: false
         11: false
         12: false
         13: true
         14: false
      }
   */


   int n, w;
 
   cin >> n >> w;
   cout << "n " << n << "w " << w << "\n";
   bool can[w+1];
   for (int i = 0; i < w+1; i++) {
      can[i] = false;
   }

   can[0] = true;
   for (int id = 0; id < n; id++) {
      int x;
      cin >> x;
      cout << "x " << x << "\n";
      for (int i = w; i >= x; i--) {
         if (can[i-x]) {
            cout << "true: " << "i " << i << "\n";
            can[i] = true;
         }
      }
   }
   int x = 0;
   for (int i : can) {
      cout << "x: " << x << " ";
      if (i) {
         cout << "YES!";
      } else {
         cout << "No!";
      }
      x++;
   }
   return 0;
}

/**
 {
   0:    true
   1:    false
   2:    true
   3:    false
   4:    true
   5:    false
   6:    true
   7:    true
   8:    true
   9:    true
   10:   true
   11:   true
   12:   true
   13:   true
   14:   true
 }
*/