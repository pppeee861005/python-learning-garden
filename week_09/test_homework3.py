# 測試版本 - 作業三：文字檔解析

# 使用指定的兩行敘述讀取檔案
infile = open('word_count.txt')      # 開啟檔案
lines = infile.read().split("\n")    # 讀取檔案，依不同行切割為串列
infile.close()

# 初始化計數器
line_count = 0
word_count = 0
char_count = 0

# 定義標點符號
punctuation = ".,!?;:\"'()[]{}/-"

# 處理每一行
for line in lines:
    if line.strip():  # 非空行
        line_count += 1
    
    words = line.split()
    word_count += len(words)
    
    for char in line:
        if char != ' ' and char not in punctuation:
            char_count += 1

# 輸出結果
result = f"檔案中共有 {line_count} 行，{word_count} 個字，{char_count} 個字元(不含標點符號)"
print(result)

# 將結果寫入檔案以便查看
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(result)
    f.write('\n\n詳細資訊：\n')
    f.write(f'讀取到的行：{lines}\n')
    for i, line in enumerate(lines, 1):
        if line.strip():
            f.write(f'第{i}行："{line}" - 單字數：{len(line.split())}\n')
