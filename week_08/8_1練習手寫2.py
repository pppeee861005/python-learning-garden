#道導入nums
nums = [30, 3, 8, 20, 25, 21, 25, 10, 7, 18]

def find_kth(nums, k):
    top_k = nums[:k]#取到k個就好了
    
    
    def min_index(lst):#找到最小的數字的索引
        mini_i = 0
        for i in range(1, len(lst)):#111
            if lst[i] < lst[mini_i]:#第一個先和第二個比，得到最小的x。然後x再和第三個比..第四個比。直到找到最小的
                mini_i = i#更新最小(索引值)
        return mini_i
    
    for num in nums[k:]:#一開始從資料挖掉了k個，現在處理剩下的
        idx = min_index(top_k)#得到top_k最小值的索引
        if num > top_k[idx]:#剩下的如果找到大於top_k最小值的數字y，就丟到top_k
            top_k[idx] = num #y取代x
    idx = min_index(top_k) #得到 新的 top_k最小值的索引
    return top_k[idx] #回傳 新的 top_k最小值

#處理美觀的Print
def print_colorful_result(nums, k, result):
    #顏色定義
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'
    #框線
    print(f"{CYAN}{'='*40}{END}")
    print(f"{YELLOW}原始數列：{END}{nums}")
    print(f"{GREEN}第 {k} 大的數字是：{RED}{result}{END}")
    print(f"{CYAN}{'='*40}{END}")

#呼叫
if __name__ == "__main__":
    result = find_kth(nums, 3)
print_colorful_result(nums, 3, result)
