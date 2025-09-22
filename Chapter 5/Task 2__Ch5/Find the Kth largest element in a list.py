def findKthLargest(lst, k):
    if len(lst) == 1:
        return lst[0]
    n = len(lst)
    target = n - k

    pivot = lst[-1]
    less = []
    greater = []

    for i in lst[:-1]:
        if i <= pivot:
            less.append(i)
        else:
            greater.append(i)

    if target < len(less):
        return findKthLargest(less, len(less) - target)#=[45,23],1
    elif target == len(less):
        return pivot
    else:
        return findKthLargest(greater, k - len(less) - 1)





print(findKthLargest([100,45,23,66],3))






