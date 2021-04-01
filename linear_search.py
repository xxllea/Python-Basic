# 线性查找
def linear_search(list, value):
    for index, val in enumerate(list):
        if val == value:
            return index
    else:
        return None


# 二分查找
def binary_search(list, value):
    left = 0
    right = len(list) - 1
    while left <= right:  # 候选区有值
        mid = (left + right) // 2
        if list[mid] == value:
            return mid
        elif list[mid] > value:  # 待查找的值在mid左侧
            right = mid - 1
        else: # 待查找的值在mid右侧
            left = mid + 1
    else:
        return None


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(li, 3))
