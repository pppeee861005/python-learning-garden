# 驗證程式結果
import subprocess
import sys

# 執行主程式並捕獲輸出
try:
    result = subprocess.run([sys.executable, 'homework3_final.py'], 
                          capture_output=True, text=True, cwd='.')
    print("程式執行結果：")
    print(result.stdout)
    if result.stderr:
        print("錯誤訊息：")
        print(result.stderr)
except Exception as e:
    print(f"執行錯誤：{e}")

# 手動驗證
print("\n=== 手動驗證 ===")
with open('word_count.txt', 'r') as f:
    content = f.read()
    lines = content.split('\n')
    
print(f"檔案內容：")
for i, line in enumerate(lines):
    print(f"第{i+1}行：'{line}'")

non_empty_lines = [line for line in lines if line.strip()]
print(f"\n非空行數：{len(non_empty_lines)}")

total_words = sum(len(line.split()) for line in lines)
print(f"總字數：{total_words}")

punctuation = ".,!?;:\"'()[]{}/-"
char_count = sum(1 for line in lines for char in line if char != ' ' and char not in punctuation)
print(f"字元數（不含標點符號）：{char_count}")
