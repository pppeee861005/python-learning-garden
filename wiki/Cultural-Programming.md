# 🏮 文化程式專題

> *「古老的智慧與現代的技術相遇，綻放出跨越時空的美麗花朵」*

歡迎來到文化程式專題！這裡是傳統文化與現代程式技術融合的美麗園地。✨

## 🌸 **專題理念**

### 🎨 **文化與技術的詩意結合**
我們相信程式設計不僅是技術的學習，更是文化的傳承：
- **古韻新聲** - 用現代程式語言詮釋古老智慧
- **數位傳承** - 讓傳統文化在數位時代重新綻放
- **創意融合** - 在技術與人文之間架起美麗的橋樑
- **詩意表達** - 讓程式碼也能承載文化的溫度

## 🏮 **六十甲子計算系統**

### 📚 **文化背景**
六十甲子是中國古代的紀年方法，由十天干和十二地支組合而成，每六十年為一個循環。這個系統體現了中華文化對時間循環的深刻理解。

### 💻 **程式實現**

#### 🌟 **基礎版本**
```python
def calculate_ganzhi(year):
    """
    計算年份對應的天干地支
    
    Args:
        year (int): 西元年份
    
    Returns:
        str: 對應的天干地支
    """
    # 十天干
    tiangan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    
    # 十二地支
    dizhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    
    # 以西元4年為甲子年起點
    base_year = 4
    cycle_position = (year - base_year) % 60
    
    tian = tiangan[cycle_position % 10]
    di = dizhi[cycle_position % 12]
    
    return f"{tian}{di}"

# 詩意的使用範例
year = 2025
ganzhi = calculate_ganzhi(year)
print(f"🏮 西元 {year} 年是 {ganzhi} 年")
print("古老的智慧在現代程式中綻放光芒 ✨")
```

#### 🎨 **美化版本**
```python
class GanzhiCalculator:
    """六十甲子計算器 - 傳統文化的程式化表達"""
    
    def __init__(self):
        self.tiangan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        self.dizhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        self.base_year = 4  # 甲子年起點
        
        # 天干地支的文化含義
        self.tiangan_meaning = {
            "甲": "陽木，象徵生機勃勃",
            "乙": "陰木，象徵柔韌成長",
            "丙": "陽火，象徵光明熱情",
            "丁": "陰火，象徵溫暖細膩",
            "戊": "陽土，象徵厚德載物",
            "己": "陰土，象徵包容滋養",
            "庚": "陽金，象徵剛毅果決",
            "辛": "陰金，象徵精緻細膩",
            "壬": "陽水，象徵智慧流動",
            "癸": "陰水，象徵靜謐深邃"
        }
        
        self.dizhi_meaning = {
            "子": "鼠時，夜半時分，萬物歸寂",
            "丑": "牛時，雞鳴時分，勤勞耕耘",
            "寅": "虎時，平旦時分，威猛初醒",
            "卯": "兔時，日出時分，溫和靈動",
            "辰": "龍時，食時時分，變化萬千",
            "巳": "蛇時，隅中時分，智慧靈活",
            "午": "馬時，日中時分，奔騰向前",
            "未": "羊時，日昳時分，溫順和諧",
            "申": "猴時，晡時時分，機智活潑",
            "酉": "雞時，日入時分，準時守信",
            "戌": "狗時，黃昏時分，忠誠守護",
            "亥": "豬時，人定時分，安詳寧靜"
        }
    
    def calculate(self, year):
        """計算年份對應的天干地支"""
        cycle_position = (year - self.base_year) % 60
        
        tian = self.tiangan[cycle_position % 10]
        di = self.dizhi[cycle_position % 12]
        
        return {
            "year": year,
            "ganzhi": f"{tian}{di}",
            "tiangan": tian,
            "dizhi": di,
            "tiangan_meaning": self.tiangan_meaning[tian],
            "dizhi_meaning": self.dizhi_meaning[di],
            "cycle_position": cycle_position + 1
        }
    
    def display_beautiful_result(self, year):
        """美麗地展示計算結果"""
        result = self.calculate(year)
        
        print("🏮" + "="*50 + "🏮")
        print(f"    西元 {result['year']} 年的天干地支")
        print("🏮" + "="*50 + "🏮")
        print()
        print(f"📅 年份：{result['ganzhi']} 年")
        print(f"🌟 位置：六十甲子第 {result['cycle_position']} 位")
        print()
        print(f"🌱 天干：{result['tiangan']} - {result['tiangan_meaning']}")
        print(f"🐾 地支：{result['dizhi']} - {result['dizhi_meaning']}")
        print()
        print("✨ 古老的智慧在現代程式中重新綻放 ✨")
        print()

# 使用範例
calculator = GanzhiCalculator()
calculator.display_beautiful_result(2025)
```

#### 🎯 **互動版本**
```python
def interactive_ganzhi_explorer():
    """互動式六十甲子探索器"""
    calculator = GanzhiCalculator()
    
    print("🏮 歡迎來到六十甲子探索器！")
    print("讓我們一起探索時間的奧秘...")
    print()
    
    while True:
        try:
            print("請選擇功能：")
            print("1. 🔍 查詢特定年份")
            print("2. 📊 顯示完整六十甲子表")
            print("3. 🎲 隨機探索")
            print("4. 🚪 退出程式")
            
            choice = input("\n請輸入選項 (1-4)：").strip()
            
            if choice == "1":
                year = int(input("請輸入年份："))
                calculator.display_beautiful_result(year)
                
            elif choice == "2":
                display_complete_ganzhi_table()
                
            elif choice == "3":
                import random
                random_year = random.randint(1900, 2100)
                print(f"🎲 隨機選擇年份：{random_year}")
                calculator.display_beautiful_result(random_year)
                
            elif choice == "4":
                print("🌸 感謝使用六十甲子探索器！")
                print("願古老的智慧伴您前行 ✨")
                break
                
            else:
                print("❌ 請輸入有效的選項")
                
        except ValueError:
            print("❌ 請輸入有效的數字")
        except KeyboardInterrupt:
            print("\n🌸 程式已退出，再見！")
            break
        
        input("\n按 Enter 繼續...")
        print("\n" + "="*60 + "\n")

def display_complete_ganzhi_table():
    """顯示完整的六十甲子表"""
    calculator = GanzhiCalculator()
    
    print("📊 完整六十甲子表")
    print("="*60)
    
    for i in range(60):
        year = 4 + i  # 從甲子年開始
        result = calculator.calculate(year)
        position = i + 1
        
        print(f"{position:2d}. {result['ganzhi']:2s} | "
              f"天干：{result['tiangan']} | 地支：{result['dizhi']}")
        
        if position % 10 == 0:  # 每十個換行
            print("-" * 60)
```

## 📝 **詩韻程式創作**

### 🌸 **詩意的程式設計**
將程式設計與詩歌創作結合，讓代碼也能承載美感和情感。

#### 🎨 **詩句生成器**
```python
class PoetryGenerator:
    """詩句生成器 - 讓程式也能吟詩作對"""
    
    def __init__(self):
        self.seasons = {
            "春": ["花開", "鳥鳴", "綠柳", "暖風", "細雨"],
            "夏": ["荷香", "蟬聲", "綠蔭", "清風", "星空"],
            "秋": ["楓紅", "雁歸", "金桂", "涼風", "明月"],
            "冬": ["雪花", "梅香", "寒風", "暖陽", "歸家"]
        }
        
        self.emotions = {
            "喜": ["歡樂", "愉悅", "開心", "滿足", "幸福"],
            "怒": ["憤怒", "不滿", "激動", "憤慨", "怒火"],
            "哀": ["悲傷", "憂愁", "思念", "惆悵", "離愁"],
            "樂": ["快樂", "輕鬆", "自在", "舒暢", "愜意"]
        }
        
        self.actions = ["漫步", "凝望", "聆聽", "感受", "思考"]
        self.places = ["花園", "小徑", "湖邊", "山頂", "庭院"]
    
    def generate_poem(self, season="春", emotion="喜"):
        """生成詩句"""
        import random
        
        season_words = self.seasons.get(season, self.seasons["春"])
        emotion_words = self.emotions.get(emotion, self.emotions["喜"])
        
        # 生成四句詩
        poem_lines = []
        
        # 第一句：季節描寫
        line1 = f"{season}日{random.choice(season_words)}滿{random.choice(self.places)}"
        poem_lines.append(line1)
        
        # 第二句：情感表達
        line2 = f"{random.choice(emotion_words)}之情{random.choice(self.actions)}中"
        poem_lines.append(line2)
        
        # 第三句：動作描寫
        line3 = f"{random.choice(self.actions)}{random.choice(self.places)}聽{random.choice(season_words)}"
        poem_lines.append(line3)
        
        # 第四句：總結昇華
        line4 = f"程式如詩韻味長"
        poem_lines.append(line4)
        
        return poem_lines
    
    def display_poem(self, season="春", emotion="喜"):
        """美麗地展示詩句"""
        poem = self.generate_poem(season, emotion)
        
        print("📝" + "="*40 + "📝")
        print("    程式詩韻 - 代碼中的詩意")
        print("📝" + "="*40 + "📝")
        print()
        
        for i, line in enumerate(poem, 1):
            print(f"    {line}")
            if i == 2:  # 在第二句後加空行
                print()
        
        print()
        print("✨ 在程式的世界中，也有詩意的美好 ✨")
        print()

# 使用範例
poet = PoetryGenerator()
poet.display_poem("秋", "思")
```

## 🎮 **文化遊戲設計**

### 🏮 **成語接龍程式**
```python
class ChengYuGame:
    """成語接龍遊戲 - 寓教於樂的文化程式"""
    
    def __init__(self):
        # 簡化的成語庫（實際應用中可以擴展）
        self.chengyu_dict = {
            "一": ["一心一意", "一帆風順", "一鳴驚人"],
            "心": ["心想事成", "心花怒放", "心曠神怡"],
            "意": ["意氣風發", "意味深長", "意猶未盡"],
            "帆": ["帆風順水"],
            "順": ["順風順水", "順理成章"],
            "鳴": ["鳴鑼開道"],
            "人": ["人山人海", "人才輩出", "人定勝天"],
            # ... 可以繼續擴展
        }
    
    def find_next_chengyu(self, last_char):
        """根據最後一個字找下一個成語"""
        return self.chengyu_dict.get(last_char, [])
    
    def play_game(self):
        """開始遊戲"""
        print("🏮 歡迎來到成語接龍遊戲！")
        print("讓我們在遊戲中學習中華文化的智慧")
        print()
        
        current_chengyu = "一心一意"
        print(f"起始成語：{current_chengyu}")
        
        score = 0
        
        while True:
            last_char = current_chengyu[-1]
            next_options = self.find_next_chengyu(last_char)
            
            if not next_options:
                print(f"很遺憾，沒有以'{last_char}'開頭的成語了")
                break
            
            print(f"\n請接以'{last_char}'開頭的成語：")
            for i, option in enumerate(next_options, 1):
                print(f"{i}. {option}")
            
            try:
                choice = int(input("請選擇 (輸入數字)：")) - 1
                if 0 <= choice < len(next_options):
                    current_chengyu = next_options[choice]
                    score += 1
                    print(f"✅ 很好！當前成語：{current_chengyu}")
                    print(f"🏆 目前得分：{score}")
                else:
                    print("❌ 無效選擇")
                    break
            except (ValueError, KeyboardInterrupt):
                print("\n🌸 遊戲結束！")
                break
        
        print(f"\n🎉 最終得分：{score}")
        print("感謝參與成語接龍，文化學習永不止步！")

# 使用範例
game = ChengYuGame()
game.play_game()
```

## 🌟 **文化數據視覺化**

### 📊 **二十四節氣圖表**
```python
import matplotlib.pyplot as plt
import numpy as np

def create_solar_terms_chart():
    """創建二十四節氣的美麗圖表"""
    
    # 二十四節氣
    solar_terms = [
        "立春", "雨水", "驚蟄", "春分", "清明", "穀雨",
        "立夏", "小滿", "芒種", "夏至", "小暑", "大暑",
        "立秋", "處暑", "白露", "秋分", "寒露", "霜降",
        "立冬", "小雪", "大雪", "冬至", "小寒", "大寒"
    ]
    
    # 設置中文字體
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 創建圓形圖表
    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(projection='polar'))
    
    # 計算角度
    angles = np.linspace(0, 2*np.pi, 24, endpoint=False)
    
    # 設置顏色（按季節）
    colors = ['#FF6B9D'] * 6 + ['#4ECDC4'] * 6 + ['#FFE66D'] * 6 + ['#A8E6CF'] * 6
    
    # 繪製節氣點
    ax.scatter(angles, [1]*24, c=colors, s=200, alpha=0.8)
    
    # 添加節氣名稱
    for angle, term in zip(angles, solar_terms):
        ax.text(angle, 1.1, term, ha='center', va='center', fontsize=10)
    
    # 設置圖表
    ax.set_ylim(0, 1.3)
    ax.set_title('🌸 二十四節氣圓圖 🌸', fontsize=16, pad=30)
    ax.grid(True, alpha=0.3)
    ax.set_rticks([])  # 隱藏徑向刻度
    
    # 添加季節標籤
    season_angles = [np.pi/2, 0, -np.pi/2, np.pi]
    seasons = ['春', '夏', '秋', '冬']
    season_colors = ['#FF6B9D', '#4ECDC4', '#FFE66D', '#A8E6CF']
    
    for angle, season, color in zip(season_angles, seasons, season_colors):
        ax.text(angle, 0.5, season, ha='center', va='center', 
                fontsize=20, fontweight='bold', color=color)
    
    plt.tight_layout()
    plt.show()

# 使用範例
create_solar_terms_chart()
```

## 🎯 **學習專案建議**

### 🌱 **初級專案**
1. **生肖計算器** - 根據年份計算生肖
2. **簡單詩句生成** - 隨機組合詩詞
3. **節氣提醒程式** - 顯示當前節氣信息

### 🌿 **中級專案**
1. **完整的六十甲子系統** - 包含日期計算
2. **成語學習遊戲** - 互動式成語學習
3. **古詩詞分析工具** - 分析詩詞的韻律和結構

### 🌸 **高級專案**
1. **中華文化知識庫** - 整合多種文化元素
2. **智能詩詞創作** - 使用AI技術創作詩詞
3. **文化教育平台** - 完整的文化學習系統

## 💡 **創意發想**

### 🎨 **更多文化元素**
- **五行相生相剋** - 程式化表達五行理論
- **八卦易經** - 數位化的易經占卜
- **中醫理論** - 程式化的中醫診斷輔助
- **書法藝術** - 數位書法練習系統
- **傳統音樂** - 古典音樂的程式表達

### 🌟 **技術融合**
- **機器學習** - 智能文化內容推薦
- **數據分析** - 文化傳播趨勢分析
- **視覺化** - 美麗的文化數據圖表
- **遊戲化** - 寓教於樂的文化遊戲

## 🤝 **參與方式**

### 📝 **貢獻內容**
- 分享您的文化程式創作
- 提供更多文化元素的程式化想法
- 改進現有的程式碼和算法
- 撰寫文化背景的詳細說明

### 💬 **討論交流**
- 在 Issues 中分享您的文化程式想法
- 討論傳統文化的現代表達方式
- 交流程式設計與文化融合的心得
- 提出新的文化程式專題建議

---

## 🌈 **結語**

文化程式專題不僅是技術的學習，更是文化的傳承和創新。當我們用現代的程式語言來表達古老的智慧時，我們不僅在學習編程，更在參與文化的數位化轉型。

讓我們一起在程式的世界中，為傳統文化注入新的生命力，讓古老的智慧在現代技術中重新綻放光芒！

**願您在文化與技術的交融中，創造出屬於這個時代的美麗作品！** 🏮✨

---

*最後更新：2025年6月*
