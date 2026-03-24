#!/usr/bin/env python3
"""
冒泡排序 (Bubble Sort) 实现
作者：marschen278-cpu
创建时间：2026-03-24
"""

def bubblesort(arr):
    """
    冒泡排序 - 基础版本
    
    原理：重复地走访要排序的数列，一次比较两个元素，
    如果它们的顺序错误就把它们交换过来。
    
    Args:
        arr: 待排序的列表
        
    Returns:
        排序后的新列表
    """
    result = arr.copy()
    n = len(result)
    
    for i in range(n):
        # 最后 i 个元素已经有序
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                # 交换元素
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result


def bubblesort_optimized(arr):
    """
    冒泡排序 - 优化版本
    
    优化点：如果某一趟遍历中没有发生交换，说明已经有序，可以提前结束
    
    Args:
        arr: 待排序的列表
        
    Returns:
        排序后的新列表
    """
    result = arr.copy()
    n = len(result)
    
    for i in range(n):
        swapped = False  # 标记是否发生交换
        
        # 最后 i 个元素已经有序
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                # 交换元素
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        
        # 如果没有发生交换，说明已经有序
        if not swapped:
            break
    
    return result


def bubblesort_inplace(arr):
    """
    冒泡排序 - 原地版本（直接修改原数组）
    
    Args:
        arr: 待排序的列表（原地修改）
        
    Returns:
        原列表（已排序）
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


def visualize_bubble_sort(arr):
    """
    可视化冒泡排序过程（打印每一步）
    
    Args:
        arr: 待排序的列表
    """
    result = arr.copy()
    n = len(result)
    step = 0
    
    print(f"初始数组：{result}")
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
                step += 1
                print(f"  步骤 {step}: 交换位置 {j} 和 {j+1} -> {result}")
        
        if not swapped:
            print(f"  已有序，提前结束")
            break
    
    print(f"最终结果：{result}")
    return result


def main():
    """测试冒泡排序"""
    print("=" * 60)
    print("冒泡排序 (Bubble Sort) 测试")
    print("=" * 60)
    
    # 测试用例 1: 普通数组
    test1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\n【测试 1】普通数组")
    print(f"原始数组：{test1}")
    result1 = bubblesort(test1)
    print(f"排序结果：{result1}")
    
    # 测试用例 2: 优化版本
    test2 = [5, 2, 8, 2, 9, 1, 5, 5]
    print(f"\n【测试 2】优化版本（包含重复元素）")
    print(f"原始数组：{test2}")
    result2 = bubblesort_optimized(test2)
    print(f"排序结果：{result2}")
    
    # 测试用例 3: 已排序数组（测试优化版本的提前结束）
    test3 = [1, 2, 3, 4, 5, 6, 7]
    print(f"\n【测试 3】已排序数组（测试提前结束优化）")
    print(f"原始数组：{test3}")
    result3 = bubblesort_optimized(test3)
    print(f"排序结果：{result3}")
    
    # 测试用例 4: 原地排序
    test4 = [42, 17, 89, 35, 66, 10]
    print(f"\n【测试 4】原地排序")
    print(f"原始数组：{test4}")
    bubblesort_inplace(test4)
    print(f"排序结果：{test4}")
    
    # 测试用例 5: 可视化演示
    print(f"\n【测试 5】可视化排序过程")
    test5 = [5, 3, 8, 4, 2]
    visualize_bubble_sort(test5)
    
    # 测试用例 6: 逆序数组
    test6 = [9, 7, 5, 3, 1]
    print(f"\n【测试 6】逆序数组")
    print(f"原始数组：{test6}")
    result6 = bubblesort(test6)
    print(f"排序结果：{result6}")
    
    print("\n" + "=" * 60)
    print("所有测试完成！")
    print("=" * 60)
    
    # 性能说明
    print("\n📊 算法复杂度分析:")
    print("  - 最好情况：O(n) - 已排序数组，优化版本只需一趟遍历")
    print("  - 平均情况：O(n²)")
    print("  - 最坏情况：O(n²) - 逆序数组")
    print("  - 空间复杂度：O(1) - 原地排序")
    print("  - 稳定性：稳定排序")


if __name__ == "__main__":
    main()
