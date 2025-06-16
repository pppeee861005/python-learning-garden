# <加分題>
# 撰寫撲克牌遊戲(規則):
# 1)遊戲開始，問兩個玩家的名字並安排就位.
# 2)每一回合，隨機發一張牌給每個玩家.
# 3)比較剛發的牌：先比花色；如果相同，再比數字大小
# 4)拿到較大牌的玩家，將此牌交給牌面較小的玩家.
# 5)當整副牌發完，比較兩位玩家手中牌數，擁有較少牌數的玩家贏得比賽！  
#####################################################################
import card_utils 
import sound_player

def get_player_names():
    # 取得兩位玩家名字
    sound_player.confirm_sound()
    print("請輸入兩位玩家的名字：")
    player1 = input("玩家1名字：").strip()
    player2 = input("玩家2名字：").strip()
    print(f"歡迎 {player1} 和 {player2} 來到遊戲！🎉\n")
    return player1, player2

def create_deck():
    # 調用card_utils.py中的whole_deck()函式來創建牌堆
    return card_utils.whole_deck()

def shuffle_deck(deck):
    # 洗牌
    import random
    random.shuffle(deck)
    return deck

def deal_card(deck):
    # 從牌堆抽一張牌
    if deck:
        return deck.pop()
    else:
        return None

def compare_cards(card1, card2):
    # 比較兩張牌大小，先比花色，再比數字
    suit_order = {4: 4, 3: 3, 2: 2, 1: 1}  # 4=黑桃,3=紅心,2=方塊,1=梅花
    suit1, rank1 = divmod(card1, 100)
    suit2, rank2 = divmod(card2, 100)
    if suit_order[suit1] > suit_order[suit2]:
        return 1
    elif suit_order[suit1] < suit_order[suit2]:
        return -1
    else:
        if rank1 > rank2:
            return 1
        elif rank1 < rank2:
            return -1
        else:
            return 0


import random
import card_utils

def play_game():
    # 遊戲主流程
    player1, player2 = get_player_names()
    deck = card_utils.whole_deck()
    random.shuffle(deck)

    # 初始化玩家手牌
    
    player1_hand = []
    player2_hand = []

    # 花色大小排序，黑桃最大
    suit_order = {4: 4, 3: 3, 2: 2, 1: 1}  # 4=黑桃,3=紅心,2=方塊,1=梅花

    def compare_cards(card1, card2):
        # 先比花色，再比數字大小
        suit1, rank1 = divmod(card1, 100)
        suit2, rank2 = divmod(card2, 100)
        if suit_order[suit1] > suit_order[suit2]:
            return 1
        elif suit_order[suit1] < suit_order[suit2]:
            return -1
        else:
            if rank1 > rank2:
                return 1
            elif rank1 < rank2:
                return -1
            else:
                return 0

    round_num = 1
    while len(deck) >= 2:
        import sound_player
        print(f"\n第 {round_num} 回合開始！🎴")
        sound_player.round_start_sound()
        card1 = deck.pop()
        card2 = deck.pop()
        print(f"{player1} 抽到的牌是：{card_utils.card_name(card1)}")
        print(f"{player2} 抽到的牌是：{card_utils.card_name(card2)}")

        result = compare_cards(card1, card2)
        if result == 1:
            print(f"{player1} 的牌較大，將牌交給 {player2} 🃏")
            player2_hand.append(card2)
        elif result == -1:
            print(f"{player2} 的牌較大，將牌交給 {player1} 🃏")
            player1_hand.append(card1)
        else:
            print("兩張牌相同，無人交換牌。")

        import time
        time.sleep(1)
        
        


        round_num += 1

    print("\n遊戲結束！計算結果中...⏳")
    sound_player.round_end_sound()
    print(f"{player1} 手中牌數：{len(player1_hand)}")
    print(f"{player2} 手中牌數：{len(player2_hand)}")

    if len(player1_hand) < len(player2_hand):
        print(f"🎉 {player1} 獲勝！恭喜！🎉")
    elif len(player1_hand) > len(player2_hand):
        print(f"🎉 {player2} 獲勝！恭喜！🎉")
    else:
        print("平手！真是勢均力敵！🤝")

if __name__ == "__main__":
    play_game()
