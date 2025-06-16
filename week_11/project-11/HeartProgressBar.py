import sys
import time
from colorama import init, Fore, Style

init(autoreset=True)

def HeartProgressBar(progress, total=100, bar_length=30):
    """
    顯示彩色愛心進度條 💖🤍
    :param progress: 當前進度 (0~total)
    :param total: 總進度，預設100
    :param bar_length: 進度條長度，預設30
    """
    percent = int(progress / total * 100)
    completed = int(bar_length * progress // total)
    remaining = bar_length - completed
    hearts = Fore.RED + "💖" * completed
    empty_hearts = Fore.WHITE + "🤍" * remaining
    # 使用 \r 回到行首，end="" 不換行，並用 flush 確保即時輸出
    print(f"\r{hearts}{empty_hearts} {percent}%", end="", flush=True)

# 測試用範例
if __name__ == "__main__":
    print(Fore.CYAN + "開始進度條展示 🎉")
    for i in range(101):
        HeartProgressBar(i)
        time.sleep(0.05)
    print(Fore.GREEN + "\n完成囉！✨")
