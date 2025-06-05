#[作業一]
# 1)已知串列如下，請撰寫程式刪除list中所有負數，
#   並印出結果串列。
#     x = [1, 3, 5, 0, -1, 3, -2]
#
# 2)已知串列如下，請撰寫程式計算並印出
#   list中負數的總個數。
#     y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]

print("=" * 50)
print("作業一解答")
print("=" * 50)

# 第一題：刪除串列中所有負數（方法三：使用迴圈建立新串列）
print("\n第一題：刪除串列中所有負數")
print("-" * 30)

x = [1, 3, 5, 0, -1, 3, -2]
print(f"原始串列: {x}")

# 使用迴圈建立新串列
x_filtered = []
for num in x:
    # 檢查數字是否為非負數
    if num >= 0:
        x_filtered.append(num)
# 印出結果串列
print(f"列印結果 {x_filtered}")

print("\n" + "=" * 50)

# 第二題：計算二維串列中負數的總個數（方法一：使用巢狀迴圈）
print("\n第二題：計算二維串列中負數的總個數")
print("-" * 30)

y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
print(f"原始二維串列: {y}")

# 使用巢狀迴圈
negative_count = 0
for row in y:
    # 遍歷每一行的數字
    for num in row:
        if num < 0:
            negative_count += 1
print(f"負數總個數: {negative_count}")

print("\n" + "=" * 50)
print("作業完成！")
