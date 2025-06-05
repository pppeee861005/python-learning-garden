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
        # 將字母轉換為對應的 ASCII 數值
        # 將字母轉換為數字 (a=0, b=1, ..., z=25)
        char_num = ord(char) - ord('a')
        
        # 進行移動並處理循環 (用 % 26 確保結果在 0-25 範圍內)
        new_char_num = (char_num + shift_amount) % 26
        # 如果移動後的數字小於 0，則加上 26 以確保是正數
        
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
        # 呼叫 shift_char 函數來加密每個字元
        encrypted_char = shift_char(char, shift_amount)
        # 將加密後的字元加入到結果字串中
        encrypted += encrypted_char
    
    # 回傳加密後的字串
    return encrypted

def print_result(original, shift, encrypted):
    """
    印出結果的函數，讓輸出格式統一
    """
    direction = "前移" if shift > 0 else "後移"
    print(f"輸入字串: {original} {direction} {abs(shift)}")
    print(f"加密字串: {encrypted}")
    print("-" * 40)

# 主程式開始
print("=== 文件加密 - 凱薩密碼 ===")

# 測試案例 1: "abcdefghijklmnopqrstuvwxyz" 前移 3
test1_input = "abcdefghijklmnopqrstuvwxyz"
test1_shft = 3
test_result = encrypt_string(test1_input, test_shift)
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
# 額外示範：解釋加密原理

print("\n=== 加密原理解釋 ===")
print("以 'cheer' 前移 7 為例：")
for i, char in enumerate("cheer"):
    encrypted_char = shift_char(char, 7)
    char_pos = ord(char) - ord('a')
    new_pos = (char_pos + 7) % 26
    print(f"{char} (位置{char_pos}) + 7 = {encrypted_char} (位置{new_pos})")
