# 🔄 型別轉換魔法
# 檔案名稱：type_conversion.py

print("🎭 型別轉換魔法秀！")
print("🌟 讓我們看看 Python 的變身術！")

# 字串轉數字
print("\n📝 字串轉數字魔法：")
str_number = "123"
int_number = int(str_number)
float_number = float(str_number)

print(f"📝 原始字串：'{str_number}' (型別：{type(str_number)})")
print(f"🔢 轉成整數：{int_number} (型別：{type(int_number)})")
print(f"🔢 轉成浮點數：{float_number} (型別：{type(float_number)})")

# 數字轉字串
print("\n🔢 數字轉字串魔法：")
number = 456
str_from_number = str(number)

print(f"🔢 原始數字：{number} (型別：{type(number)})")
print(f"📝 轉成字串：'{str_from_number}' (型別：{type(str_from_number)})")

# 布林值轉換
print("\n✨ 布林值轉換魔法：")
print(f"✅ True 轉整數：{int(True)}")
print(f"❌ False 轉整數：{int(False)}")
print(f"🔢 1 轉布林值：{bool(1)}")
print(f"🔢 0 轉布林值：{bool(0)}")

# 小數轉整數
print("\n🎯 小數轉整數魔法：")
decimal = 3.14159
integer = int(decimal)
print(f"🥧 原始小數：{decimal}")
print(f"🔢 轉成整數：{integer} (小數部分被捨棄)")

# 實用範例
print("\n🌈 實用範例：計算機")
print("讓使用者輸入兩個數字，然後相加")

# 模擬使用者輸入（實際使用時可以用 input()）
user_input1 = "25"
user_input2 = "17"

print(f"使用者輸入的第一個數字：'{user_input1}' (這是字串)")
print(f"使用者輸入的第二個數字：'{user_input2}' (這是字串)")

# 轉換成數字並計算
num1 = int(user_input1)
num2 = int(user_input2)
result = num1 + num2

print(f"轉換後相加：{num1} + {num2} = {result}")

print("\n🎉 型別轉換魔法秀結束！")
print("💡 記住：Python 可以在不同型別間自由轉換！")
