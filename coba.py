'''
  Leetcode: 139. Word Break (medium)

  Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

  Note that the same word in the dictionary may be reused multiple times in the segmentation.

  

  Example 1:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

  Example 2:
    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
    Note that you are allowed to reuse a dictionary word.

  Example 3:
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false
  

  Constraints:
    - 1 <= s.length <= 300
    - 1 <= wordDict.length <= 1000
    - 1 <= wordDict[i].length <= 20
    - s and wordDict[i] consist of only lowercase English letters.
    - All the strings of wordDict are unique.
'''

class TrieNode:
  def __init__(self):
    self.isEnd = False 
    self.children = {}

def wordBreak(s, wordDict): 
  # construct trie 
  trie = TrieNode()

  for i in range(len(wordDict)):
    w = wordDict[i]
    pointer = trie
    for c in w:
      if c not in pointer.children:
        pointer.children[c] = TrieNode()
      pointer = pointer.children[c]
    pointer.isEnd = True
  
  store = ['']
  si = 0; # store index
  pointer = trie 
  for i in range(len(s)):
    c = s[i]
    print('store', store)
    print('char', c, 'si', si)
    print('pointer', pointer.children)
    if c in trie.children:
      print('ROOT CHILDREN', pointer.isEnd, si - 1)
      if pointer.isEnd:
        print('NEW or SPACE')
        store.append(c)
        si += 1
        pointer = trie.children[c]
      else: 
        if c in pointer.children:
          store[si] += c 
          pointer = pointer.children[c]
        else: 
          return False
    else:
      print('NOT ROOT CHILDREN')
      if c in pointer.children:
        print('ADD')
        store[si] += c
        pointer = pointer.children[c]
      else: 
        print('REJOIN', store[si])
        # rejoin 
        store[si - 1] += store[si]
        store.pop()
        si -= 1
        if (si == -1): return False
        # reset pointer 
        pointer = trie
        for x in store[si]:
          if x not in pointer.children:
            return False
          else:
            pointer = pointer.children[x]

        store[si] += c 
        print('pointer.children', pointer.children)
        pointer = pointer.children[c] 
  # check words 
  print('last pointer', pointer.isEnd)
  print('store', store)

  # last rejoin
  if not pointer.isEnd:
    store[si - 1] += store[si]
    store.pop()
    si -= 1
    if (si == -1): return False
    # reset pointer 
    pointer = trie
    print('store', store)
    for x in store[si]:
      if x not in pointer.children:
        return False
      else:
        pointer = pointer.children[x]

  return pointer.isEnd



# s1 = 'leetcode'; wd1 = ['leet', 'code']; # expect: true
# s2 = 'applepenapple'; wd2 = ['apple', 'pen']; # expect: true
# x2 = 'applepenapple'; xd2 = ['apple', 'ap', 'pp', 'pen']
# s3 = 'catsandog'; wd3 = ['cats', 'dog', 'sand', 'and', 'cat']; # expect: false
# s4 = 'catandcats'; wd4 = ['cat', 'and', 'cats']; # expect: true
# s5 = 'catsandcat'; wd5 = ['cat', 'and', 'cats']; # expect: true
# s6 = 'ab'; wd6 = ['a', 'b'] # expect: true
# s7 = 'bb'; wd7 = ['a', 'b', 'bb', 'bbb', 'bbbb'] # expect: true, output: false
# s8 = 'cars'; wd8 = ['car', 'ca', 'rs']
# s9 = 'a'; wd9 = ['b']; # expect: false,
# s10 = 'aaaaaaa'; wd10 = ["aaaa","aa"]; # expect: false, output: true
# s11 = 'aaaaaaa'; wd11 = ['aaaa', 'aaa'] # expect: true, output: false
# s12 = 'catscat'; wd12 = ['cat', 'cats'] # expect: true
# s13 = 'ccbb'; wd13 = ['bc', 'cb']
# s14 = "catsandogcat"; wd14 = ["cats","dog","sand","and","cat","an"] # expect: True, output: false
'''
get initial store
  temp = [cats, cat]
  else 
    False


tempStore = []
loop temp 
  #1
  cats
  add tempStore -> [[cats, 4]]
  #2
  cat
  add tempStore -> [[cats, 4], [cat, 3]]

  loop store [[cats, 4], [cat, 3]]
    #1 store ['cats', 4]
    temp = [and, an]
    loop temp 
      #1 temp 'and'
      i = 4
      char = a
      and
      add store -> [[cats, 4], [cat, 3], [cats and, 7]]
      
      #2 temp 'an'
      i = 4
      char = a
      an
      add store -> [[cats, 4], [cat, 3], [cats and, 7], [cats an, 6]]
    
    #2 store ['cat', 3]
    temp = [sand]
      loop temp 
        #1 temp 'sand'
        i = 3
        char = s
        sand
        add store -> [[cats, 4], [cat, 3], [cats and, 7], [cats an, 6], [cat sand, 7]]

'''
def wordBreak2(s, wordDict):
  map = {}
  # built map
  for i in range(len(wordDict)): 
    # print('map', map)
    fc = wordDict[i][0]
    # print('fc', fc,)
    if fc in map:
      map[fc].append( wordDict[i] )
    else: 
      map[fc] = [ wordDict[i] ]
  
  '''
  loop w.length - 1 + s current index
  cat cats 
  res
  cats an dog cat

  s14 = "catsandogcat"; wd14 = ["cats","dog","sand","and","cat","an"] # expect: True, output: false

  cat
  cats 
  '''
  # i = float('inf')
  # if s[0] in map: 
  #   for [w, j] in map[s[0]]:
  #       store.append([w, j])  
  #       i = min(i, j)
  # else:
  #   return False

  # i = float('inf')
  # temp = []
  # for w in wordDict:
  #   if w[0] == s[0]:
  #     temp.append()
  #     i = min(i, len(w) - 1)
  

  i = 0
  store = [['', 0]]
  x = 0
  # print('s length', len(s))
  while len(store) > 0 and i < len(s): 
    x += 1 
    # if x >= 4: break
    # print('i', i)
    tempStore = []
    nextI = float('inf')
    for [sw, j] in store:
      # print('store word', sw, 'store index', j)
      if j >= len(s): 
        tempStore.append([sw, j])
        continue
      c = s[j]
      # find temp 
      temp = map[c] if c in map else []
      if len(temp) == 0: continue 
      # print('temp', temp)

      for w in temp: 
        # print('temp word', w)
        nextI = min(nextI, len(w) + j)
        sj = j
        isAdd = True
        for wc in w:
          if sj >= len(s):
            # print('out of range s when check temp char with s char')
            isAdd = False 
            break
          sc = s[sj]
          # print('wc', wc, 'sc', sc)
          sj += 1
          if wc != sc: 
            isAdd = False 
            break
        if isAdd:
          tempStore.append([sw + w + ' ', sj])
        # print('tempStore', tempStore)
    store = tempStore
    i = nextI
    # print('store inside', store)  
  # print('store', store)
  # print('map after', map)
  return True if len(store) > 0 else False
  '''
      loop store [[cats, 4], [cat, 3]]
      #1 store ['cats', 4]
      temp = [and, an]
      loop temp 
        #1 temp 'and'
        i = 4
        char = a
        and
        add store -> [[cats, 4], [cat, 3], [cats and, 7]]
        
        #2 temp 'an'
        i = 4
        char = a
        an
        add store -> [[cats, 4], [cat, 3], [cats and, 7], [cats an, 6]]
      
      #2 store ['cat', 3]
      temp = [sand]
        loop temp 
          #1 temp 'sand'
          i = 3
          char = s
          sand
          add store -> [[cats, 4], [cat, 3], [cats and, 7], [cats an, 6], [cat sand, 7]]
    '''


# print(wordBreak2(s14, wd14))

# Time limit exceeded
# from collections import deque
from datetime import datetime
def wordBreak3(s, wordDict): 
  map = {}

  for w in wordDict:
    c = w[0]
    if c in map:
      map[c].append(w)
    else: 
      map[c] = [w]

  store = deque([0])

  while len(store) > 0: 
    i = store.pop()

    if i >= len(s):
      return True

    c = s[i]
    tempStore = []
    # print('char', c)
    if c in map: 
      for wm in map[c]: 
        # print('map[c]', map[c])
        # print('i', i, 'len(wm)', len(wm))
        sw = s[i: i + len(wm)]
        # print('wm', wm, 'sw', sw)
        if wm == sw: 
          tempStore.append(i + len(wm))

    # else:
    #   return False
    # print('tempStore', tempStore)
    store.extendleft(tempStore)
  
  # print('store after', store)
  # print('s length', len(s))
  return False

# implement NeetCode's explanation
def wordBreak4(s, wordDict):
  dp = [False for i in range(len(s) + 1)]
  dp[len(s)] = True
  # print('dp', len(dp), 's', len(s))
  store = []

  for i in range(len(s) - 1, -1, -1): 
    char = s[i]
    for w in wordDict:
      if char == w[0] and i + len(w) <= len(s) and s[i: i + len(w)] == w and dp[i + len(w)]:
        dp[i] = True
    # print('char', char)
  
  return dp[0]
  
  print('dp after', dp)
s1 = 'leetcode'; wd1 = ['leet', 'code']; # expect: true
s2 = 'applepenapple'; wd2 = ['apple', 'pen']; # expect: true
x2 = 'applepenapple'; xd2 = ['apple', 'ap', 'pp', 'pen'] # expect: true
s3 = 'catsandog'; wd3 = ['cats', 'dog', 'sand', 'and', 'cat']; # expect: false
s4 = 'catandcats'; wd4 = ['cat', 'and', 'cats']; # expect: true
s5 = 'catsandcat'; wd5 = ['cat', 'and', 'cats']; # expect: true
s6 = 'ab'; wd6 = ['a', 'b'] # expect: true
s7 = 'bb'; wd7 = ['a', 'b', 'bb', 'bbb', 'bbbb'] # expect: true, output: false
s8 = 'cars'; wd8 = ['car', 'ca', 'rs']
s9 = 'a'; wd9 = ['b']; # expect: false,
s10 = 'aaaaaaa'; wd10 = ["aaaa","aa"]; # expect: false, output: true
'''
  dp[7] = false 
  dp[6] = false 
  dp[5] = true | dp[4] = true | dp[3] = true | dp[2] = true | dp[1] = true | dp[0] = true
'''
s11 = 'aaaaaaa'; wd11 = ['aaaa', 'aaa'] # expect: true, output: false
s12 = 'catscat'; wd12 = ['cat', 'cats'] # expect: true
s13 = 'ccbb'; wd13 = ['bc', 'cb']
s14 = "catsandogcat"; wd14 = ["cats","dog","sand","and","cat","an"] # expect: True, output: false
s15 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wd15 = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

start = datetime.timestamp(datetime.now())
print('result: ', wordBreak4(s15, wd15))
print('runtime: ', start - datetime.timestamp(datetime.now()))
