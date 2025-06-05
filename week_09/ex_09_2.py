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

def shift_char(c, shift):
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
    else:
        return c

def encrypt(text, shift):
    return ''.join(shift_char(c, shift) for c in text)

# 測試資料
test_cases = [
    ("abcdefghijklmnopqrstuvwxyz", -3),  # 前移3
    ("cheer", -7),                      # 前移7
    ("melon", 10),                      # 後移10
    ("sleep", -9),                      # 前移9
]

for s, shift in test_cases:
    print(f"輸入字串：{s} 移動位數 {abs(shift)}{'前移' if shift < 0 else '後移'}")
    print(f"加密字串：{encrypt(s, shift)}")
    print()
