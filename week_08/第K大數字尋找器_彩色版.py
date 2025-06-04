nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def find_kth(nums, k):
    
    """
    Return the kth largest number in a list of numbers.

    The function takes a list of numbers and an integer k as input, and
    returns the kth largest number in the list.

    For example, if the input list is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    and k is 5, the function should return 6, which is the 5th largest
    number in the list.

    :param nums: A list of numbers.
    :type nums: list
    :param k: An integer indicating the kth largest number to find.
    :type k: int
    :return: The kth largest number in the list.
    :rtype: int
    """
    # 先取前 k 個數字作為初始 top_k「重點在這裡」
    top_k = nums[:k]
    
    def min_index(lst):
        """
        找到列表中最小元素的索引位置
        
        :param lst: 要搜尋的數字列表
        :type lst: list
        :return: 最小元素的索引
        :rtype: int
        """
        mini_i = 0
        for i in range(1, len(lst)):  # 遍歷一個動態維護的序號
            if lst[i] < lst[mini_i]:
                mini_i = i  # 找到最小的數字的索引
        return mini_i  # 回傳最小的數字的索引

    # 從第 k+1 個元素開始檢查，重點是找到 idx
    for num in nums[k:]:
        idx = min_index(top_k)  # 得到 top_k 最小值的索引
        
        if num > top_k[idx]:  # 用索引比較新的數字和 top 中最小的數的大小
            top_k[idx] = num  # 更新 top_k[top中最小的數的索引]
    
    # 最後 top_k 中最小的就是第 k 大
    idx = min_index(top_k)
    return top_k[idx]

def print_colorful_result(nums, k, result):
    """
    以美觀的彩色格式顯示第 k 大數字的結果 🌈
    
    :param nums: 數字列表
    :type nums: list
    :param k: 要找第幾大的數字
    :type k: int
    :param result: 第 k 大的數字結果
    :type result: int
    """
    # 彩色字元 🎨
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    END = '\033[0m'
    
    # 美感框線 ✨
    print(f"\n{CYAN}{'🌟' * 20}{END}")
    print(f"{YELLOW}📊 原始數列：{END}{BLUE}{nums}{END}")
    print(f"{GREEN}🎯 第 {MAGENTA}{k}{END}{GREEN} 大的數字是：{RED}✨ {result} ✨{END}")
    print(f"{CYAN}{'🌟' * 20}{END}\n")

if __name__ == "__main__":
    print("🎯 歡迎使用第 K 大數字尋找器！🎯")
    
    # 測試案例 1：原始數列
    print("\n📝 測試案例 1：")
    k = 5
    result = find_kth(nums, k)
    print_colorful_result(nums, k, result)
    
    # 測試案例 2：不同的數列
    print("📝 測試案例 2：")
    nums2 = [15, 3, 8, 12, 7, 20, 1, 9]
    k2 = 3
    result2 = find_kth(nums2, k2)
    print_colorful_result(nums2, k2, result2)
    
    # 測試案例 3：找最大的數字
    print("📝 測試案例 3：")
    nums3 = [100, 50, 75, 25, 90, 60]
    k3 = 1
    result3 = find_kth(nums3, k3)
    print_colorful_result(nums3, k3, result3)
    
    print("🎉 所有測試完成！程式運行正常！🎉")
