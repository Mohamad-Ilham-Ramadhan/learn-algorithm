''' 
   (linked list) leetcode: 138. Copy List with Random Pointer (medium)

   A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

   Construct a deep copy of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

   For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

   Return the head of the copied linked list.

   The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:
      - `val`: an integer representing `Node.val`
      - random_index: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

   Your code will only be given the `head` of the original linked list.

   

   Example 1:

      Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
      Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

   Example 2:

      Input: head = [[1,1],[2,1]]
      Output: [[1,1],[2,1]]

   Example 3:


      Input: head = [[3,null],[3,0],[3,null]]
      Output: [[3,null],[3,0],[3,null]]
   

   Constraints:
      - 0 <= n <= 1000
      - -10^4 <= Node.val <= 10^4
      - Node.random is null or is pointing to some node in the linked list.

   Related Topics:
      (Hash Table) (Linked List)

   ===============================================

   Soluton by NeetCode:

   Leetcode submission:
      runtime: 55 ms, beats 42.19%
      memory: 17.3 MB, beats 37.37%
'''

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
   oldToCopy = {None: None} 

   cur = head 
   while cur: 
      copy = Node(cur.val)
      oldToCopy[cur] = copy 
      cur = cur.next 
   
   cur = head 
   while cur: 
      copy = oldToCopy[cur]
      copy.next = oldToCopy[cur.next]
      copy.random = oldToCopy[cur.random]
      cur = cur.next 
   
   return oldToCopy[head]

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
h14 = Node(1,None,None) 
h13 = Node(10,h14,None)
h12 = Node(11,h13,h14)
h11 = Node(13,h12,None)
h10 = Node(7,h11,None)
h11.random = h10 
h13.random = h12
h10.index = 0

# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
h22 = Node(3,None, None)
h21 = Node(3,h22, None)
h20 = Node(3,h21, None)
h21.random = h20
# print('RESULT :', copyRandomList(h10))

