import pygame
import threading
import time

pygame.mixer.init()

def confirm_sound():
    """播放確認音效 check.mp3"""
    play_sound("week_11/project-11/「はいは～い♪」.mp3")

def read_sound():
    """讀取並播放指定路徑的音效檔"""
    play_sound("week_11/project-11/check.mp3")

def bye_sound():
    """示範播放音效功能，播放 check.mp3"""
    play_sound("week_11/project-11/「バイバーイ」.mp3")

def round_start_sound():
    """播放回合開始音效，キャンセル7.mp3"""
    play_sound("week_11/project-11/キャンセル7.mp3")

def round_end_sound():
    """播放回合結束音效，お疲れ様です.mp3"""
    play_sound("week_11/project-11/「お疲れ様です」.mp3")

def play_sound(file_path):
    def _play():
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    # 使用執行緒避免阻塞主程式
    thread = threading.Thread(target=_play)
    thread.start()

if __name__ == "__main__":
    print("示範播放確認音效 🎵")
    bye_sound()
    time.sleep(1)
    confirm_sound()
    time.sleep(1)
    read_sound()
