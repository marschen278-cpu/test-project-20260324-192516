#!/usr/bin/env python3
"""
快速排序 (Quick Sort) 实现
作者：marschen278-cpu
创建时间：2026-03-24
"""

def quicksort(arr):
    """
    快速排序实现
    
    Args:
        arr: 待排序的列表
        
    Returns:
        排序后的新列表
    """
    # 基准情况：空列表或单元素列表已排序
    if len(arr) <= 1:
        return arr
    
    # 选择中间元素作为基准值
    pivot = arr[len(arr) // 2]
    
    # 分区：小于、等于、大于基准值的元素
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # 递归排序左右分区
    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    快速排序 - 原地版本（节省空间）
    
    Args:
        arr: 待排序的列表（原地修改）
        low: 起始索引
        high: 结束索引
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # 分区操作
        pivot_index = partition(arr, low, high)
        # 递归排序左右两部分
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)
    
    return arr


def partition(arr, low, high):
    """
    分区函数（原地版本）
    
    Args:
        arr: 待排序列表
        low: 起始索引
        high: 结束索引
        
    Returns:
        基准值的最终位置
    """
    pivot = arr[high]  # 选择最后一个元素作为基准
    i = low - 1  # i 指向小于 pivot 区域的最后一个元素
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # 将基准值放到正确位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def main():
    """测试快速排序"""
    print("=" * 50)
    print("快速排序 (Quick Sort) 测试")
    print("=" * 50)
    
    # 测试用例 1: 普通数组
    test1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\n测试 1 - 原始数组：{test1}")
    result1 = quicksort(test1)
    print(f"排序结果：{result1}")
    
    # 测试用例 2: 包含重复元素
    test2 = [5, 2, 8, 2, 9, 1, 5, 5]
    print(f"\n测试 2 - 原始数组：{test2}")
    result2 = quicksort(test2)
    print(f"排序结果：{result2}")
    
    # 测试用例 3: 已排序数组
    test3 = [1, 2, 3, 4, 5]
    print(f"\n测试 3 - 原始数组：{test3}")
    result3 = quicksort(test3)
    print(f"排序结果：{result3}")
    
    # 测试用例 4: 逆序数组
    test4 = [9, 7, 5, 3, 1]
    print(f"\n测试 4 - 原始数组：{test4}")
    result4 = quicksort(test4)
    print(f"排序结果：{result4}")
    
    # 测试用例 5: 原地排序
    test5 = [42, 17, 89, 35, 66, 10]
    print(f"\n测试 5 - 原地排序 - 原始数组：{test5}")
    quicksort_inplace(test5)
    print(f"排序结果：{test5}")
    
    print("\n" + "=" * 50)
    print("所有测试完成！")
    print("=" * 50)


if __name__ == "__main__":
    main()
