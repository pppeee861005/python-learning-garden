# [作業二]
# 文件加密
#
# 最簡單的加密是將每個英文字元在 26 個英文字母
# (大、小寫各 26 個)中旋轉往前移，對應至不同字母；
# 記住所對應字母，未來便可解密。
#
# 如 加密方式：將每個字元前移 3 個在英文字母中的次序，
# 即：a對應到d；b對e； .. x對a；y對b；z對c
#
# 請撰寫程式加密以下輸入字串：
#   1) "abcdefghijklmnopqrstuvwxyz" 前移 3
#   2) "cheer" 前移 7
#   3) "melon" 後移 10
#   4) "sleep" 前移 9
#
# 印出：1)輸入字串 與 2)加密字串
#
# (如)：
# 輸入字串：cheer 移動位數 7
# 加密字串：jolly
#
# (提示)：化整為零，先寫個函數可以移動字元(字母)，
#         再在移動字串時呼叫此函數。
###############################################################
def shift_char(char, shift_amount): 
    """
    移動單個字母的函數
    
    參數:
        char: 要移動的字母 (a-z)
        shift_amount: 移動的位數 (正數往前移，負數往後移)
    
    回傳:
        移動後的字母
    """
    #檢查字元是否為小寫字母
    if 'a' <= char <= 'z':
        #將字元轉換為對應的 ASCII 數值
        # ord('a') = 97
        # ord('z') = 122    
        #將字元轉換為對應的數字位置 (0-25)
        char_num = ord(char) - ord('a')
        #進行移動並處理循環 (用 % 26 確保結果在 0-25 範圍內)
        new_char_num = (char_num + shift_amount) % 26
        #將數字轉回字母
        new_char = chr(new_char_num + ord('a'))
        return new_char
    else:
        #如果不是小寫字母，直接回傳原字元
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
print("=== 作業二: 文件加密練習 ===\n")
# 測試案例一
test1 = "abcdefghijklmnopqrstuvwxyz"
test1_shift = 3
test1_encrypted = encrypt_string(test1, test1_shift)
print("測試案例一")
print_result(test1, test1_shift, test1_encrypted)
# 測試案例二
test2 = "cheer"
test2_shift = 7
test2_encrypted = encrypt_string(test2, test2_shift)
print("測試案例二")
print_result(test2, test2_shift, test2_encrypted)
# 測試案例三
test3 = "melon"
test3_shift = -10 # 後移 10
test3_encrypted = encrypt_string(test3, test3_shift)
print("測試案例三")
print_result(test3, test3_shift, test3_encrypted)
# 測試案例四
test4 = "sleep"
test4_shift = 9
test4_encrypted = encrypt_string(test4, test4_shift)
print("測試案例四")
print_result(test4, test4_shift, test4_encrypted)

#額外示範:解釋加密原理
print("\n=== 加密原理示範 ===\n")
print("以 'cheer' 前移 7 為例：")
for char in "cheer":
    encrypted_char = shift_char(char, 7)
    # 計算原字元和加密後字元的字母位置
    original_pos = ord(char) - ord('a')
    # 計算加密後字元的字母位置
    encrypted_pos = ord(encrypted_char) - ord('a')
    print(f"{char} (位置{original_pos}) + 7 = {encrypted_char} (位置{encrypted_pos})")