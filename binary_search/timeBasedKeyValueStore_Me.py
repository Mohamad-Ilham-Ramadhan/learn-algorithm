'''
   (binary search) leetcode: 981. Time based key-value store (medium)

   Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

   Implement the `TimeMap` class:

      - `TimeMap()` Initializes the object of the data structure.
      - `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time timestamp.
      - `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

   Example 1:

      Input
      ["TimeMap", "set", "get", "get", "set", "get", "get"]
      [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
      Output
      [null, null, "bar", "bar", null, "bar2", "bar2"]

      Explanation
      TimeMap timeMap = new TimeMap();
      timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
      timeMap.get("foo", 1);         // return "bar"
      timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
      timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
      timeMap.get("foo", 4);         // return "bar2"
      timeMap.get("foo", 5);         // return "bar2"
   
   Constraints:
      - 1 <= key.length, value.length <= 100
      - key and value consist of lowercase English letters and digits.
      - 1 <= timestamp <= 10^7
      - All the timestamps timestamp of set are strictly increasing.
      - At most 2 * 10^5 calls will be made to set and get.

   Related topics:
      (hash table) (string) (binary search) (design)
   
   =============================================================================

   Solution by myself:
      hash map
         {key: [[]]} the element of array is array of [timestamp, value] (attempt #1), on attempt #2 I use tupple
      binary search
   
   leetcode submission: 
      #1 array element is an array
         runtime: 766 ms, beats 75.84%
         memory: 74.8 MB, beats 16.49%

      #2 array element is a tuple
         runtime: 764 ms, beats 76.29%
         memory: 73.9 MB, beats 75.29%
'''

'''
   [1,3,6,10,11,12,13]
   limit = 7
   l = 2
   r = 2
   m = 2 (6)
   res = [1,3]
   10 <= limit:
      res = [t,v]
      l = m + 1
   else
      r = m - 1
   return res
'''
class TimeMap:

   def __init__(self):
      self.hm = {}

   def set(self, key: str, value: str, timestamp: int) -> None:
      if key in self.hm: 
         # self.hm[key].append([timestamp, value])

         # attempt #2
         self.hm[key].append( (timestamp, value) )
      else: 
         # self.hm[key] = [[timestamp, value]]

         # attempt #2
         self.hm[key] = [(timestamp, value)]

   def get(self, key: str, timestamp: int) -> str:
      if key not in self.hm:
         return ''
      arr = self.hm[key]
      # binary search reside here
      l = 0 
      r = len(arr) - 1
      m = (l + r) // 2
      result = [0,'']
      while l <= r:
         me = arr[m] # mid element 
         if me[0] <= timestamp: 
            result = me 
            l = m + 1
         else :
            r = m - 1
      
      return result[1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


tupoks = (3, 'bar')
print('tupoks', tupoks[0], tupoks[1])