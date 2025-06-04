# 日期模組與迴圈應用
# 作業二：選擇性刪減檔案
# 
# 目標：針對超過 30 天的檔案，只保留星期二收到的，其餘刪除。
# 已知：
#   1. archive 為所有檔案名稱的串列（以接收日期命名的壓縮檔）
#   2. 檔案名稱格式為 'YYYY-MM-DD.zip'
# 輸出：
#   印出超過 30 天且不是星期二收到的檔案名稱

import datetime

archive = [
    '2024-07-05.zip', '2024-07-16.zip', '2024-07-24.zip',
    '2024-08-06.zip', '2024-08-14.zip', '2024-08-20.zip',
    '2024-09-04.zip', '2024-09-12.zip', '2024-09-24.zip',
    '2024-10-01.zip', '2024-10-15.zip', '2024-10-25.zip'
]

def is_old_and_not_tuesday(file_name):
    """判斷檔案是否超過 30 天且不是星期二收到"""
    date = datetime.datetime.strptime(file_name, '%Y-%m-%d.zip')
    return (datetime.datetime.now() - date).days > 30 and date.weekday() != 1

# 過濾出需刪除的檔案
old_and_not_tuesday_files = [file for file in archive if is_old_and_not_tuesday(file)]

print(old_and_not_tuesday_files)
