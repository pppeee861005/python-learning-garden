# 🌟 個人資料練習
# 檔案名稱：my_profile.py
# 這是你的練習作業，請修改成你自己的資料！

# 🎨 請在這裡填入你的個人資料
name = "請輸入你的名字"
age = 0  # 請輸入你的年齡
hobby = "請輸入你的興趣"
favorite_color = "請輸入你最喜歡的顏色"
dream = "請輸入你的夢想"

# 🌈 美麗的個人檔案輸出
print("✨" * 40)
print("🌟 我的個人檔案")
print("✨" * 40)

print(f"👋 大家好！我是 {name}")
print(f"🎂 我今年 {age} 歲")
print(f"🎨 我最喜歡的興趣是：{hobby}")
print(f"🌈 我最喜歡的顏色是：{favorite_color}")
print(f"💫 我的夢想是：{dream}")

# 🎯 根據年齡給出鼓勵話語
if age < 15:
    print("🌱 你還很年輕，有無限的可能性！")
elif age < 25:
    print("🌟 青春年華，正是學習的好時光！")
elif age < 40:
    print("🌸 人生正精彩，繼續追求夢想！")
else:
    print("🌺 經驗豐富，智慧滿滿！")

print("✨" * 40)
print("🎉 很高興認識你！")
print("💪 一起在 Python 學習花園中成長吧！")
