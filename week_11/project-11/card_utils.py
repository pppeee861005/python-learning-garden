import random

# 花色與符號對照表
suites = {
    1: '♧',  # Club
    2: '♦️',  # Diamond
    3: '♥️',  # Heart
    4: '♤'   # Spade
}

# 牌面名稱對照表
ranks = {
    11: 'J 👑',
    12: 'Q 👸',
    13: 'K 🤴',
    14: 'A 🅰️'
}

def whole_deck():
    """產生整副牌(數值編號)並回傳"""
    deck = []
    for suite in range(1, 5):
        for rank in range(2, 15):
            deck.append(suite * 100 + rank)
    return deck

def pretty_print_deck(deck):
    """依花色分組印出牌組"""
    for suite in range(1, 5):
        cards = [str(card) for card in deck if card // 100 == suite]
        print(f"{suites[suite]}: {' '.join(cards)}")

def card_name(card):
    """根據數值編號回傳牌名"""
    suite_num = card // 100
    rank_num = card % 100
    suite = suites.get(suite_num, '❓')
    rank = ranks.get(rank_num, str(rank_num))
    return f"{suite}{rank}"

def print_deck_numbers():
    """印出整副牌的數值編號"""
    deck = whole_deck()
    pretty_print_deck(deck)

def print_shuffled_deck():
    """洗牌並印出整副牌"""
    deck = whole_deck()
    random.shuffle(deck)
    pretty_print_deck(deck)

def deal_random_card():
    """洗牌後隨機發一張牌並顯示牌名"""
    deck = whole_deck()
    random.shuffle(deck)
    card = random.choice(deck)
    print(f"隨機抽發一張牌：{card} - {card_name(card)}")
