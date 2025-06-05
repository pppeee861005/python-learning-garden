# [作業二] 文件加密 - 凱薩密碼
# 適合 Python 新手的詳細解答

def shift_char(char, shift_amount):
    """
    移動單個字母的函數
    
    參數:
        char: 要移動的字母 (a-z)
        shift_amount: 移動的位數 (正數往前移，負數往後移)
    
    回傳:
        移動後的字母
    """
    # 檢查是否為小寫英文字母
    if 'a' <= char <= 'z':
        # 將字母轉換為數字 (a=0, b=1, ..., z=25)
        char_num = ord(char) - ord('a')
        
        # 進行移動並處理循環 (用 % 26 確保結果在 0-25 範圍內)
        new_char_num = (char_num + shift_amount) % 26
        
        # 將數字轉回字母
        new_char = chr(new_char_num + ord('a'))
        
        return new_char
    else:
        # 如果不是小寫字母，直接回傳原字元
        return char

def encrypt_string(text, shift_amount):
    """
    加密整個字串的函數
    
    參數:
        text: 要加密的字串
        shift_amount: 移動的位數
    
    回傳:
        加密後的字串
    """
    encrypted = ""  # 用來存放加密結果的空字串
    
    # 逐一處理字串中的每個字元
    for char in text:
        encrypted_char = shift_char(char, shift_amount)
        encrypted += encrypted_char
    
    return encrypted

def print_result(original, shift, encrypted):
    """
    印出結果的函數，讓輸出格式統一
    """
    direction = "前移" if shift > 0 else "後移"
    print(f"輸入字串：{original} {direction} {abs(shift)}")
    print(f"加密字串：{encrypted}")
    print("-" * 40)

# 主程式開始
print("=== 文件加密練習 ===\n")

# 測試案例 1: "abcdefghijklmnopqrstuvwxyz" 前移 3
test1_input = "abcdefghijklmnopqrstuvwxyz"
test1_shift = 3
test1_result = encrypt_string(test1_input, test1_shift)
print("測試案例 1:")
print_result(test1_input, test1_shift, test1_result)

# 測試案例 2: "cheer" 前移 7
test2_input = "cheer"
test2_shift = 7
test2_result = encrypt_string(test2_input, test2_shift)
print("測試案例 2:")
print_result(test2_input, test2_shift, test2_result)

# 測試案例 3: "melon" 後移 10 (用負數表示後移)
test3_input = "melon"
test3_shift = -10
test3_result = encrypt_string(test3_input, test3_shift)
print("測試案例 3:")
print_result(test3_input, test3_shift, test3_result)

# 測試案例 4: "sleep" 前移 9
test4_input = "sleep"
test4_shift = 9
test4_result = encrypt_string(test4_input, test4_shift)
print("測試案例 4:")
print_result(test4_input, test4_shift, test4_result)

def print_alphabet_table():
    """顯示字母表對照表"""
    print("📚 字母表對照表：")
    print("原始: " + " ".join([chr(i + ord('a')) for i in range(26)]))
    print("位置: " + " ".join([f"{i:2d}" for i in range(26)]))
    print()

def print_encryption_table(text, shift_amount):
    """用表格形式顯示加密過程"""
    print("📊 加密轉換表格：")
    print("┌─────────┬─────────┬─────────────┬─────────┬─────────┐")
    print("│ 原字母  │ 原位置  │   計算式    │ 新位置  │ 新字母  │")
    print("├─────────┼─────────┼─────────────┼─────────┼─────────┤")
    
    for char in text:
        if 'a' <= char <= 'z':
            char_pos = ord(char) - ord('a')
            new_pos = (char_pos + shift_amount) % 26
            encrypted_char = chr(new_pos + ord('a'))
            
            # 格式化計算式
            if shift_amount >= 0:
                formula = f"({char_pos}+{shift_amount})%26"
            else:
                formula = f"({char_pos}{shift_amount})%26"
            
            print(f"│    {char}    │   {char_pos:2d}    │ {formula:11s} │   {new_pos:2d}    │    {encrypted_char}    │")
    
    print("└─────────┴─────────┴─────────────┴─────────┴─────────┘")
    print()

def print_step_by_step_demo(text, shift_amount):
    """步驟式解釋加密過程"""
    print("🔍 步驟式解釋：")
    direction = "前移" if shift_amount > 0 else "後移"
    print(f"將 '{text}' {direction} {abs(shift_amount)} 位：")
    print()
    
    result = ""
    for i, char in enumerate(text):
        if 'a' <= char <= 'z':
            char_pos = ord(char) - ord('a')
            new_pos = (char_pos + shift_amount) % 26
            encrypted_char = chr(new_pos + ord('a'))
            result += encrypted_char
            
            print(f"步驟 {i+1}: {char} → {encrypted_char}")
            print(f"       位置 {char_pos} → 位置 {new_pos}")
            if new_pos < char_pos and shift_amount > 0:
                print(f"       (超過 z，循環回到字母表開頭)")
            print()
    
    print(f"🎯 最終結果: '{text}' → '{result}'")
    print()

def print_visual_demo():
    """視覺化展示循環概念"""
    print("🔄 字母循環概念展示：")
    print("字母表是循環的，就像時鐘一樣：")
    print()
    print("... → x → y → z → a → b → c → ...")
    print("     22  23  24  25   0   1   2")
    print()
    print("例如：z (位置 25) + 1 = a (位置 0)")
    print("     y (位置 24) + 3 = b (位置 1)")
    print()

# 額外示範：解釋加密原理 (此部分僅供教育用途，並不影響程式的主要功能)
print("\n" + "="*50)
print("🎓 加密原理詳細解釋")
print("="*50)

# 顯示字母表對照
print_alphabet_table()

# 以 'cheer' 前移 7 為例進行詳細解釋
demo_text = "cheer"
demo_shift = 7

print(f"📝 範例：將 '{demo_text}' 前移 {demo_shift} 位")
print("-" * 30)

# 表格式顯示
print_encryption_table(demo_text, demo_shift)

# 步驟式解釋
print_step_by_step_demo(demo_text, demo_shift)

# 循環概念說明
print_visual_demo()

print("💡 重點提醒：")
print("• 使用 ord() 函數將字母轉換為數字")
print("• 使用 chr() 函數將數字轉換回字母") 
print("• 使用 % 26 確保結果在 0-25 範圍內（循環效果）")
print("• 只處理小寫英文字母 a-z")
