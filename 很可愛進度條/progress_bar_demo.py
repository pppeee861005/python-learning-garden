"""
🌈 美麗的進度條展示程式 🌈
作者：您的Python老師
功能：展示多種風格的進度條效果
"""

import time
import sys
import random

def print_header():
    """印出美麗的標題"""
    print("=" * 60)
    print("🎨 歡迎來到進度條的美麗世界！ 🎨".center(60))
    print("=" * 60)
    print()

def simple_progress_bar(total=50):
    """簡單的文字進度條 📊"""
    print("🔹 簡單進度條展示：")
    print()
    
    for i in range(total + 1):
        # 計算進度百分比
        percent = (i / total) * 100
        
        # 創建進度條視覺效果
        filled = int(i / 2)  # 每2個單位填充一個字符
        bar = "█" * filled + "░" * (25 - filled)
        
        # 顯示進度條
        print(f"\r進度: [{bar}] {percent:5.1f}% ({i}/{total})", end="")
        sys.stdout.flush()
        
        # 模擬工作時間
        time.sleep(0.1)
    
    print("\n✅ 完成！\n")

def colorful_progress_bar(total=30):
    """彩色進度條 🌈"""
    print("🔹 彩色進度條展示：")
    print()
    
    # ANSI 顏色代碼
    colors = [
        '\033[91m',  # 紅色
        '\033[93m',  # 黃色
        '\033[92m',  # 綠色
        '\033[96m',  # 青色
        '\033[94m',  # 藍色
        '\033[95m'   # 紫色
    ]
    reset = '\033[0m'  # 重置顏色
    
    for i in range(total + 1):
        percent = (i / total) * 100
        filled = int((i / total) * 40)
        
        # 選擇顏色（根據進度變化）
        color_index = int((i / total) * (len(colors) - 1))
        current_color = colors[color_index]
        
        # 創建彩色進度條
        bar = current_color + "●" * filled + reset + "○" * (40 - filled)
        
        print(f"\r進度: [{bar}] {current_color}{percent:5.1f}%{reset}", end="")
        sys.stdout.flush()
        
        time.sleep(0.15)
    
    print("\n🎉 彩色進度條完成！\n")

def emoji_progress_bar(total=20):
    """表情符號進度條 😊"""
    print("🔹 表情符號進度條展示：")
    print()
    
    emojis = ["😴", "😪", "🙂", "😊", "😄", "🤩", "🎉"]
    
    for i in range(total + 1):
        percent = (i / total) * 100
        filled = int((i / total) * 30)
        
        # 根據進度選擇表情符號
        emoji_index = int((i / total) * (len(emojis) - 1))
        current_emoji = emojis[emoji_index]
        
        # 創建表情符號進度條
        bar = "🟩" * filled + "⬜" * (30 - filled)
        
        print(f"\r{current_emoji} 進度: [{bar}] {percent:5.1f}%", end="")
        sys.stdout.flush()
        
        time.sleep(0.2)
    
    print("\n🎊 表情符號進度條完成！\n")

def loading_animation():
    """載入動畫效果 ⏳"""
    print("🔹 載入動畫展示：")
    print()
    
    animations = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    messages = [
        "正在準備資料...",
        "正在處理中...",
        "即將完成...",
        "最後檢查..."
    ]
    
    for message in messages:
        for _ in range(10):  # 每個訊息顯示10次動畫
            for frame in animations:
                print(f"\r{frame} {message}", end="")
                sys.stdout.flush()
                time.sleep(0.1)
        print()  # 換行
    
    print("✨ 載入完成！\n")

def download_simulation():
    """模擬下載進度條 📥"""
    print("🔹 模擬檔案下載：")
    print()
    
    file_size = 1024  # KB
    downloaded = 0
    
    while downloaded < file_size:
        # 隨機下載速度
        chunk = random.randint(10, 50)
        downloaded = min(downloaded + chunk, file_size)
        
        percent = (downloaded / file_size) * 100
        filled = int((downloaded / file_size) * 50)
        
        bar = "█" * filled + "▒" * (50 - filled)
        speed = chunk * 10  # 模擬KB/s
        
        print(f"\r📥 下載: [{bar}] {percent:5.1f}% ({downloaded}/{file_size}KB) {speed}KB/s", end="")
        sys.stdout.flush()
        
        time.sleep(0.1)
    
    print("\n📁 檔案下載完成！\n")

def main():
    """主程式 🚀"""
    print_header()
    
    try:
        # 展示各種進度條
        simple_progress_bar()
        time.sleep(1)
        
        colorful_progress_bar()
        time.sleep(1)
        
        emoji_progress_bar()
        time.sleep(1)
        
        loading_animation()
        time.sleep(1)
        
        download_simulation()
        
        # 結束訊息
        print("=" * 60)
        print("🎊 所有進度條展示完成！感謝您的觀看！ 🎊".center(60))
        print("💡 您現在可以在自己的程式中使用這些進度條了！".center(60))
        print("=" * 60)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  程式被使用者中斷")
        print("👋 再見！")

if __name__ == "__main__":
    main()
