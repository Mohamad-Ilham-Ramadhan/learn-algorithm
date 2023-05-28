/*
   LeetCode: 212. Word Search II (hard)

   Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board.

   Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.


   Example 1:
      [o a a n]
      [e t a e]
      [i h k r]
      [i f l v]

   Input: 
      board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], 
      words = ["oath","pea","eat","rain"]
      Output: ["eat","oath"]

   Example 2:
      [a b]
      [c d]

   Input: 
      board = [["a","b"],["c","d"]], 
      words = ["abcb"]
      Output: []
   

   Constraints:
      - m == board.length
      - n == board[i].length
      - 1 <= m, n <= 12
      - board[i][j] is a lowercase English letter.
      - 1 <= words.length <= 3 * 104
      - 1 <= words[i].length <= 10
      - words[i] consists of lowercase English letters.
      - All the strings of words are unique.

   Solution by myself: 
      This is so hard to explain
      So many steps and complex

   LeetCode submission:
      - Runtime: 3932 ms, beats 21.23%
      - Memory: 59 MB, beats 10.93%
*/

/*
   [o a a n]
   [e t a e]
   [i h k r]
   [i f l v]

   Input: 
      board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], 
      words = ["oath","pea","eat","rain"]
      Output: ["eat","oath"]

    o    a   a    n  e
   a e  a t  n a  e  t
   a i  n h    k  r  a
   n i    f    l  v  e
*/

function findWords(board, words) {
   let boardChars = new Set();
   let possibleWords = [];
   let maxLengthPossible = 0; // determine length of traverse recursion

   // collect a unique chars in the board
   for (let i = 0; i < board.length; i++) {
      const y = board[i];
      for (let x = 0; x < y.length; x++) {
         const char = board[i][x];
         boardChars.add(char);
      }
   }

   // console.log('boardChars: ', boardChars);

   // filter all possible words based on chars in the board and chars in the words
   for (let word of words) {
      let isPossible = true;
      for (let i = 0; i < word.length; i++) {
         const char = word[i];
         if (!boardChars.has(char)) {
            isPossible = false;
            break;
         }
      }
      if (isPossible) {
         maxLengthPossible = word.length > maxLengthPossible ? word.length : maxLengthPossible;
         possibleWords.push(word)
      };
   }
   class TrieNode {
      constructor() {
         this.child = {};
         this.end = false;
      }
   }

   function createTrie(words) {
      let trie = new TrieNode();
      for (let i = 0; i < words.length; i++) {
         const word = words[i];
         let pointer = trie;
         for (let j = 0; j < word.length; j++) {
            const char = word[j];
            if (!(char in pointer.child)) {
               pointer.child[char] = new TrieNode();
            }
            pointer = pointer.child[char];
         }
         pointer.end = true;
      }
      return trie;
   }
   // console.log('possible words:', possibleWords);
   // console.log('max length:', maxLengthPossible);
   let trie = createTrie(possibleWords);
   // console.log('possible trie:', trie);

   function traverse(board, visited, coor, curStr, triePointer) {
      // console.log('===================== ');
      const x = coor[0]; // current x
      const y = coor[1]; // current y
      let count = 0; // traverse count;

      // console.log('curStr:', curStr, 'coor', coor[0], coor[1]);
      // console.log('in traverse result', result);
      // console.log('trie', Object.assign({},trie)   );

      if (triePointer.end && !result.has(curStr)) {
         // console.log('result add', curStr)
         result.add(curStr);
      }
      if (curStr.length >= maxLengthPossible) {
         // console.log('STOP curstr.length > max length', curStr, result)
         return;
      }

      if (result.size >= possibleWords.length) {
         // console.log('STOP result penuh');
         return;
      };




      // console.log('traverse more', curStr, triePointer, visited);
      // console.log(!visited.has(`${x},${y+1}`) && board[y+1] !== undefined);

      if (!visited.has(`${x - 1},${y}`) && board[y][x - 1] !== undefined) {
         const copyVisited = new Set(visited);
         const char = board[y][x - 1];
         // console.log('next char left', char);
         let newTriePointer = Object.assign({}, triePointer);
         if (char in newTriePointer.child) {
            newTriePointer = newTriePointer.child[char];
            traverse(board, copyVisited.add(`${x - 1},${y}`), [x - 1, y], curStr + char, newTriePointer);
            count++;
         }
      }
      if (!visited.has(`${x},${y - 1}`) && board[y - 1] !== undefined) {
         const copyVisited = new Set(visited);
         const char = board[y - 1][x];
         // console.log('next char top', char);
         let newTriePointer = Object.assign({}, triePointer);
         if (char in newTriePointer.child) {
            newTriePointer = newTriePointer.child[char];
            traverse(board, copyVisited.add(`${x},${y - 1}`), [x, y - 1], curStr + char, newTriePointer);
            count++;
         }
      }
      if (!visited.has(`${x + 1},${y}`) && board[y][x + 1] !== undefined) {
         const copyVisited = new Set(visited);
         const char = board[y][x + 1];
         // console.log('next char right', char, 'y', y, 'x', x+1, curStr);
         let newTriePointer = Object.assign({}, triePointer);
         if (char in newTriePointer.child) {
            newTriePointer = newTriePointer.child[char];
            traverse(board, copyVisited.add(`${x + 1},${y}`), [x + 1, y], curStr + char, newTriePointer);
            count++;
         }
      }
      // console.log('NEAR BOTTOM', curStr);
      if (!visited.has(`${x},${y + 1}`) && board[y + 1] !== undefined) {
         const copyVisited = new Set(visited);
         const char = board[y + 1][x];
         // console.log('next char bottom', char, 'y', y+1, 'x', coor[0], curStr);

         let newTriePointer = Object.assign({}, triePointer);
         if (char in newTriePointer.child) {
            newTriePointer = newTriePointer.child[char];
            traverse(board, copyVisited.add(`${x},${y + 1}`), [x, y + 1], curStr + char, newTriePointer);
            count++;
         }
      }

      // if no cells are traversable
      if (count === 0) {
         // console.log('word', curStr);
         return;
      }

   }

   let result = new Set();

   for (let y = 0; y < board.length; y++) {
      for (let x = 0; x < board[y].length; x++) {
         const char = board[y][x];
         let triePointer = trie;
         if (result.size >= possibleWords.length) {
            // console.log('STOP result penuh');
            break;
         };
         if (!(char in triePointer.child)) {
            continue;
         }
         triePointer = triePointer.child[char];
         // console.log('START char', char);
         traverse(board, (new Set()).add(`${x},${y}`), [x, y], char, triePointer);
      }
   }

   // console.log('result', Array.from(result));
   return Array.from(result);
}

const board1 = [
   ['o', 'a', 'a', 'n'],
   ['e', 't', 'a', 'e'],
   ['i', 'h', 'k', 'r'],
   ['i', 'f', 'l', 'v'],
]; const words1 = ['eat', 'oath', 'pea', 'rain'];
const board2 = [
   ['a', 'b'],
   ['c', 'd'],
]; const words2 = ['abcd', 'bdc', 'a', 'ac'];
const board3 = [
   ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
]; // 12 x 12
const words3 = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"];
const board4 = [
   ["a", "a", "a", "a"],
   ["a", "a", "a", "a"],
   ["a", "a", "a", "a"],
   ["a", "a", "a", "a"],
]; const words4 = ["a", "aa", "aaa", "aaaa"]; // 63ms, 0.063 detik
const board5 = [
   ["a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a"],
   ["a", "a", "a", "a", "a"],
]; const words5 = ["a", "aa", "aaa", "aaaa", "aaaaa", 'aaaaaa']; // 6300 ms, 6.3 detik
const board6 = [
   ["a", "a", "a", "a", "a", 'a'],
   ["a", "a", "a", "a", "a", 'a'],
   ["a", "a", "a", "a", "a", 'a'],
   ["a", "a", "a", "a", "a", 'a'],
   ["a", "a", "a", "a", "a", 'a'],
   ["a", "a", "a", "a", "a", 'a'],
]; const words6 = ["a", "aa", "aaa", "aaaa", "aaaaa", 'aaaaaa']; // 6300 ms, 6.3 detik
const board7 = [
   ['a']
]; const words7 = ['a'];

const board8 = [
   ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
   ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
   ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
   ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
   ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
   ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
   ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
   ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
   ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
   ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"]
];
const words8 = ["ababababaa", "ababababab", "ababababac", "ababababad", "ababababae", "ababababaf", "ababababag", "ababababah", "ababababai", "ababababaj", "ababababak", "ababababal", "ababababam", "ababababan", "ababababao", "ababababap", "ababababaq", "ababababar", "ababababas", "ababababat", "ababababau", "ababababav", "ababababaw", "ababababax", "ababababay", "ababababaz", "ababababba", "ababababbb", "ababababbc", "ababababbd", "ababababbe", "ababababbf", "ababababbg", "ababababbh", "ababababbi", "ababababbj", "ababababbk", "ababababbl", "ababababbm", "ababababbn", "ababababbo", "ababababbp", "ababababbq", "ababababbr", "ababababbs", "ababababbt", "ababababbu", "ababababbv", "ababababbw", "ababababbx", "ababababby", "ababababbz", "ababababca", "ababababcb", "ababababcc", "ababababcd", "ababababce", "ababababcf", "ababababcg", "ababababch", "ababababci", "ababababcj", "ababababck", "ababababcl", "ababababcm", "ababababcn", "ababababco", "ababababcp", "ababababcq", "ababababcr", "ababababcs", "ababababct", "ababababcu", "ababababcv", "ababababcw", "ababababcx", "ababababcy", "ababababcz", "ababababda", "ababababdb", "ababababdc", "ababababdd", "ababababde", "ababababdf", "ababababdg", "ababababdh", "ababababdi", "ababababdj", "ababababdk", "ababababdl", "ababababdm", "ababababdn", "ababababdo", "ababababdp", "ababababdq", "ababababdr", "ababababds", "ababababdt", "ababababdu", "ababababdv", "ababababdw", "ababababdx", "ababababdy", "ababababdz", "ababababea", "ababababeb", "ababababec", "ababababed", "ababababee", "ababababef", "ababababeg", "ababababeh", "ababababei", "ababababej", "ababababek", "ababababel", "ababababem", "ababababen", "ababababeo", "ababababep", "ababababeq", "ababababer", "ababababes", "ababababet", "ababababeu", "ababababev", "ababababew", "ababababex", "ababababey", "ababababez", "ababababfa", "ababababfb", "ababababfc", "ababababfd", "ababababfe", "ababababff", "ababababfg", "ababababfh", "ababababfi", "ababababfj", "ababababfk", "ababababfl", "ababababfm", "ababababfn", "ababababfo", "ababababfp", "ababababfq", "ababababfr", "ababababfs", "ababababft", "ababababfu", "ababababfv", "ababababfw", "ababababfx", "ababababfy", "ababababfz", "ababababga", "ababababgb", "ababababgc", "ababababgd", "ababababge", "ababababgf", "ababababgg", "ababababgh", "ababababgi", "ababababgj", "ababababgk", "ababababgl", "ababababgm", "ababababgn", "ababababgo", "ababababgp", "ababababgq", "ababababgr", "ababababgs", "ababababgt", "ababababgu", "ababababgv", "ababababgw", "ababababgx", "ababababgy", "ababababgz", "ababababha", "ababababhb", "ababababhc", "ababababhd", "ababababhe", "ababababhf", "ababababhg", "ababababhh", "ababababhi", "ababababhj", "ababababhk", "ababababhl", "ababababhm", "ababababhn", "ababababho", "ababababhp", "ababababhq", "ababababhr", "ababababhs", "ababababht", "ababababhu", "ababababhv", "ababababhw", "ababababhx", "ababababhy", "ababababhz", "ababababia", "ababababib", "ababababic", "ababababid", "ababababie", "ababababif", "ababababig", "ababababih", "ababababii", "ababababij", "ababababik", "ababababil", "ababababim", "ababababin", "ababababio", "ababababip", "ababababiq", "ababababir", "ababababis", "ababababit", "ababababiu", "ababababiv", "ababababiw", "ababababix", "ababababiy", "ababababiz", "ababababja", "ababababjb", "ababababjc", "ababababjd", "ababababje", "ababababjf", "ababababjg", "ababababjh", "ababababji", "ababababjj", "ababababjk", "ababababjl", "ababababjm", "ababababjn", "ababababjo", "ababababjp", "ababababjq", "ababababjr", "ababababjs", "ababababjt", "ababababju", "ababababjv", "ababababjw", "ababababjx", "ababababjy", "ababababjz", "ababababka", "ababababkb", "ababababkc", "ababababkd", "ababababke", "ababababkf", "ababababkg", "ababababkh", "ababababki", "ababababkj", "ababababkk", "ababababkl", "ababababkm", "ababababkn", "ababababko", "ababababkp", "ababababkq", "ababababkr", "ababababks", "ababababkt", "ababababku", "ababababkv", "ababababkw", "ababababkx", "ababababky", "ababababkz", "ababababla", "abababablb", "abababablc", "ababababld", "abababable", "abababablf", "abababablg", "abababablh", "ababababli", "abababablj", "abababablk", "ababababll", "abababablm", "ababababln", "abababablo", "abababablp", "abababablq", "abababablr", "ababababls", "abababablt", "abababablu", "abababablv", "abababablw", "abababablx", "abababably", "abababablz", "ababababma", "ababababmb", "ababababmc", "ababababmd", "ababababme", "ababababmf", "ababababmg", "ababababmh", "ababababmi", "ababababmj", "ababababmk", "ababababml", "ababababmm", "ababababmn", "ababababmo", "ababababmp", "ababababmq", "ababababmr", "ababababms", "ababababmt", "ababababmu", "ababababmv", "ababababmw", "ababababmx", "ababababmy", "ababababmz", "ababababna", "ababababnb", "ababababnc", "ababababnd", "ababababne", "ababababnf", "ababababng", "ababababnh", "ababababni", "ababababnj", "ababababnk", "ababababnl", "ababababnm", "ababababnn", "ababababno", "ababababnp", "ababababnq", "ababababnr", "ababababns", "ababababnt", "ababababnu", "ababababnv", "ababababnw", "ababababnx", "ababababny", "ababababnz", "ababababoa", "ababababob", "ababababoc", "ababababod", "ababababoe", "ababababof", "ababababog", "ababababoh", "ababababoi", "ababababoj", "ababababok", "ababababol", "ababababom", "ababababon", "ababababoo", "ababababop", "ababababoq", "ababababor", "ababababos", "ababababot", "ababababou", "ababababov", "ababababow", "ababababox", "ababababoy", "ababababoz", "ababababpa", "ababababpb", "ababababpc", "ababababpd", "ababababpe", "ababababpf", "ababababpg", "ababababph", "ababababpi", "ababababpj", "ababababpk", "ababababpl", "ababababpm", "ababababpn", "ababababpo", "ababababpp", "ababababpq", "ababababpr", "ababababps", "ababababpt", "ababababpu", "ababababpv", "ababababpw", "ababababpx", "ababababpy", "ababababpz", "ababababqa", "ababababqb", "ababababqc", "ababababqd", "ababababqe", "ababababqf", "ababababqg", "ababababqh", "ababababqi", "ababababqj", "ababababqk", "ababababql", "ababababqm", "ababababqn", "ababababqo", "ababababqp", "ababababqq", "ababababqr", "ababababqs", "ababababqt", "ababababqu", "ababababqv", "ababababqw", "ababababqx", "ababababqy", "ababababqz", "ababababra", "ababababrb", "ababababrc", "ababababrd", "ababababre", "ababababrf", "ababababrg", "ababababrh", "ababababri", "ababababrj", "ababababrk", "ababababrl", "ababababrm", "ababababrn", "ababababro", "ababababrp", "ababababrq", "ababababrr", "ababababrs", "ababababrt", "ababababru", "ababababrv", "ababababrw", "ababababrx", "ababababry", "ababababrz", "ababababsa", "ababababsb", "ababababsc", "ababababsd", "ababababse", "ababababsf", "ababababsg", "ababababsh", "ababababsi", "ababababsj", "ababababsk", "ababababsl", "ababababsm", "ababababsn", "ababababso", "ababababsp", "ababababsq", "ababababsr", "ababababss", "ababababst", "ababababsu", "ababababsv", "ababababsw", "ababababsx", "ababababsy", "ababababsz", "ababababta", "ababababtb", "ababababtc", "ababababtd", "ababababte", "ababababtf", "ababababtg", "ababababth", "ababababti", "ababababtj", "ababababtk", "ababababtl", "ababababtm", "ababababtn", "ababababto", "ababababtp", "ababababtq", "ababababtr", "ababababts", "ababababtt", "ababababtu", "ababababtv", "ababababtw", "ababababtx", "ababababty", "ababababtz", "ababababua", "ababababub", "ababababuc", "ababababud", "ababababue", "ababababuf", "ababababug", "ababababuh", "ababababui", "ababababuj", "ababababuk", "ababababul", "ababababum", "ababababun", "ababababuo", "ababababup", "ababababuq", "ababababur", "ababababus", "ababababut", "ababababuu", "ababababuv", "ababababuw", "ababababux", "ababababuy", "ababababuz", "ababababva", "ababababvb", "ababababvc", "ababababvd", "ababababve", "ababababvf", "ababababvg", "ababababvh", "ababababvi", "ababababvj", "ababababvk", "ababababvl", "ababababvm", "ababababvn", "ababababvo", "ababababvp", "ababababvq", "ababababvr", "ababababvs", "ababababvt", "ababababvu", "ababababvv", "ababababvw", "ababababvx", "ababababvy", "ababababvz", "ababababwa", "ababababwb", "ababababwc", "ababababwd", "ababababwe", "ababababwf", "ababababwg", "ababababwh", "ababababwi", "ababababwj", "ababababwk", "ababababwl", "ababababwm", "ababababwn", "ababababwo", "ababababwp", "ababababwq", "ababababwr", "ababababws", "ababababwt", "ababababwu", "ababababwv", "ababababww", "ababababwx", "ababababwy", "ababababwz", "ababababxa", "ababababxb", "ababababxc", "ababababxd", "ababababxe", "ababababxf", "ababababxg", "ababababxh", "ababababxi", "ababababxj", "ababababxk", "ababababxl", "ababababxm", "ababababxn", "ababababxo", "ababababxp", "ababababxq", "ababababxr", "ababababxs", "ababababxt", "ababababxu", "ababababxv", "ababababxw", "ababababxx", "ababababxy", "ababababxz", "ababababya", "ababababyb", "ababababyc", "ababababyd", "ababababye", "ababababyf", "ababababyg", "ababababyh", "ababababyi", "ababababyj", "ababababyk", "ababababyl", "ababababym", "ababababyn", "ababababyo", "ababababyp", "ababababyq", "ababababyr", "ababababys", "ababababyt", "ababababyu", "ababababyv", "ababababyw", "ababababyx", "ababababyy", "ababababyz", "ababababza", "ababababzb", "ababababzc", "ababababzd", "ababababze", "ababababzf", "ababababzg", "ababababzh", "ababababzi", "ababababzj", "ababababzk", "ababababzl", "ababababzm", "ababababzn", "ababababzo", "ababababzp", "ababababzq", "ababababzr", "ababababzs", "ababababzt", "ababababzu", "ababababzv", "ababababzw", "ababababzx", "ababababzy", "ababababzz"];


const start = Date.now();
console.log('RESULT: ', findWords(board8, words8));
console.log('runtime', Date.now() - start);
// function findWords(board, words) {

//    // console.log('left', board[0][-1]);
//    function traverse(board, visited, cur, curStr) {
//       const x = cur[0]; // current x
//       const y = cur[1]; // current y
//       let count = 0; // traverse count;

//       // console.log('trie', Object.assign({},trie)   );

//       if (!visited.has(`${x - 1},${y}`) && board[y][x - 1] !== undefined) {
//          const copyVisited = new Set(visited);
//          const char = board[y][x - 1];
//          traverse(board, copyVisited.add(`${x - 1},${y}`), [x - 1, y], curStr + char);
//          count++;
//       }
//       if (!visited.has(`${x},${y - 1}`) && board[y - 1] !== undefined) {
//          const copyVisited = new Set(visited);
//          const char = board[y - 1][x];
//          traverse(board, copyVisited.add(`${x},${y - 1}`), [x, y - 1], curStr + char);
//          count++;
//       }
//       if (!visited.has(`${x + 1},${y}`) && board[y][x + 1] !== undefined) {
//          const copyVisited = new Set(visited);
//          const char = board[y][x + 1];
//          traverse(board, copyVisited.add(`${x + 1},${y}`), [x + 1, y], curStr + char);
//          count++;
//       }
//       if (!visited.has(`${x},${y + 1}`) && board[y + 1] !== undefined) {
//          const copyVisited = new Set(visited);
//          const char = board[y + 1][x];
//          traverse(board, copyVisited.add(`${x},${y + 1}`), [x, y + 1], curStr + char);
//          count++;
//       }

//       // if no cells are traversable
//       if (count === 0) {
//          // console.log('word', curStr);
//          return;
//       }

//    }


//    // let trie = {};


//    for (let y = 0; y < board.length; y++) {
//       for (let x = 0; x < board[y].length; x++) {
//          const char = board[y][x];
//          // let triePointer = trie;
//          // if (! (char in triePointer) ) {
//          //    triePointer[char] = {};
//          // }
//          // triePointer = triePointer[char];
//          // traverse(board, (new Set()).add(`${x},${y}`), [x,y], char, triePointer );
//          traverse(board, (new Set()).add(`${x},${y}`), [x, y], char);
//       }
//    }

//    // for (let i = 0; i < words.length; i++) {
//    //    const word = words[i];
//    //    let pointer = trie;
//    //    let found = true;
//    //    for (let y = 0; y < word.length; y++) {
//    //       const char = word[y];
//    //       // console.log('char', char);
//    //       // console.log('pointer', pointer);
//    //       if ( !(char in pointer) ) { found = false; break };
//    //       pointer = pointer[char];
//    //    }
//    //    if (found) {
//    //       result.push(word);
//    //    }
//    // }

//    // ========================================

//    // let zed = 0;

//    // function deleteUnmatch(wordsToMatch, char) {
//    //    for (const word in wordsToMatch) {
//    //       const i = ++wordsToMatch[word];
//    //       // console.log('deleteUnmatch', 'word', word, 'i', i, 'char', char);
//    //       // delete unmatch the current traverse char with word's current char from wordsToMatch
//    //       if (word[i] !== char) {
//    //          // console.log('DELETE WORD', word, word[i], char);
//    //          delete wordsToMatch[word];
//    //       }
//    //    }
//    //    return wordsToMatch;
//    // }

//    // function assignPossibleWords(wordsToMatch, char) {
//    //    if (wordsMapFirstChar[char] !== undefined && Object.keys(wordsMapFirstChar[char]).length > 0) {
//    //       for (let word in wordsMapFirstChar[char]) {
//    //          if (wordsToMatch[word] === undefined) {
//    //             wordsToMatch = { ...wordsToMatch, [word]: 0 };
//    //          }
//    //       }
//    //    }
//    //    return wordsToMatch;
//    // }

//    // function traverse(board, visited, cur, wordsToMatch) {
//    //    // if (zed >= 100) return;
//    //    // zed++;
//    //    const x = cur[0]; // current x
//    //    const y = cur[1]; // current y
//    //    let count = 0; // traverse count;

//    //    for (const word in wordsToMatch) {
//    //       const i = wordsToMatch[word];
//    //       // console.log('match only word', word, 'i', i);
//    //       // if a word already match all char
//    //       if (i + 1 === word.length) {
//    //          if (result[word] === undefined) {
//    //             result[word] = true;
//    //          }
//    //          // console.log('detected word', word);
//    //          delete wordsMapFirstChar[word[0]][word];
//    //          delete wordsToMatch[word];
//    //          continue;
//    //       };
//    //    }

//    //    // all words found
//    //    if (Object.keys(result).length >= words.length) {
//    //       // console.log('UDAH ANJING');
//    //       return;
//    //    }

//    //    if (Object.keys(wordsToMatch).length === 0) return;


//    //    // console.log('wordsToMatch', wordsToMatch);

//    //    if (!visited.has(`${x - 1},${y}`) && board[y][x - 1] !== undefined) {
//    //       const copyVisited = new Set(visited);
//    //       const char = board[y][x - 1];
//    //       const newWordsToMatch = assignPossibleWords( deleteUnmatch(Object.assign({},wordsToMatch), char), char);
//    //       traverse(board, copyVisited.add(`${x - 1},${y}`), [x - 1, y], newWordsToMatch);
//    //       count++;
//    //    }
//    //    if (!visited.has(`${x},${y - 1}`) && board[y - 1] !== undefined) {
//    //       const copyVisited = new Set(visited);
//    //       const char = board[y - 1][x];
//    //       const newWordsToMatch = assignPossibleWords( deleteUnmatch(Object.assign({},wordsToMatch), char), char);
//    //       traverse(board, copyVisited.add(`${x},${y - 1}`), [x, y - 1], newWordsToMatch);
//    //       count++;
//    //    }
//    //    if (!visited.has(`${x + 1},${y}`) && board[y][x + 1] !== undefined) {
//    //       const copyVisited = new Set(visited);
//    //       const char = board[y][x + 1];
//    //       const newWordsToMatch = assignPossibleWords( deleteUnmatch(Object.assign({},wordsToMatch), char), char);
//    //       traverse(board, copyVisited.add(`${x + 1},${y}`), [x + 1, y], newWordsToMatch);
//    //       count++;
//    //    }
//    //    if (!visited.has(`${x},${y + 1}`) && board[y + 1] !== undefined) {
//    //       const copyVisited = new Set(visited);
//    //       const char = board[y + 1][x];
//    //       const newWordsToMatch = assignPossibleWords( deleteUnmatch(Object.assign({},wordsToMatch), char), char);
//    //       traverse(board, copyVisited.add(`${x},${y + 1}`), [x, y + 1], newWordsToMatch);
//    //       count++;
//    //    }

//    //    // if no cells are traversable
//    //    if (count === 0) {
//    //       // console.log('word', curStr);
//    //       return;
//    //    }

//    // }

//    // // search word 
//    // let result = {};
//    // let wordsMapFirstChar = {};
//    // let wordsMapIndex = {};
//    // for (let i = 0; i < words.length; i++) {
//    //    const word = words[i];
//    //    wordsMapFirstChar[word[0]] = wordsMapFirstChar[word[0]] ? { ...wordsMapFirstChar[word[0]], [word]: 0 } : { [word]: 0 };
//    //    wordsMapIndex[word] = i;
//    // }

//    // // console.log('wordsMapFirstChar', wordsMapFirstChar);

//    // for (let y = 0; y < board.length; y++) {
//    //    for (let x = 0; x < board[y].length; x++) {
//    //       const char = board[y][x];
//    //       // console.log('first char', char);
//    //       // let triePointer = trie;
//    //       if (!(char in wordsMapFirstChar)) {
//    //          continue;
//    //       }

//    //       traverse(board, (new Set()).add(`${x},${y}`), [x, y], Object.assign(wordsMapFirstChar[char]));
//    //    }
//    // }

//    // return Object.keys(result);
// }


