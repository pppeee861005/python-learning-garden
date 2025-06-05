#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
走馬燈程式 - 捷運站訊息顯示
模擬捷運站的走馬燈效果，讓訊息優雅地滾動顯示
按 Ctrl+C 可以終止程式
"""

import time
import os
import sys

def clear_screen():
    """清除螢幕內容，讓顯示更乾淨"""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_marquee_frame(message, position, screen_width=50):
    """
    創建走馬燈的單一畫面
    
    參數:
        message: 要顯示的訊息
        position: 目前文字的位置
        screen_width: 螢幕寬度
    
    回傳:
        格式化後的顯示字串
    """
    # 在訊息前後加上空格，讓滾動效果更自然
    full_message = " " * screen_width + message + " " * screen_width
    
    # 計算要顯示的部分
    start_pos = position % len(full_message)
    display_text = full_message[start_pos:start_pos + screen_width]
    
    # 如果不夠長，從頭補齊
    if len(display_text) < screen_width:
        display_text += full_message[:screen_width - len(display_text)]
    
    return display_text

def main():
    """主程式：執行走馬燈效果"""
    
    # 捷運站訊息
    train_message = "列車將進站 請勿靠近車門 以免夾傷"
    
    # 顯示設定
    screen_width = 50  # 螢幕寬度
    scroll_speed = 0.2  # 滾動速度（秒）
    position = 0  # 目前位置
    
    print("=" * 60)
    print("🚇 捷運站走馬燈系統啟動 🚇")
    print("=" * 60)
    print("按 Ctrl+C 可以終止程式")
    print("=" * 60)
    print()
    
    try:
        while True:
            # 清除螢幕（可選，讓效果更流暢）
            # clear_screen()
            
            # 創建當前畫面
            display_line = create_marquee_frame(train_message, position, screen_width)
            
            # 顯示走馬燈
            print(f"\r[{display_line}]", end="", flush=True)
            
            # 移動位置
            position += 1
            
            # 等待一段時間
            time.sleep(scroll_speed)
            
    except KeyboardInterrupt:
        # 當使用者按 Ctrl+C 時優雅地結束
        print("\n")
        print("=" * 60)
        print("🚇 走馬燈系統已安全關閉，感謝使用！ 🚇")
        print("=" * 60)
        sys.exit(0)

if __name__ == "__main__":
    main()
