'''
   (heap) leetcode: 621. Task Scheduler (medium). Companies (Google)

   Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

   However, there is a non-negative integer `n` that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks.

   Return the least number of units of times that the CPU will take to finish all the given tasks.

   

   Example 1:
      Input: tasks = ["A","A","A","B","B","B"], n = 2
      Output: 8
      Explanation: 
      A -> B -> idle -> A -> B -> idle -> A -> B
      There is at least 2 units of time between any two same tasks.

   Example 2:
      Input: tasks = ["A","A","A","B","B","B"], n = 0
      Output: 6
      Explanation: On this case any permutation of size 6 would work since n = 0.
      ["A","A","A","B","B","B"]
      ["A","B","A","B","A","B"]
      ["B","B","B","A","A","A"]
      ...
      And so on.

   Example 3:
      Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
      Output: 16
      Explanation: 
      One possible solution is
      A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
   

   Constraints:
      - 1 <= task.length <= 10^4
      - tasks[i] is upper-case English letter.
      - The integer n is in the range [0, 100].

   Related topics: 
      (Array) (Hash Table) (Greedy) (Sorting) (Heap) (Counting)
      
   ================================================================

   Solution by myself:
      using max heap
   
   Leetcode submission: 
      runtime: 548 ms, beats 69.10%
      memory: 17 MB, beats 12.7%
   
   
'''
from heapq import heapify, heappush, heappop
def leastInterval(tasks, n):
   if n == 0: return len(tasks)

   # initial count 
   hm = {} 
   for c in tasks: 
      if c in hm: hm[c] += 1
      else: hm[c] = 1 
   
   # create initial heap
   heap = []
   heapify(heap)
   for key in hm: 
      heappush(heap, -hm[key])
   
   total = 0
   while len(heap):
      # initial task for the group
      # ((A) -> B -> C) -> ( (A) -> D -> E) ->( (A) -> F -> G) -> ((A) -> idle -> idle) -> ((A) -> idle -> idle) -> ((A))
      print('total', total, 'len(heap)', len(heap))
      idle = n
      total += 1
      popped = -heappop(heap) - 1
      print('popped out', popped)
      list = [] # temporary storage for the next heap
      if popped > 0: list.append(popped)

      while idle and len(heap): 
         # tasks if any to cooldown the initial tasks
         idle -= 1
         total += 1
         popped = -heappop(heap) - 1
         print('popped in', popped)
         if popped > 0: list.append(popped)

      if len(list) == 0 and len(heap) == 0:
         # all tasks has been done
         break  
      else: 
         print('idle', idle)
         total += idle 
         for num in list:
            heappush(heap, -num)
   
   return total

t1 = ["A","A","A","B","B","B"]; n1 = 2 # 8
t2 = ["A","A","A","A","A","A","B","C","D","E","F","G"]; n2=2  # 16
t3 = ["A","A","A","B","B","B"]; n3 = 0 # 6
t4 = ['C']; n4 = 1
print('RESULT :', leastInterval(t4, n4))
'''
["A","A","A","A","A","A","B","C","D","E","F","G"] n=2 
[6,1]
{5: 1, 1: 4} 
a->b->c
new heap [5,1]
'''