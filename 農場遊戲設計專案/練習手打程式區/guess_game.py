import random

def player_guess():
    """
    玩家指定數字上限，並與電腦互動猜測其隨機產生的數字
    :param (int) x: 要猜測的數字之範圍上限
    """
    #提示要求輸入猜測數字的範噹圍上限
    up = int(input("請輸入猜測數字的範圍上限 :"))
    # 電腦隨機產生 1~x 間的任一整數
    secret = random.randint(1, up)
    # 玩家猜數字
    for _ in range(up):
        # 提示要求玩家輸入猜測的數字
        guess = int(input(f"猜一個 1-{up} 間的數字: "))
        # 如果所猜數字 < 電腦隨機數
        if guess < secret:
            print("太小了 @ 請再猜一個數字")
        # 如果所猜數字 > 電腦隨機數
        elif guess > secret:
            print("太大了 ! 請再猜個數字")
        # 猜對了
        else:
            print(f"恭喜你猜對了祕密數字 {secret} !!")
            break 
    # 2. 電腦來猜數字
def computer_guess():
    """
    玩家選定數字，並與電腦互動，由電腦猜測此數字
    :param (int) x: 要猜測的數字之範圍上限
    """
    # 1) 提示要求輸入猜測數字的上限
    up = int(input("請輸入上限數字 :"))
    # 2) 請玩家選定一個 1~x 間的數字並記住
    secret = int(input(f"請選定一個 1-{up} 間的數字並記住 :"))

    low = 1
    high = up
    for _ in range(up):
        # 電腦隨機產生 1~up 間的任一整數
        guess = random.randint(low, high)
#電腦要猜了
        print(f"我猜 {guess} ,太高(H)/太低(L) 或 答對了(C)  ??")
#提示要求玩家輸入提示
        user_hint = input("請輸入提示 (H:太高， L:太低， C:中3了) :").upper()
        if user_hint == "H":
            high = guess -1
        elif user_hint == "L":
            low = guess + 1
        elif user_hint == "C":
            print(f"da太好了，貉電腦猜對了，太強了了!!")
            break
        # 4. 執行主程式
def main():
    """
    主程式
    """
    # 玩家選擇猜數字的模式
    選擇 = input("請擇模式 1:玩家來猜數字，2:電腦來猜數字:")
    if 選擇 == "1":
        player_guess()

    elif 選擇 == "2":
        computer_guess()
    else:
        print("BBBvf 無效的輸入，請重新輸入")

if __name__ == "__main__":
    main()
