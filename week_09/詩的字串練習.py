# [練習二] 字串長度、搜尋 - 再別康橋 🌸
# 用程式碼品味徐志摩的詩意美學

print("=" * 60)
print("🌸 練習二：字串處理與搜尋 - 再別康橋 🌸")
print("=" * 60)

# 徐志摩的經典詩作「再別康橋」
cambridge_poem = """輕輕的我走了，正如我輕輕的來；我輕輕的招手，作別西天的雲彩。
那河畔的金柳，是夕陽中的新娘；波光裡的豔影，在我的心頭蕩漾。
軟泥上的青荇，油油的在水底招搖；在康河的柔波裡，我甘心做一條水草
那樹蔭下的一潭，不是清泉，是天上虹；揉碎在浮藻間，沉澱著彩虹似的夢。
尋夢？撐一支長篙，向青草更青處漫溯，滿載一船星輝，在星輝斑斕裡放歌
但我不能放歌，悄悄是別離的笙簫；夏蟲也為我沉默，沉默是今晚的康橋！
悄悄的我走了，正如我悄悄的來；我揮一揮衣袖，不帶走一片雲彩。"""

# 1️⃣ 列出完整的詩歌字串
print("\n📜 新詩字串內容：")
print("-" * 50)
print(cambridge_poem)

# 2️⃣ 切分字串為列表（按行分割）
poem_lines = cambridge_poem.split('\n')
print("\n📝 新詩串列內容 :")
print("-" * 50)
for i, line in enumerate(poem_lines, 1):
    print(f"第{i}行: {line}")

# 3️⃣ 統計詩歌的行數和字數
line_count = len(poem_lines)
total_characters = sum(len(line)for line in poem_lines)

print("\n📊 統計資訊：")
print("-" * 50)
print(f"🔢 詩歌行數：{line_count}")
print(f"📝詩歌字數：{total_characters}")

# 4️⃣ 互動式字串搜尋功能
print("\n🔍 字串搜尋功能：")
while True:
    search_word = input("請輸入搜尋字串(輸入 'quit' 結束) :")
    
    if search_word.lower() == 'quit':
        print("👋 感謝使用，再見!")
        break

    if search_word.strip() == "":
        print("⚠️ 請輪入有效的搜尋字串")
        continue
    
    # 計算搜尋字串出現的次數
    count = cambridge_poem.count(search_word)
    
    if count > 0:
        print(f"✨ 搜尋的字：「{search_word}」共出現 {count} 次")
        
        # 額外功能：顯示出現在哪些行
        print("📍 出現位置 :")
        for i, line in enumerate(poem_lines, 1):
            if search_word in line:
                print(f"   第{i}行:{line}")
    else:
        print(f"❌ 搜尋的字:「{search_word}」沒有出現在詩中")
    
    print("-" * 30)

print("\n🎉 程式執行完畢！")
