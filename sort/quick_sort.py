




def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [i for i in arr[:-1] if i <=pivot]
    right = [i for i in arr[:-1] if i >pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


nums = [4,23,564,2,3,5]
ans = quick_sort(nums)
print(ans)