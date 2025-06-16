import pygame
import sys
from 主程式 import show_welcome

# 初始化pygame
pygame.init()

# 設定視窗大小
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("賭場遊戲 Pygame 視窗 🎲")

# 設定字型，改用支援中文的字型
font = pygame.font.SysFont("Microsoft JhengHei", 30)

# 呼叫主程式的歡迎函式，取得歡迎訊息
def get_welcome_text():
    import io
    import sys
    # 將標準輸出暫存起來
    buffer = io.StringIO()
    sys.stdout = buffer
    show_welcome()
    sys.stdout = sys.__stdout__
    return buffer.getvalue()

welcome_text = get_welcome_text()

# 將歡迎訊息分行
lines = welcome_text.splitlines()

# 主迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))  # 深色背景

    # 顯示歡迎訊息
    y = 50
    for line in lines:
        text_surface = font.render(line, True, (255, 215, 0))  # 金黃色文字
        screen.blit(text_surface, (50, y))
        y += 40

    pygame.display.flip()

pygame.quit()
sys.exit()
