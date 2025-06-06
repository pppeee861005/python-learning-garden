# 🤖 自我介紹小機器人
# 檔案名稱：intro_bot.py

print("🤖 哈囉！我是你的 Python 小助手！")
print("🌟 讓我們來認識一下吧！")

# 收集使用者資訊
name = input("👋 請告訴我你的名字：")
age_str = input("🎂 請告訴我你的年齡：")
hobby = input("🎨 你最喜歡的興趣是什麼：")

# 型別轉換
age = int(age_str)  # 字串轉整數

# 計算一些有趣的數據
next_year_age = age + 1
birth_year = 2024 - age

# 美麗的輸出
print("\n" + "🌸" * 40)
print("📋 你的個人檔案：")
print("🌸" * 40)
print(f"🌟 姓名：{name}")
print(f"🎂 年齡：{age} 歲")
print(f"🎯 興趣：{hobby}")
print(f"📅 出生年份：約 {birth_year} 年")
print(f"🎈 明年你就 {next_year_age} 歲了！")

# 個性化訊息
if age < 18:
    print("🌱 你還很年輕，未來充滿無限可能！")
elif age < 30:
    print("🌟 正值青春年華，是學習的黃金時期！")
else:
    print("🌸 人生經驗豐富，學習永遠不嫌晚！")

print("🌸" * 40)
print(f"🎉 很高興認識你，{name}！")
