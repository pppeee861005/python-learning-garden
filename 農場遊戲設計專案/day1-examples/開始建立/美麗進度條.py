# 🎨 美麗的進度條
# 檔案名稱：beautiful_progress.py

import time

print("\n\n\n")

def show_progress(task_name, duration=5):
    """顯示美麗的進度條"""
    print(f"🌱 開始任務：{task_name}")
    
    for i in range(duration + 1):
        # 計算進度百分比
        progress = i / duration * 100
        # 每一次跳10%
        # 創建進度條
        filled = int(progress // 10)# 每 10% 算一格
        bar = "🌸" * filled + "🌿" *(10 - filled)#第一輪一個花，10-1個草...
        
        # 顯示進度
        
        print(f"\r🌈 進度：〈{bar} 〉{progress:.0f}%" ,end="")
        
        time.sleep(1)
    
    print(f"\n✅ {task_name} 完成！")

# 執行範例
show_progress("我要 大大便 ", 10)
