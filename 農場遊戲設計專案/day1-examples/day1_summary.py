# 📚 今天的學習心得
# 檔案名稱：day1_summary.py

import time

def print_with_delay(text, delay=0.5):
    """帶延遲效果的輸出"""
    print(text)
    time.sleep(delay)

print("🌸" * 50)
print("📚 第一天學習心得總結")
print("🌸" * 50)

print_with_delay("✅ 今天我學會了：")
print_with_delay("   🔹 Python 基本語法（變數、資料型別）")
print_with_delay("   🔹 使用 print() 輸出美麗的文字")
print_with_delay("   🔹 import 模組的使用方法")
print_with_delay("   🔹 time 模組製作動畫效果")
print_with_delay("   🔹 input() 與使用者互動")
print_with_delay("   🔹 型別轉換的技巧")
print_with_delay("   🔹 Pygame 建立第一個視窗")
print_with_delay("   🔹 在 Pygame 中繪製彩色圖形")

print_with_delay("\n🌟 我最喜歡的部分：")
favorite = input("請輸入你最喜歡的學習內容：")

print_with_delay(f"\n🎉 太棒了！{favorite} 確實很有趣！")
print_with_delay("🌱 明天我們將學習更多進階內容！")
print_with_delay("💪 繼續加油，Python 學習花園等著你！")

print("🌸" * 50)
