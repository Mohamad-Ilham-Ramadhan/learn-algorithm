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

   Solution by NeetCode: 

   LeetCode submission:
      #1
         - Runtime:  5414 ms, beats 12.55%
         - Memory:  50.3 MB, beats 42.44%
      #2
         - Runtime: 5276 ms, beats 14.48%
         - Memory: 50.1 MB, beats 49.20%
      #3 (with my optimizations code)
         - Runtime: 4095 ms, beats 20.91%
         - Memory: 50.3 MB, beats 44.37%
      #4 (with my optimizations code)
         - Runtime: 4066 ms, beats 20.91%
         - Memory: 50.1 MB, beats 49.20%
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

class TrieNode {
   constructor() {
      this.children = {};
      this.isWord = false;           
   }

   addWord(word) {
      let cur = this;
      for (let c of word) {
         if (! (c in cur.children)) cur.children[c] = new TrieNode();
         cur = cur.children[c];
      }
      cur.isWord = true;
   }
}
function findWords(board, words) {

   // my optimizations #4 [start]
   let boardChars = new Set();
   let possibleWords = [];

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
         possibleWords.push(word)
      };
   }
   // my optimizations #4 [end]

   let root = new TrieNode();
   // for (let w of words) {
   //    root.addWord(w);
   // }

   // my optimizations #4 [start]
   for (let w of possibleWords) {
      root.addWord(w);
   }
   // my optimizations #4 [end]

   const ROWS = board.length;
   const COLS = board[0].length;
   let res = new Set();
   let visit = new Set();

   function dfs(r, c, node, word) {
      if (
         (r < 0 || c < 0) ||
         (r === ROWS || c === COLS) ||
         ( visit.has(`${r},${c}`)) ||
         (! (board[r][c] in node.children) ) || 
         (res.size === words.length) // <----- my optimizations (#3, #4)
      ) return;

      visit.add(`${r},${c}`);
      node = node.children[board[r][c]];
      word += board[r][c];

      if (node.isWord) res.add(word);

      dfs(r - 1, c, node, word);
      dfs(r + 1, c, node, word);
      dfs(r, c - 1, node, word);
      dfs(r, c + 1, node, word);

      visit.delete(`${r},${c}`);
   }

   for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
         // my optimizations #4 [start]
         if (res.size >= possibleWords.size) {
            return Array.from(res);
         }
         // my optimizations #4 [end]
         dfs(r, c, root, '');
      }
   }

   return Array.from(res);
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
console.log('RESULT: ', findWords(board1, words1));
console.log('runtime', Date.now() - start);
