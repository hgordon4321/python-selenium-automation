# 1. Reverse selection sort
def sel_sort_r(nums: list):
    for i in range(len(nums)):
        max_index = i
        for j in range(i, len(nums)):
            if nums[j] > nums[max_index]:
                max_index = j
        nums.insert(i, nums.pop(max_index))
    return nums


# 2. Reverse bubble sort
def bub_sort_r(nums: list):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j+1] > nums[j]:
                nums.insert(j+1, nums.pop(j))
    return nums


# 3. Reverse insertion sort
def ins_sort_r(nums: list):
    for i in range(1, len(nums)):
        ins_index = 0
        for j in range(0, i):
            if nums[i] < nums[j]:
                ins_index += 1
            else:
                break
        nums.insert(ins_index, nums.pop(i))
    return nums


# 4. Reverse merge sort
def mer_sort_r(nums: list):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    return merge_lists(mer_sort_r(nums[:mid]), mer_sort_r(nums[mid:]))


def merge_lists(l1: list, l2: list):
    merged_list = []
    while len(l1) and len(l2) > 0:
        if l1[0] >= l2[0]:
            merged_list.append(l1.pop(0))
        else:
            merged_list.append(l2.pop(0))
    merged_list.extend(l1)
    merged_list.extend(l2)
    return merged_list







# Function calls
print("1. Selection Sort:", sel_sort_r([5, 1, 8, 4, 6, 9, 15]))
print("2. Bubble Sort:   ", bub_sort_r([5, 1, 8, 4, 6, 9, 15]))
print("3. Insertion Sort:", ins_sort_r([5, 1, 8, 4, 6, 9, 15]))
print("4. Merge Sort:    ", mer_sort_r([5, 1, 8, 4, 6, 9, 15]))