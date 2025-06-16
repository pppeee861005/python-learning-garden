# 🎨 我的第一個 Pygame 視窗
# 檔案名稱：first_pygame_window.py

import pygame
import sys

# 初始化 Pygame
pygame.init()

# 設定視窗大小
window_width = 800
window_height = 600
# 定義顏色（RGB 值）
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 250)
PINK = (255, 192, 203)
LIGHT_GREEN = (144, 238, 144)
# 建立視窗
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("  🌸我的第一個pygamer視客窗耶耶耶")

# 遊戲主迴圈
running = True
clock = pygame.time.Clock()

print("🎮 Pygame視窗已經啟動，開始玩吧 ! ")
print("❌ jng 按按xx關掉 ")

while running:
    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("👋 isa 謝謝 再見 881 ")
    
    # 填充背景色
    screen.fill(SKY_BLUE)
    
    # 更新顯示
    pygame.display.flip()
    
    # 控制幀率
    clock.tick(60)

# 結束 Pygame
pygame.quit()
sys.exit()
