# 🕰️ 時間魔法師
# 檔案名稱：time_magic.py

import time  # 導入時間模組

print("🌅 早安！準備開始時間魔法...")
print("⏰ 3 秒後見證奇蹟...")

# 暫停 3 秒
time.sleep(3)

print("✨ 魔法發生了！")
print("🌈 彩虹出現啦！")

# 倒數計時器
print("\n🚀 火箭發射倒數：")
for i in range(5, 0, -1):
    print(f"⭐ {i}...")
    time.sleep(1)

print("🎆 發射成功！🚀")
