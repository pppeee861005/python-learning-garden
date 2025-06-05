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

# 第一題：刪除串列中所有負數
print("\n第一題：刪除串列中所有負數")
print("-" * 30)

x = [1, 3, 5, 0, -1, 3, -2]
print(f"原始串列: {x}")

# 方法一：使用串列推導式 (List Comprehension)
x_filtered_1 = [num for num in x if num >= 0]
print(f"方法一結果: {x_filtered_1}")

# 方法二：使用 filter() 函數
x_filtered_2 = list(filter(lambda num: num >= 0, x))
print(f"方法二結果: {x_filtered_2}")

# 方法三：使用迴圈建立新串列
x_filtered_3 = []
for num in x:
    if num >= 0:
        x_filtered_3.append(num)
print(f"方法三結果: {x_filtered_3}")

# 方法四：直接修改原串列（從後往前刪除）
x_copy = x.copy()  # 複製原串列以保留原始資料
for i in range(len(x_copy) - 1, -1, -1):
    if x_copy[i] < 0:
        x_copy.pop(i)
print(f"方法四結果: {x_copy}")

print("\n" + "=" * 50)

# 第二題：計算二維串列中負數的總個數
print("\n第二題：計算二維串列中負數的總個數")
print("-" * 30)

y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
print(f"原始二維串列: {y}")

# 方法一：使用巢狀迴圈
negative_count_1 = 0
for row in y:
    for num in row:
        if num < 0:
            negative_count_1 += 1
print(f"方法一結果: 負數總個數 = {negative_count_1}")

# 方法二：使用串列推導式配合 sum()
negative_count_2 = sum(1 for row in y for num in row if num < 0)
print(f"方法二結果: 負數總個數 = {negative_count_2}")

# 方法三：先展平串列再計算
flattened = [num for row in y for num in row]
negative_count_3 = sum(1 for num in flattened if num < 0)
print(f"方法三結果: 負數總個數 = {negative_count_3}")

# 方法四：詳細顯示每個負數
print("\n詳細分析:")
negative_numbers = []
for i, row in enumerate(y):
    for j, num in enumerate(row):
        if num < 0:
            negative_numbers.append(f"y[{i}][{j}] = {num}")

print(f"找到的負數位置和值:")
for neg in negative_numbers:
    print(f"  {neg}")
print(f"總計: {len(negative_numbers)} 個負數")

print("\n" + "=" * 50)
print("作業完成！")
