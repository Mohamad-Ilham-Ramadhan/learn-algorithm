'''
   (linked list) leetcode : 146. LRU Cache (medium). Companies: [Twitch]

   Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

   Implement the `LRUCache` class:
      - `LRUCache(int capacity)` Initialize the LRU cache with positive size `capacity`.
      - `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
      - `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.
      - The functions `get` and `put` must each run in `O(1)` average time complexity.

   

   Example 1:

      Input
         ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
         [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
      Output
         [null, null, null, 1, null, -1, null, -1, 3, 4]

      Explanation
         LRUCache lRUCache = new LRUCache(2);
         lRUCache.put(1, 1); // cache is {1=1}
         lRUCache.put(2, 2); // cache is {1=1, 2=2}
         lRUCache.get(1);    // return 1
         lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
         lRUCache.get(2);    // returns -1 (not found)
         lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
         lRUCache.get(1);    // return -1 (not found)
         lRUCache.get(3);    // return 3
         lRUCache.get(4);    // return 4
   

   Constraints:
      1 <= capacity <= 3000
      0 <= key <= 10^4
      0 <= value <= 10^5
      At most 2 * 10^5 calls will be made to get and put.

   Related Topics
      (Hash Table) (Linked List) (Design) (Doubly-Linked List)

   ============================================

   Solution by NeetCode

   leetcode submission: 
      runtime: 861 ms, 36.66%
      memory: 78.5 MB, 49.32%
'''
class Node: 
   def __init__(self, key, val):
      self.key, self.val = key, val
      self.prev = self.next = None 

class LRUCache:

   def __init__(self, capacity):
      self.cap = capacity
      self.cache = {} # map key to node

      # left=LRU, right=most recent
      self.left, self.right = Node(0,0), Node(0,0)
      self.left.next, self.right.prev = self.right, self.left 

   # remove node from list
   def remove(self, node):
      prev, nxt = node.prev, node.next
      prev.next, nxt.prev = nxt, prev 

   # insert at right
   def insert(self, node):
      prev, nxt = self.right.prev, self.right 
      prev.next = nxt.prev = node
      node.next, node.prev = nxt, prev

   def get(self, key):
      if key in self.cache: 
         self.remove(self.cache[key])
         self.insert(self.cache[key])
         return self.cache[key].val
      return -1

   def put(self, key, value) -> None:
      if key in self.cache:
         self.remove(self.cache[key])
      self.cache[key] = Node(key, value)
      self.insert(self.cache[key])

      if len(self.cache) > self.cap: 
         # remove from the list and delete the LRU from the hashmap 
         lru = self.left.next 
         self.remove(lru)
         del self.cache[lru.key]

lru = LRUCache(2)
lru.put(2,1)
lru.put(1,1)
print('LIST :', lru.listView())
lru.put(2,3)
print('LIST :', lru.listView())
lru.put(4,1)
print('LIST :', lru.listView())
'''
   ["LRUCache","put","put","put","put","get","get"]
   [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
   output: [null,null,null,null,null,1,-1]
   expect: [null,null,null,null,null,-1,3]

   [[4],[1,1],[2,2],[3,3],[4,4],[2],[5,5],[6,6],[1],[2],[3],[4],[5],[6],[7,7],[2],[4],[5],[6],[7]]

   1->2->3->[4]
   1->[2]->3->4 get[2]
   [2]->4->5->6 put[5,6]
   2->4->5->[6] get[1,2,3,4,5,6]
   4->5->[6]->7 put[7]  

   ["LRUCache","put","put","put","put","get","put","put","put","get","get","get","get","get","get","get","put","put","get","get","get","get","get","get"]
   [[4],[1,1],[2,2],[3,3],[4,4],[2],[5,5],[6,6],[7,7],[1],[7],[3],[4],[5],[6],[2],[8,8],[9,9],[2],[5],[6],[7],[8],[9]]

   1->2->3->4
   1->2->3->4 put[1,2,3,4]
   1->3->4->2 get[2] '2'
   2->5->6->7 put[5,6,7]
   7->5->6->2 get[1,7,3,4,5,6,2] '7','5','6','2'
   6->2->8->9 put[8,9]
   2->6->8->9 get[2,5,6,7,8,9] '2','6','8','9'

'''
