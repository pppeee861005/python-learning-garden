# 作業三：文字檔解析
# 仿照 UNIX 中 wc 公用程式解析文字檔

# === 路徑說明 ===
# 1. 絕對路徑：完整的檔案位置，從根目錄開始
#    例如：'D:/遊樂場/code_homework/week_09/word_count.txt'
# 2. 相對路徑：相對於目前程式執行位置的路徑
#    例如：'word_count.txt' (同目錄下的檔案)
#    例如：'../word_count.txt' (上一層目錄的檔案)

# 使用指定的兩行敘述讀取檔案
# 這裡使用相對路徑 'word_count.txt'，表示檔案在同一個目錄下
infile = open('word_count.txt')      # 開啟檔案 (相對路徑)
lines = infile.read().split("\n")    # 讀取檔案，依不同行切割為串列
                                     # 即串列元素依序是檔案內每一行

# 關閉檔案（良好的程式習慣）
infile.close()

# 初始化計數器
line_count = 0      # 行數計數器
word_count = 0      # 字數計數器
char_count = 0      # 字元計數器（不含標點符號）

# 定義標點符號（用來排除計算）
punctuation = ".,!?;:\"'()[]{}/-"

# 逐行處理文字
for line in lines:
    # 如果這一行不是空行，就計算為一行
    if line.strip():  # strip() 移除前後空白，如果移除後還有內容就不是空行
        line_count += 1
    
    # 將這一行分割成單字來計算字數
    words = line.split()  # split() 會依空白分割字串成單字列表
    word_count += len(words)  # 加上這一行的單字數量
    
    # 計算字元數（不含標點符號）
    for char in line:
        # 如果字元不是空白且不是標點符號，就計算
        if char != ' ' and char not in punctuation:
            char_count += 1

# 輸出結果（按照作業要求的格式）
print(f"檔案中共有 {line_count} 行，{word_count} 個字，{char_count} 個字元(不含標點符號)")

# === 路徑使用說明 ===
print("\n=== 路徑說明 ===")
print("本程式使用相對路徑：'word_count.txt'")
print("這表示檔案必須與程式在同一個目錄下")
print("適合上傳到 Google Classroom，因為兩個檔案會在同一個資料夾中")
