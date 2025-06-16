import os

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"🎉 檔案已成功從 {old_name} 更名為 {new_name}！✨")
    except FileNotFoundError:
        print(f"❌ 找不到檔案：{old_name}，請確認檔案路徑是否正確。")
    except FileExistsError:
        print(f"❌ 目標檔案名稱 {new_name} 已存在，請選擇其他名稱。")
    except Exception as e:
        print(f"❌ 發生錯誤：{e}")

if __name__ == "__main__":
    old_file = "week_11/project-11/BARbar.py"
    new_file = "week_11/project-11/HeartProgressBar.py"
    rename_file(old_file, new_file)
