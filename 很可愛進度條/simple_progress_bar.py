"""
🌟 簡單進度條學習版 🌟
適合Python初學者學習
"""

import time

def my_first_progress_bar():
    """我的第一個進度條 🎯"""
    print("🎨 歡迎學習進度條！")
    print("=" * 40)
    print()
    
    # 設定總共要完成的工作量
    total_work = 20
    
    print("開始工作... 💪")
    
    # 用迴圈來模擬工作進度
    for i in range(total_work + 1):
        # 計算完成的百分比
        percentage = (i / total_work) * 100
        
        # 創建進度條的視覺效果
        filled_blocks = int(i / 2)  # 每2個單位顯示一個方塊
        progress_bar = "■" * filled_blocks + "□" * (10 - filled_blocks)
        
        # 顯示進度（\r 讓文字在同一行更新）
        print(f"\r進度: [{progress_bar}] {percentage:5.1f}%", end="")
        
        # 暫停一下，讓我們看到進度變化
        time.sleep(0.2)
    
    print("\n🎉 工作完成！")
    print()

def cute_progress_bar():
    """可愛的進度條 🐱"""
    print("🐱 可愛進度條展示：")
    print()
    
    total = 15
    
    for i in range(total + 1):
        percentage = (i / total) * 100
        
        # 用可愛的符號做進度條
        hearts = "💖" * i
        empty = "🤍" * (total - i)
        
        print(f"\r可愛度: {hearts}{empty} {percentage:5.1f}%", end="")
        time.sleep(0.3)
    
    print("\n😍 超級可愛！")
    print()

def learning_progress():
    """學習進度條 📚"""
    print("📚 學習Python的進度：")
    print()
    
    subjects = [
        "變數和資料型態 📝",
        "條件判斷 🤔", 
        "迴圈 🔄",
        "函數 ⚙️",
        "串列 📋",
        "字典 📖"
    ]
    
    total_subjects = len(subjects)
    
    for i, subject in enumerate(subjects):
        percentage = ((i + 1) / total_subjects) * 100
        filled = "🟢" * (i + 1)
        empty = "⚪" * (total_subjects - i - 1)
        
        print(f"\r學習進度: [{filled}{empty}] {percentage:5.1f}% - 正在學習: {subject}", end="")
        time.sleep(1.5)
    
    print("\n🎓 恭喜！Python基礎學習完成！")
    print()

def main():
    """主程式 - 展示所有進度條"""
    print("🌈" * 20)
    print("歡迎來到進度條學習樂園！".center(40))
    print("🌈" * 20)
    print()
    
    # 展示第一個進度條
    my_first_progress_bar()
    
    # 等待一下
    time.sleep(1)
    
    # 展示可愛進度條
    cute_progress_bar()
    
    # 等待一下
    time.sleep(1)
    
    # 展示學習進度條
    learning_progress()
    
    # 結束語
    print("✨" * 40)
    print("🎊 進度條學習完成！您真棒！ 🎊".center(40))
    print("💡 現在您可以自己製作進度條了！".center(40))
    print("✨" * 40)

# 如果直接執行這個檔案，就會執行main函數
if __name__ == "__main__":
    main()
