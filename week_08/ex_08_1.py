import random

def guess(x):
    """
    玩家指定數字上限，並與電腦互動猜測其隨機產生的數字
    :param (int) x: 要猜測的數字之範圍上限
    """
    secret_number = random.randint(1, x)
    while True:
        user_guess = int(input(f"猜一個 1-{x} 間的數字: "))
        if user_guess < secret_number:
            print("太小了！請再猜個數字")
        elif user_guess > secret_number:
            print("太大了！請再猜個數字")
        else:
            print(f"恭喜你猜對了秘密數字 {secret_number} !!")
            break

def computer_guess(x):
    """
    玩家選定數字，並與電腦互動，由電腦猜測此數字
    :param (int) x: 要猜測的數字之範圍上限
    """
    print(f"請選定一個 1-{x} 間的數字，並記住")
    low, high = 1, x
    while True:
        computer_guess = random.randint(low, high)
        user_hint = input(f"我猜 {computer_guess}，太高(H)/太低(L) 或 正確(C)?? ")
        if user_hint.upper() == "H":
            high = computer_guess - 1
        elif user_hint.upper() == "L":
            low = computer_guess + 1
        elif user_hint.upper() == "C":
            print(f"耶~ 電腦猜對了你的秘密 {computer_guess} !!")
            break
        else:
            print("無效的輸入，請重新輸入")

# Test the functions
guess(100)
computer_guess(100)