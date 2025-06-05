
total_characters = sum(len(line) for line in poem_lines)

這行程式碼用來計算詩歌所有行的總字數。sum(len(line) for line in poem_lines) 是一個「生成式」（generator expression），會對    poem_lines 這個串列中的每一行    line，先用    len(line) 計算該行的字元數，然後用    sum() 把所有行的字數加總起來，結果存到    total_characters 變數。這種寫法簡潔又直觀，常用於統計多行文字的總長度。

count = cambridge_poem.count(search_word)
這行程式碼用來計算某個單字或子字串在整首詩（   cambridge_poem）中出現的次數。   cambridge_poem.count(search_word) 會回傳    search_word 在    cambridge_poem 這個字串裡出現的總次數，並把結果存到變數    count。這種寫法常用於文字分析、關鍵字統計或搜尋功能，可以快速得知某個詞在文本中出現了幾次。

.count 是 Python 字串（str）和串列（list）物件的方法，用來計算某個子字串或元素在原始資料中出現的次數。 例如： • 對字串："hello world".count("o") 會回傳 2，因為 "o" 出現了兩次。 • 對串列：[1, 2, 2, 3].count(2) 會回傳 2，因為 2 出現了兩次。  在你的程式中，cambridge_poem.count(search_word) 就是計算 search_word 這個字串在 cambridge_poem 這首詩中出現了幾次。

這個程式會先把整首詩用    split('\n') 切成一段一段（每一行），主要有以下幾個原因： 1.  方便逐行顯示
　切成    poem_lines 之後，可以用 for 迴圈把每一行分別印出來，讓輸出格式更清楚、易讀。  2.  方便統計行數與每行字數
　這樣可以直接用    len(poem_lines) 得到行數，也能用    sum(len(line) for line in poem_lines) 計算每行字數的總和。  3.  方便搜尋時標示出現在哪一行
　在搜尋功能中，程式可以判斷搜尋字串出現在第幾行，並把該行內容印出來，讓使用者更容易找到關鍵字的位置。   總結：
雖然直接用整首詩的字串也能做總字數或關鍵字統計，但切成一段一段（每一行）可以讓程式更靈活，方便做進階的顯示、分析和互動功能。

enumerate
是 Python 的內建函式，用來在 for 迴圈中同時取得元素的索引（編號）和值。當你用 for i, value in enumerate(序列): 這種寫法時，i 會自動從 0 開始編號，value 則是序列中的每個元素。這樣可以讓你在遍歷資料時，不需要自己額外設計計數器，就能同時取得索引和內容。   enumerate 也可以指定起始編號，例如    enumerate(序列, 1) 會讓索引從 1 開始。這個函式常用於需要同時處理元素和其位置的情境，讓程式碼更簡潔易讀。


任務要求：
1.顯示整首詩
2.將詩拆成一段一段
3.計算：1.行數2.字數|
4.搜尋字串：1.計算出現次數2.出現在哪一行
5.程式結束
6.美觀

技術架構：
1.將整首詩放在 cambridge_poem變數中
2.用.split('\n')將整首詩切開 放在 poem_lines變數中
3.在for循環中，用enumerate(poem_lines, 1)：取得序號及值
for i, line in enumerate(poem_lines, 1):
    print(f"第{i}行 : {line}")
4.用以展示以下效果：    
第1行：輕輕的我走了，正如我輕輕的來；我輕輕的招手，作別西天的雲彩。

5.用len來計算行數
6.用len來計算字數。計算每行中的字數，再用sum來加總字數

7.用while True:來反復得到user的搜尋字串：處理3種狀況
a：如果quit就break
b:空白就反復要求user輸入
c:找到字串，計算次數
用.count
count = cambridge_poem.count(search_word)

7.額外功能：
顯示出現在哪些行
用enumerate(poem_lines, 1):

for i, line in enumerate(poem_lines, 1):
            if search_word in line:
                print(f"   第{i}行:{line}")


8.
1.如果有就計算次數
2.沒有的話顯示沒有
9.顯示結尾

'\n' 是 Python 字串中的換行字元，代表「newline」或「line break」。當你在字串中插入 '\n'，輸出時就會從這個位置開始換到下一行。這個字元常用於格式化輸出、多行文字、或將資料分行顯示。例如：print("Hello\nWorld") 會印出：


poem_lines = cambridge_poem.split('\n')  和    poem_lines = cambridge_poem.split() 的差異在於分割依據不同： •    split('\n') 是依照換行符號（每一行的結尾）來切割，得到的是「每一行」為一個元素的串列。這樣    poem_lines 會是一個「每行一元素」的清單，適合逐行處理詩歌。  •    split()（沒有參數）則是依照所有空白字元（包括空格、Tab、換行等）來切割，得到的是「每一個詞」為一個元素的串列。這樣    poem_lines 其實會變成「所有詞語」的清單，而不是每一行。

舉例說明： 假設詩歌內容如下：                        •  用    split('\n') 結果是：                        （每一行一個元素）  •  用    split() 結果是：                        （這裡因為每行沒有空格，效果看起來一樣，但如果有空格或多行，會把所有詞語拆成一個個元素）   總結： •    split('\n')：分割成「每一行」。 •    split()：分割成「每一個詞」（遇到任何空白就切開）。  在詩歌逐行顯示、逐行搜尋時，應該用    split('\n')。如果你想要統計所有詞語或做詞語分析，可以用    split()。

.strip 是 Python 字串（str）物件的方法，用來去除字串開頭和結尾的空白字元，包括空格、換行（\n）、製表符（\t）等。通常會寫成 .strip()，例如：s.strip()。這個方法不會改變原本的字串，而是回傳一個去除前後空白的新字串。常用於處理使用者輸入、檔案讀取或資料清理時，確保資料前後沒有多餘的空白。