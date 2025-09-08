# Anagram Task
def bubbleSort(arr):
    number = len(arr)
    for i in range(number):
        for j in range (number-i-1):
            if arr [j]>arr[j+1]:
                arr [j],arr [j+1]=arr [j+1],arr[j]
    return arr


while True:

    word1=input("Enter the first word: ").lower()
    word2=input("Enter the second word: ").lower()
    list1=list(word1)
    list2=list(word2)

    l1=bubbleSort(list1)
    l2=bubbleSort(list2)
    print(l1)
    print(l2)

    if l1==l2:
        print("The two words are Anagrams ")
    else:
        print("The two words are NOT Anagrams")
