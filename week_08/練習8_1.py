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

nums = [30, 3, 8, 20, 25, 21, 25, 10, 7, 18]

def find_kth(nums, k):
    """
    回傳 nums 中第 k 大的數字
    :param nums: 數字串列
    :param k: 第 k 大
    :return: 第 k 大的數字
    """
    # 先取前 k 個數字作為初始 top_k
    top_k = nums[:k]
    # 找出 top_k 中最小的數字
    def min_index(lst):
        """     
    Find the index of the minimum element in a list.

    :param lst: List of comparable elements.
    :return: Index of the smallest element in the list.
    """

        min_i = 0#接下來要用索引處理，所以先設定為0
        for i in range(1, len(lst)):
            if lst[i] < lst[min_i]:#索引x<索引y，min_i=0, 1, 2, 3...
                min_i = i
        return min_i #是索引

    # 從第 k+1 個數字開始檢查. 例如 k=5, 則從第 6 個數字開始. 需注意：數字在程式中有時是數字有時是索引
    for num in nums[k:]:
        idx = min_index(top_k)  #得到top_k最小值的索引
        if num > top_k[idx]:    #索引
            top_k[idx] = num    #

    # 最後 top_k 中最小的就是第 k 大
    idx = min_index(top_k)
    return top_k[idx]

# 美麗的彩色輸出
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
