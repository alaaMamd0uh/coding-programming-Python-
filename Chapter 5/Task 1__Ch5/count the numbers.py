

def count_items(arr):
    if arr==[]:
        return 0

    rest= arr [1:]

    return 1+ count_items(rest)

numbers=[2,4,3,5,8,19,30,8,76]
print(count_items(numbers))


