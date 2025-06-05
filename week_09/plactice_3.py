# Python x ChatGPT
# String parse & extract - 字串與迴圈
#
# [練習三]
# 字串解析與擷取
#
# 問題：有字串如下, 請擷取並印出所有在 '@' 字元後的網域名稱
# 輸入：
#    'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 \
#     steve@apple.com brian@ibm.com rocky@google.com Mon Jan 7'
# 輸出：
#    (uct.ac.za, apple.com, ibm.com, google.com)
#
# (請分別使用 str.find() 與 str.split() 方法撰寫程式)

text = (
    "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 "
    "steve@apple.com brian@ibm.com rocky@google.com Mon Jan 7"
)

print("【方法一：使用 str.find()】")
domains = []
start = 0
while True:
    at_pos = text.find('@', start)
    if at_pos == -1:
        break
    # 找到 @ 後，往後找空白或結尾
    space_pos = text.find(' ', at_pos)
    if space_pos == -1:
        space_pos = len(text)
    domain = text[at_pos+1:space_pos]
    domains.append(domain)
    start = at_pos + 1
print(tuple(domains))

print("\n【方法二：使用 str.split()】")
domains2 = []
words = text.split()
for word in words:
    if '@' in word:
        # 以 @ 分割，取後半段
        parts = word.split('@')
        if len(parts) == 2:
            domains2.append(parts[1])
print(tuple(domains2))


# 美感說明：
# 1. 兩種方法都能優雅地擷取網域名稱。
# 2. 第一種用 find()，像在字串裡尋寶。
# 3. 第二種用 split()，像把句子切成一片片，挑出有 @ 的部分。
# 4. 結果都會印出 (uct.ac.za, apple.com, ibm.com, google.com)
