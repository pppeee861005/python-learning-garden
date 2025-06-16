from HeartProgressBar import HeartProgressBar
import card_utils
import sound_player
import time

def show_welcome():
    sound_player.read_sound()
    print("🎲🎉 歡迎來到賭場遊戲！🎉🎲")
    print("讓我們開始一場有趣的牌局吧！\n")

def show_menu():
    print("請選擇遊戲模式：")
    print("1️⃣ 印出整副牌的數值編號")
    print("2️⃣ 印出洗牌後的整副牌")
    print("3️⃣ 洗牌後隨機發一張牌，並顯示牌名")
    print("4️⃣ 撲克牌遊戲")
    print("0️⃣ 離開遊戲")

def main():
    show_welcome()
    while True:
        show_menu()
        choice = input("請輸入選項 (0-4): ").strip()
        if choice == "0":
            sound_player.bye_sound()
            print("感謝遊玩！期待下次再見！🎉")
            break
        elif choice in ["1", "2", "3", "4"]:
            
            sound_player.confirm_sound()
            print("\n開始執行，請稍候...🐱")
            time.sleep(2)
            for i in range(101):
                HeartProgressBar(i)
                time.sleep(0.04)
            print()
            if choice == "1":
                time.sleep(2)
                print("\n")
                print("🎉 玩家選擇了第一項選項：印出整副牌的數值編號 🎉")            
                card_utils.print_deck_numbers()
                sound_player.read_sound()
            elif choice == "2":
                print("\n")
                print("🎉 玩家選擇了第二項選項：印出洗牌後的整副牌 🎉")
                card_utils.print_shuffled_deck()
                sound_player.confirm_sound()
            elif choice == "3":
                print("\n")
                print("🎉 玩家選擇了第三項選項：洗牌後隨機發一張牌，並顯示牌名 🎉")
                
                card_utils.deal_random_card()
                sound_player.read_sound()
            elif choice == "4":
                print("\n")
                print("🎉 玩家選擇了第四項選項：撲克牌遊戲 🎉")
                import plus
                plus.play_game()
            print()
            cont = input("是否繼續遊戲？(y/n): ").strip().lower()
            if cont != "y":
                sound_player.bye_sound()
                print("感謝遊玩！期待下次再見！🎉")
                break
        else:
            print("輸入錯誤，請輸入0-4之間的數字。\n")

if __name__ == "__main__":
    main()
