# 🎨 彩色圖形展示
# 檔案名稱：colorful_shapes.py

import pygame
import sys

pygame.init()

# 視窗設定
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("🌈 彩色圖形展示 - Python 藝術花園")

# 顏色定義
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# 遊戲主迴圈
running = True
clock = pygame.time.Clock()

print("🎨 彩色圖形展示開始！")
print("🌈 你會看到各種美麗的圖形")
print("❌ 點擊視窗右上角的 X 可以關閉視窗")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("🎭 藝術展示結束，謝謝欣賞！")
    
    # 白色背景
    screen.fill(WHITE)
    
    # 繪製彩色圖形
    # 紅色圓形
    pygame.draw.circle(screen, RED, (200, 150), 50)
    
    # 綠色矩形
    pygame.draw.rect(screen, GREEN, (300, 100, 100, 100))
    
    # 藍色三角形（用多邊形繪製）
    pygame.draw.polygon(screen, BLUE, [(500, 100), (450, 200), (550, 200)])
    
    # 黃色橢圓
    pygame.draw.ellipse(screen, YELLOW, (150, 300, 120, 80))
    
    # 紫色線條
    pygame.draw.line(screen, PURPLE, (50, 50), (750, 550), 5)
    
    # 橙色圓環
    pygame.draw.circle(screen, ORANGE, (600, 400), 60, 8)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
