# ex_08_2 筆記

## 題目重點
- 利用 `datetime` 模組處理日期。
- 檔案名稱以日期命名，格式為 `YYYY-MM-DD.zip`。
- 目標：對超過 30 天的檔案，只保留星期二收到的，其餘刪除（實際上是列出要刪除的檔案）。

## 解題步驟
1. 解析檔案名稱取得日期。
2. 判斷該日期是否超過 30 天。
3. 判斷該日期是否為星期二（weekday() == 1）。
4. 若超過 30 天且不是星期二，則列入要刪除的清單。

## 主要程式碼說明
```python
import datetime

def is_old_and_not_tuesday(file_name):
    date = datetime.datetime.strptime(file_name, '%Y-%m-%d.zip')
    if (datetime.datetime.now() - date).days > 30 and date.weekday() != 1:
        return True
    return False
    這段程式碼定義了一個名為 is_old_and_not_tuesday 的函式，用來判斷一個檔案名稱（假設格式為 YYYY-MM-DD.zip）所代表的日期是否「超過 30 天」且「不是星期二」。首先，函式會用 datetime.datetime.strptime(file_name, '%Y-%m-%d.zip') 解析檔名，取得對應的日期物件。接著，計算這個日期距離現在的天數，如果超過 30 天，且該日期的星期幾不是星期二（date.weekday() != 1，其中 0 代表星期一，1 代表星期二），就回傳 True；否則回傳 False。這種寫法常用於檔案清理或備份管理，判斷哪些檔案需要處理或刪除。

old_and_not_tuesday_files = [file for file in archive if is_old_and_not_tuesday(file)]
print(old_and_not_tuesday_files)
```
這段程式碼使用了「串列生成式」（list comprehension）來過濾出符合特定條件的檔案。old_and_not_tuesday_files = [file for file in archive if is_old_and_not_tuesday(file)] 這一行會從 archive 這個檔案清單中，挑選出所有經過 is_old_and_not_tuesday(file) 判斷為 True 的檔案，並將它們組成一個新的串列 old_and_not_tuesday_files。這表示這個新串列只包含「超過 30 天且不是星期二」的檔案。 接下來的 print(old_and_not_tuesday_files) 會把這些符合條件的檔案名稱印出來，方便你檢查或進一步處理。這種寫法簡潔又直觀，常用於資料過濾、檔案管理等情境。

## 小技巧
- `datetime.datetime.strptime()` 可將字串轉為日期物件。
- `datetime.datetime.now()` 取得現在時間。
- `date.weekday()` 取得星期幾（0=一, 1=二, ..., 6=日）。

## 輸出範例
```
['2024-07-05.zip', '2024-07-24.zip', '2024-08-14.zip', '2024-09-04.zip', '2024-09-12.zip', '2024-10-25.zip']

這行程式碼會回傳一個布林值（True 或 False），用來判斷某個日期是否「超過 30 天」且「不是星期二」。它的運作方式是：先用    datetime.datetime.now() - date 算出現在時間與指定日期    date 之間的時間差，再取 .days 得到相差的天數。如果這個天數大於 30，且    date.weekday() != 1（   weekday() 回傳 1 代表星期二），就會回傳 True，否則回傳 False。這種寫法常用於檔案過濾或資料清理，判斷哪些資料已經夠舊且不在特定星期幾。

這行程式碼使用「串列生成式」（list comprehension）來過濾檔案清單。它會從    archive 這個檔案列表中，逐一檢查每個檔案名稱    file，並呼叫    is_old_and_not_tuesday(file) 這個函式判斷該檔案是否「超過 30 天且不是星期二收到」。只有符合這兩個條件的檔案才會被加入新的串列    old_and_not_tuesday_files。這樣的寫法可以快速、簡潔地取得所有需要進一步處理或刪除的檔案名稱，常用於自動化檔案管理或資料清理的情境。