#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
簡易走馬燈程式 - 適合初學者
讓文字像捷運站一樣滾動顯示
"""

import time

def main():
    # 要顯示的訊息
    message = "列車將進站 請勿靠近車門 以免夾傷"
    
    # 螢幕寬度
    width = 40
    
    # 在訊息前後加上空格，讓滾動更自然
    full_text = " " * width + message + " " * width
    
    print("🚇 捷運站走馬燈 🚇")
    print("按 Ctrl+C 停止")
    print("-" * (width + 2))
    
    try:
        position = 0
        while True:
            # 取出要顯示的部分
            display = full_text[position:position + width]
            
            # 顯示文字（\r 讓文字在同一行更新）
            print(f"\r{display}", end="", flush=True)
            
            # 移動到下一個位置
            position += 1
            
            # 如果滾動完了，重新開始
            if position >= len(full_text) - width:
                position = 0
            
            # 等待 0.15 秒
            time.sleep(0.15)
            
    except KeyboardInterrupt:
        print("\n\n🚇 走馬燈已停止，謝謝使用！")

if __name__ == "__main__":
    main()
