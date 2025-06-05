text = (
    "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 "
    "steve@apple.com brian@ibm.com rocky@google.com Mon Jan 7"
)

print(" 【方法一:使用str.find() 】")#11122
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
    domain = text[at_pos + 1:space_pos]
    domains.append(domain)
    start = space_pos + 1
print(tuple(domains))

print("\n 【方法二 : 使用str.split() 】")
words = text.split()
domains = []

for word in words:
    if '@' in word:
        
    # 以@分割字串，取後半部分
        part = word.split('@')
        print("part是:",part)
    
        if len(part) == 2:
            domain = part[1]
            domains.append(domain)

print(tuple(domains))