## 建立與啟用虛擬環境

1. **檢查 Python 是否已安裝**  
   在終端機輸入以下指令，檢查是否已安裝 Python：
   ```bash
   python --version
   ```
   如果未安裝，請先從 [Python 官方網站](https://www.python.org/) 下載並安裝。

2. **進入目標目錄**  
   開啟終端機 (Command Prompt 或 PowerShell)，切換到目標目錄：
   ```bash
   cd /c:/Users/Administrator/Downloads/code_homework
   ```

3. **建立虛擬環境**  
   使用 `python -m venv` 指令建立虛擬環境：
   ```bash
   python -m venv venv
   ```

4. **啟用虛擬環境**  
   - 在 Windows 上：
     ```bash
     .\venv\Scripts\activate
     ```
   - 如果使用的是 PowerShell：
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```

5. **確認虛擬環境已啟用**  
   啟用後，終端機提示符前應該會出現 `(venv)`，表示虛擬環境已成功啟用。

6. **安裝所需套件**  
   在虛擬環境中安裝所需的 Python 套件：
   ```bash
   pip install -r requirements.txt
   ```

7. **停用虛擬環境**  
   完成工作後，可使用以下指令停用虛擬環境：
   ```bash
   deactivate
   ```
