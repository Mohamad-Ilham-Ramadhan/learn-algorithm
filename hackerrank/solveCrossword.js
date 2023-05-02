// crossword puzzle using recursion technique

const crossword = [
   '+-++++++++',
   '+-++++++++',
   '+-++++++++',
   '+-----++++',
   '+-+++-++++',
   '+-+++-++++',
   '+++++-++++',
   '++------++',
   '+++++-++++',
   '+++++-++++',
];
const words = 'LONDON;DELHI;ICELAND;ANKARA';


// solveCrossword(crossword, words);

function sc(crossword, words) {
   // loop secara horizontal jika tidak ada huruf sama sekali berati first recursive maka insert kata yang unik (1)
   // recursive lagi 
   // loop secara horizontal hingga ketemu huruf lalu check atas bawah apakah '-' (2)
   // [yes] berarti ada (crossline vertical) maka simpen indexColumnnya 
   // cari dan simpan length crossline tersebut dan index keberapa huruf itu pada crossline 
   // cocokan length dan huruf pada index itu dengan salah satu word yang ada di words.
   // [yes] jika sudah ketemu maka insert
   // hapus inserted word dar words
   // [no] (mungkin dicabut inserted word ganti dengan word yang sama lengthnya)
   // recursive lagi (2)

   // loop secara horizontal hingga ketemu huruf lalu check atas bawah apakah huruf jika [yes] maka check cell kanan kiri jika ada '-' (2)
   // [yes] ada (crossline horizontal) maka simpen indexRownya 
   // cari dan simpan length crossline tersebut dan index keberapa huruf itu pada crossline 
   // cocokan length dan huruf pada index itu dengan salah satu word yang ada di words.
   // jika sudah ketemu maka insert
   // hapus inserted word dar words
   // recursive lagi (2) 
   console.log("================================");
   console.log('WORDS', words);
   let wordsArr = words.split(';');
   console.log('wordsArr', wordsArr);
   console.log('crossword', JSON.stringify(crossword, null, 2));
   const wordsLength = wordsArr.map(word => word.length);
   // let insertedWords = [];
   // CROSSWORD LINE (available line) MAPING ==== [start section] === 
   let availableLines = []; // { startRow, endRow, startColumn, endColumn, length, type} => available line yang bisa cocok dengan available words berdasarkan length nya


   // (CONDITION) Base condition 
   if (!crossword.find(row => row.includes('-'))) {
      console.log('BASE CONDITION: ALL LINE HAS BEEN INSERTED');
      return crossword;
   }



   // collect horizontal lines [start]
   for (let i = 0; i < 10; i++) {
      let length = 0;
      let startColumn = 0;
      let crossed = [];
      let wordCount = 0; // untuk cek apakah line itu udah di isi word
      let word = '';
      for (let j = 0; j < 10; j++) {

         const currentCell = crossword[i][j];
         const isTheDashEnd = (currentCell === '+' && length > 0);
         const isTheLineEnd = ((currentCell === '-' || currentCell.match(/[A-Z]/g)) && j === 9);

         // === DEBUG ===
         // if (i === 6) {
         //    console.log('COLLECT ROW: ' + i, j, 'currentCell', currentCell, 'word', word);
         // }
         // === DEBUG ===

         if (isTheDashEnd || isTheLineEnd) {
            const endColumn = isTheDashEnd ? j - 1 : j;
            length = isTheLineEnd ? length + 1 : length;
            if (currentCell.match(/[A-Z]/g) || currentCell === '-') {
               word += currentCell;
               if (currentCell.match(/[A-Z]/g)) {
                  wordCount++;
                  crossed.push({ letter: currentCell, indexInWord: j - startColumn, row: i, column: j });
               }
            }
            // cari length dengan length dari words jika ada maka taruh di availableLines
            if (wordsLength.find(l => l === length)) { // word.length harus sama dengan line.length cocok untuk swapable line, karena jika ada word dengan length padahal line itu udah diisi maka line itu masih bisa di swap dengan word lain
               availableLines.push({
                  type: 'horizontal',
                  startRow: i,
                  endRow: i,
                  startColumn,
                  endColumn,
                  length,
                  wordCount,
                  isFilled: wordCount === length ? true : false,
                  crossed,
                  word,
               });
            }
            length = 0;
            startColumn = 0;
            crossed = [];
            wordCount = 0;
            word = '';
            continue;
         }
         if ((currentCell === '-' || currentCell.match(/[A-Z]/g)) && length === 0) {
            startColumn = j;
            length++;
            word += currentCell;
            if (currentCell.match(/[A-Z]/g)) {
               wordCount++;
               crossed.push({ letter: currentCell, indexInWord: j - startColumn, row: i, column: j });
            }
            continue;
         }
         if (currentCell === '-' || currentCell.match(/[A-Z]/g)) {
            length++;
            word += currentCell;
            if (currentCell.match(/[A-Z]/g)) {
               wordCount++;
               crossed.push({ letter: currentCell, indexInWord: j - startColumn, row: i, column: j });
            }
            continue;
         }

         // if '-' the last in the row, so next loop is new row
      }
   }
   // collect horizontal lines [end]

   // collect vertical lines [start]
   for (let i = 0; i < 10; i++) {
      // (BELUM ANTISIPASI FULL VERTICAL LINE)
      let length = 0;
      let startRow = 0;
      let crossed = [];
      let wordCount = 0; // untuk cek apakah line itu udah di isi word
      let word = '';
      for (let j = 0; j < 10; j++) {
         const currentCell = crossword[j][i];
         const isTheDashEnd = (currentCell === '+' && length > 0);
         const isTheLineEnd = ((currentCell === '-' || currentCell.match(/[A-Z]/g)) && j === 9);

         if (isTheDashEnd || isTheLineEnd) {
            const endRow = isTheDashEnd ? j - 1 : j;
            length = isTheLineEnd ? length + 1 : length;

            if (currentCell.match(/[A-Z]/g) || currentCell === '-') {
               word += currentCell;
               if (currentCell.match(/[A-Z]/g)) {
                  wordCount++;
                  crossed.push({ letter: currentCell, indexInWord: j - startRow, row: j, column: i });
               }
            }

            // cari length dengan length dari words jika ada maka taruh di availableLines (horizontal gak butuh ini)
            if (wordsLength.find(l => l === length)) { // word.length harus sama dengan line.length cocok untuk swapable line, karena jika ada word dengan length padahal line itu udah diisi maka line itu masih bisa di swap dengan word lain
               availableLines.push({
                  type: 'vertical',
                  startRow,
                  endRow,
                  startColumn: i,
                  endColumn: i,
                  length,
                  isFilled: wordCount === length ? true : false,
                  crossed,
                  word,
               });
            }
            length = 0;
            startRow = 0;
            crossed = [];
            wordCount = 0;
            word = '';
            continue;
         }

         if ((currentCell === '-' || currentCell.match(/[A-Z]/g)) && length === 0) {
            // console.log('FIRST LINE Found', 'row', j, 'length', length, 'column', i);
            startRow = j;
            length++;
            word += currentCell;
            if (currentCell.match(/[A-Z]/g)) {
               wordCount++;
               crossed.push({ letter: currentCell, indexInWord: j - startRow, row: j, column: i });
            }
            continue;
         }
         if ((currentCell === '-' || currentCell.match(/[A-Z]/g))) {
            // console.log('COUNTINUE THE LINE', startRow, j);
            length++;
            word += currentCell;
            if (currentCell.match(/[A-Z]/g)) {
               wordCount++;
               crossed.push({ letter: currentCell, indexInWord: j - startRow, row: j, column: i });
            }
            continue;
         }
      }
   }
   // collect vertical lines [end]


   let wordsDetail = wordsArr.map(word => ({
      word,
      length: word.length,
      lengthOccurence: wordsLength.reduce((acc, cl) => {
         return cl === word.length ? acc + 1 : acc;
      }, 0),
      isInserted: false,
   }));

   function insertUniqueLengthWord() {
      console.log('THE FIRST TIME');
      console.log('availableLines', availableLines);


      // sort wordsDetail by lengthOccurence ascending
      wordsDetail = wordsDetail.sort((a, b) => a.lengthOccurence - b.lengthOccurence);

      // insert kata yang paling unik (1)
      // cari garis2 yang bersilangan dengan inserted garis 
      // caranya bisa dengan start/end index
      // insert semua garis bersilangan itu dengan kata yang benar (2)
      // cari garis2 yang bersilangan dengan inserted garis (2)
      // insert semua garis bersilangan itu dengan kata yang benar (3)

      // and so on

      const insertedWord = wordsDetail[0];
      const firstUniqueLine = availableLines.find(line => line.length === insertedWord.length);
      console.log('firstUniqueLine', firstUniqueLine);
      // cari garis2 yang bersilangan dengan firstUniqueLine 
      if (firstUniqueLine.type === 'horizontal') {
         // const crossedLines = availableLines.filter(line => line.type === 'vertical' && line.startColumn >= firstUniqueLine.startColumn && line.endColumn <= firstUniqueLine.endColumn);

         // insert first unique line 
         crossword[firstUniqueLine.startRow] = crossword[firstUniqueLine.startRow].slice(0, firstUniqueLine.startColumn) + insertedWord.word + crossword[firstUniqueLine.startRow].slice(firstUniqueLine.endColumn + 1);

         console.log('insertedWord.word', insertedWord.word, 'firstUniqueLine.endColumn + 1', firstUniqueLine.endColumn + 1);
         // insertedWords.push(wordsDetail.shift());
      } // <====   if (firstUniqueLine.type === 'horizontal')

      if (firstUniqueLine.type === 'vertical') {
         // console.log('FISRT UNIQUE LINE IS VERTICAL');
         let letterIndex = 0;
         for (let i = firstUniqueLine.startRow; i <= firstUniqueLine.endRow; i++) {
            // console.log('FISRT UNIQUE LINE IS VERTICAL row: ' + i);
            const row = crossword[i];
            crossword[i] = row.slice(0, firstUniqueLine.startColumn) + insertedWord.word[letterIndex] + row.slice(firstUniqueLine.startColumn + 1);
            letterIndex++;
         }
      }

      words = words.replace(`${insertedWord.word};`, '');

      console.log('NEXT WORDS', words);
      // return sc(crossword, words);
      return crossword;
   } // <=== function insertUniqueLengthWord

   // (CONDITION) First recursive condition or zero inserted word in the crossword
   if (!crossword.find(row => row.match(/[A-Z]/g))) {
      return insertUniqueLengthWord();
   }

   // Already inserted words in the crossword 
   if (crossword.find(row => row.match(/[A-Z]/g))) {
      console.log('THERE IS INSERTED WORDS BUT NOT FINISHED');


      const crossedLines = availableLines.filter(line => !line.isFilled && line.crossed.length !== 0);
      console.log('availableLines', availableLines);
      console.log('crossed lines:', crossedLines);

      if (crossedLines.length === 0) {
         console.log('THERE IS NO CROSSED LINE', 'wordsLength', wordsLength);
         return insertUniqueLengthWord();
      }

      const oldWords = words;

      // isi crossedLines (to insert lines) (1)
      for (let i = 0; i < crossedLines.length; i++) {
         const line = crossedLines[i];

         // const matchedWord = wordsDetail.find(wd => wd.length === line.length && (wd.word[line.crossed.indexInWord] === line.crossed.letter)); // yang length-nya sama dan salah satu hurufnya sama berdasarkan index (HARUS EDIT SUPPORT MULTI CROSSED INDEX KARENA TAKUT ADA YANG KEBETULAN SAMA DI INDEX TERSEBUT)

         // const matchedWords = wordsDetail.filter(w => w.word.length === line.length && (w.word[line.crossed.indexInWord] === line.crossed.letter));

         const matchedWords = wordsDetail.filter( w => {
            if (w.word.length !== line.length) return false;
            return line.crossed.every( l => { 
               console.log(w.word, w.word);
               return w.word[l.indexInWord] === l.letter
            });
         });
         

         console.log('matchedWords', matchedWords);
         for (let i = 0; i < matchedWords.length; i++) {
            // jika ada crossed (2) yang ga cocok dengan matchedWord maka tuker dengan word yang sama lengthnya di words
            const matchedWord = matchedWords[i];
            console.log('MATCHED WORD', matchedWord);
            if (line.type === 'horizontal') {
               // cuma crossed (2) yang ada di availableLines aja yang harus dituker karena kalo yang gak ada berarti dia (2) unik word.length nya alias dia udah bener disitu.
               const swapableLine = availableLines.find(al => {
                  if (al.type === 'horizontal' || al.isFilled !== true) return false;
                  const index = al.startColumn - line.startColumn; // index of crossed letter in matchedWord
                  const matchedWordCrossedLetter = matchedWord.word[index];
                  const alCrossedMatchedLetter = crossword[line.startRow][al.startColumn];
                  const isBothLineCrossed = al.startColumn >= line.startColumn && al.endColumn <= line.endColumn;
                  const isCrossedCellDifferentLetter = matchedWordCrossedLetter !== alCrossedMatchedLetter;

                  return isBothLineCrossed && isCrossedCellDifferentLetter;
               });
               // swap swapable line dengan word length yang sama di words
               if (swapableLine !== undefined) {
                  console.log('SWAP VERTICAL LINE', swapableLine);
                  const alternateWord = wordsDetail.find(wd => wd.length === swapableLine.word.length);
                  // (insert vertical) alternate word
                  let letterIndex = 0;
                  for (let x = swapableLine.startRow; x <= swapableLine.endRow; x++) {
                     const row = crossword[x];
                     crossword[x] = row.slice(0, swapableLine.startColumn) + alternateWord.word[letterIndex] + row.slice(swapableLine.endColumn + 1);
                     letterIndex++;
                  }

                  let ws = words.split(';').filter(w => w !== alternateWord.word); ws.push(swapableLine.word); ws = ws.join(';');
                  console.log('WS', ws, 'WORDS', words);
                  words = ws;

                  // return sc(crossword, words);
                  return crossword;

               } else {
                  console.log('GAK ADA YANG PERLU DI SWAP, INSERT AJA');
                  // (horizontal insertion) matchedWord 
                  const row = crossword[line.startRow];
                  crossword[line.startRow] = row.slice(0, line.startColumn) + matchedWord.word + row.slice(line.endColumn + 1);
                  // delete inserted word from words 
                  let ws = words.split(';').filter(w => w !== matchedWord.word); ws = ws.join(';');
                  words = ws;
                  // return sc(crossword, words);
                  return crossword;
               }
            }

            if (line.type === 'vertical') {
               console.log('MATCHED WORD', matchedWord);
               // cuma crossed (2) yang ada di availableLines aja yang harus dituker karena kalo yang gak ada berarti dia (2) unik word.length nya alias dia udah bener disitu.
               const swapableLine = availableLines.find(al => {
                  if (al.type === 'vertical' || al.isFilled !== true) return false;
                  const index = al.startRow - line.startRow; // index of crossed letter in matchedWord
                  const matchedWordCrossedLetter = matchedWord.word[index];
                  const alCrossedMatchedLetter = crossword[al.startRow][line.startColumn];

                  const isBothLineCrossed = line.startColumn >= al.startColumn && line.endColumn <= al.endColumn;
                  const isCrossedCellDifferentLetter = matchedWordCrossedLetter !== alCrossedMatchedLetter;

                  return isBothLineCrossed && isCrossedCellDifferentLetter;
               }); // <== [BELUM DI TEST] ketika ada swapableLine

               // swap swapable line dengan word length yang sama di words
               if (swapableLine !== undefined) {
                  console.log('SWAP HORIZONTAL LINE [NOT TESTED]', swapableLine);
                  // if block ini [BELUM DI TEST] ketika ada swapableLine

                  const alternateWord = wordsDetail.find(wd => wd.length === swapableLine.word.length);
                  // (horizontal insertion) alternate word
                  const row = crossword[swapableLine.startRow];
                  crossword[swapableLine.startRow] = row.slice(0, swapableLine.startColumn) + alternateWord.word + row.slice(swapableLine.endColumn + 1);
                  let ws = words.split(';').filter(w => w !== alternateWord.word); ws.push(swapableLine.word); ws = ws.join(';');
                  words = ws;
                  // return sc(crossword, words);
                  return crossword;
               } else {
                  console.log('===== DISINI NIH =====');
                  // (vertical insertion) matchedWord 
                  let letterIndex = 0;
                  for (let x = line.startRow; x <= line.endRow; x++) {
                     const row = crossword[x];
                     crossword[x] = row.slice(0, line.startColumn) + matchedWord.word[letterIndex] + row.slice(line.endColumn + 1);
                     letterIndex++;
                  }
                  // delete inserted word from words 
                  console.log('MATCHED WORD', matchedWord.word);

                  let ws = words.split(';').filter(w => w !== matchedWord.word); ws = ws.join(';');
                  words = ws;

                  // return sc(crossword, words);
                  return crossword;
               }  
            }
         }
      }

      // (SEDANG IMPLEMENT ROLLBACK) jika gak ada word yang match dengan crossed line berarti inserted wordnya salah taruh berarti ada line lain yang match lengthnya, cabut inserted word lalu taruh di akhir word biar word yang lengthnya sama masuk ke line itu 
      if (oldWords === words) {
         console.log('GAK ADA YANG MATCH (ROLLBACK NEEDED)', 'oldWords', oldWords, 'words', words);
         const insertedLine = availableLines.filter(line => line.isFilled);
         // ketika partiallyFilled crossedLine(1) gak ada yang match berarti sebelumnya ada word yang salah nempatin (kebetulan length dan inserted letter index nya sama) maka cabut crossedLines(2) dari crossedLine(1) itu tapi jangan cabut letter dari crossedlines(3) crossedlines(2) itu dan ganti word yang lain dari masing2 crossedLines(2) itu


         console.log('inserted line', insertedLine);
         insertedLine.forEach(line => {
            if (line.type === 'horizontal') {
               const row = crossword[line.startRow];
               const word = row.slice(line.startColumn, line.endColumn + 1);
               crossword[line.startRow] = row.slice(0, line.startColumn) + '-'.repeat(line.endColumn - line.startColumn + 1) + row.slice(line.endColumn + 1);
               words += `;${word}`;
            }
            if (line.type === 'vertical') {
               for (var i = line.startRow; i <= line.endRow; i++) {
                  const cell = crossword[i][line.startColumn];
                  if ((cell === line.crossed.letter) && i === line.crossed.row) {
                     console.log('TIDAK HAPUS CROSSED LETTER', cell);
                     continue;
                  }
                  crossword[i] = crossword[i].replace(cell, '-');
               }
            }
         });
         console.log('words: ', words, 'oldWords: ', oldWords);
      };


      console.log('NEXT WORDS', words);
      // return sc(crossword, words);
      return crossword;
   }




   // console.log('availableLines', availableLines);
   // console.log('insertedWords', insertedWords);
}


const crossword2 = [
   '++++++++++',
   '+------+++',
   '+++-++++++',
   '+++-++++++',
   '+++-----++',
   '+++-++-+++',
   '++++++-+++',
   '++++++-+++',
   '++++++-+++',
   '++++++++++',
];
const words2 = 'POLAND;LHASA;SPAIN;INDIA';

const crossword2Debug = [
   "++++++++++",
   "+POLAND+++",
   "+++H++++++",
   "+++A++++++",
   "+++SPAIN++",
   "+++A++-+++",
   "++++++-+++",
   "++++++-+++",
   "++++++-+++",
   "++++++++++",
];
const words2Debug = 'INDIA';

const crossword3 = [
   '+-++++++++',
   '+-++++++++',
   '+-------++',
   '+-++++++++',
   '+-++++++++',
   '+------+++',
   '+-+++-++++',
   '+++++-++++',
   '+++++-++++',
   '++++++++++',
];
const words3 = 'AGRA;NORWAY;ENGLAND;GWALIOR';

const crossword4 = [
   '++++++-+++',
   '++------++',
   '++++++-+++',
   '++++++-+++',
   '+++------+',
   '++++++-+-+',
   '++++++-+-+',
   '++++++++-+',
   '++++++++-+',
   '++++++++-+',
];
const words4 = 'ICELAND;MEXICO;PANAMA;ALMATY';

const crossword5 = [
   '++++++++++',
   '----++++++',
   '+++-++++++',
   '+++-++++++',
   '+++----+++',
   '++++++-+++',
   '++++++-+++',
   '+++----+++',
   '++++++++++',
   '++++++++++',
];
const words5 = 'DAMN;ABRA;ANDI;INDE;EDAN';

const crossword6 = [
   '+-++++++++',
   '+-++-+++++',
   '+-------++',
   '+-++-+++++',
   '+-++-+++++',
   '+-++-+++++',
   '++++-+++++',
   '++++-+++++',
   '++++++++++',
   '----------',
]; // fail hidden test case
const words6 = 'CALIFORNIA;NIGERIA;CANADA;TELAVIV';

const crossword7 = [
   '+-+++++++-',
   '+-++-++++-',
   '+-------+-',
   '+-++-++++-',
   '+-++-++++-',
   '+-++-++++-',
   '++++-++++-',
   '++++-++++-',
   '+++++++++-',
   '+++++++++-',
]; // edge case for full vertical line
const words7 = 'CALIFORNIA;NIGERIA;CANADA;TELAVIV';

const crossword8 = [
   '+-++++++++',
   '+-++-+++++',
   '+-------++',
   '+-++-++-++',
   '+-++-++-++',
   '+-++-++-++',
   '++++-++-++',
   '+--------+',
   '++++++++++',
   '----------',
]; // fail hidden test case 
const words8 = 'CALIFORNIA;LASVEGAS;NIGERIA;CANADA;TELAVIV;ALASKA';
const crossword8Debug = [
   '+-++++++++',
   '+-++T+++++',
   '+---E--C++',
   '+-++L++A++',
   '+-++A++N++',
   '+-++V++A++',
   '++++I++D++',
   '+LASVEGAS+',
   '++++++++++',
   'CALIFORNIA',
]; // fail hidden test case (STUCK THIS AFTER 3 RECURS)
const words8Debug = 'NIGERIA;ALASKA';

const crossword9 = [
   '+-++++++++',
   '+-------++',
   '+-++-+++++',
   '+-------++',
   '+-++-++++-',
   '+-++-++++-',
   '+-++------',
   '+++++++++-',
   '++++++++++',
   '++++++++++',
];
const words9 = 'ANDAMAN;MANIPUR;ICELAND;ALLEPY;YANGON;PUNE';

const crossword9Debug = [
   '+-++++++++',
   '+-------++',
   '+-++-+++++',
   '+-------++',
   '+-++-++++P',
   '+-++-++++U',
   '+-++-----N',
   '+++++++++E',
   '++++++++++',
   '++++++++++',
];
const words9Debug = 'ANDAMAN;MANIPUR;ICELAND;ALLEPY;YANGON';

const crosswordDebug = [
   '+L++++++++',
   '+O++++++++',
   '+N++++++++',
   '+DELHI++++',
   '+O+++-++++',
   '+N+++-++++',
   '+++++-++++',
   '++------++',
   '+++++-++++',
   '+++++-++++',
];
const wordsDebug = 'ICELAND;ANKARA';


console.log('final result :', JSON.stringify(sc(crossword5, words5), null, 2));  // 5 (buatan gw) never end