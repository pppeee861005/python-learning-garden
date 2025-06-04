# 練習一：哪個第 k 大？ The kth Largest
# --------------------------------------
# 題目：請參考以迴圈找最大值的方法，
#       撰寫函數找出參數 (數列) 中第 k 大數字
#       (不使用內建函數 sort/max)
# 已知：串列 nums 內含未排序的一串數字(如下)
#       k：任一正整數 (如：5)
# 輸出：印出串列中第 k (如：5) 大的數字為：
# (提示：以 k 個位置存放前 k 大的數字)
# --------------------------------------

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def find_kth(nums, k):
    # 先取前 k 個數字作為初始 top_k「重點在這裡」
    top_k = nums[:k]
    # 找出 top_k 中最小的數字的模組
    def min_index(lst):
        """
        Return the index of the minimum element in the list
        i會動態維護，mini_i會動態維護
        
        簡單：得到top中最小的數的索引
        詳細：
        頭二個數字比較大小：得到mini_i(top中最小的數的索引)，
        然後再比較mini_i和第三個數字比較大小. 
        這樣就可以得到mini_i+1(top中最小的數的索引+1)
        """
        mini_i = 0  # assume the first element is the minimum
        for i in range(1, len(lst)):#動態維護, 先做一個序號：i會從1開始到lst長度, 用來當動態索引
            if lst[i] < lst[mini_i]:#用索引方法，做lst內的數字第一個和第二個比較大小
                mini_i = i  # found a smaller element. 更新mini_i(top中最小的數的索引)
        return mini_i
    # 從第 k+1 個數字開始檢查
    for num in nums[k:]:#從第k+1個數字開始
        idx = min_index(top_k)#得到top_k最小值的索引
        
        if num > top_k[idx]:#用索引比較新的數字和top中最小的數的大小
            top_k[idx] = num#更新top_k[top中最小的數的索引]
    # 最後 top_k 中最小的就是第 k 大
    idx = min_index(top_k)#得到top_k最小值的索引
    


    return top_k[idx]

def print_colorful_result(nums, k, result):
    # 彩色字元
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'
    # 美感框線
    print(f"{CYAN}{'='*40}{END}")
    print(f"{YELLOW}原始數列：{END}{nums}")
    print(f"{GREEN}第 {k} 大的數字是：{RED}{result}{END}")
    print(f"{CYAN}{'='*40}{END}")

if __name__ == "__main__":
    k = 5
    result = find_kth(nums, k)
    print_colorful_result(nums, k, result)