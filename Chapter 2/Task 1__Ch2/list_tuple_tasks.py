
#1 The smallest word or group of words in the list
words=[]
for i in range(5):
 word=input(f"Enter a word{i+1}:",)
 words.append(word)

 smallest_len= min(len(x) for x in words )

smallestWords=[]

for word in words:
    if len(word) == smallest_len:
        smallestWords.append(word)

print(smallestWords)
###############################################################

# 2 Count Repeated Numbers in a List
numbers=input("Enter numbers separated by space:").split()
Numbers=[int(num) for num in numbers]

NumberCounts={}

for num in Numbers:
    if num not in NumberCounts:
        NumberCounts[num]=1
    else:
        NumberCounts[num]+=1

print(NumberCounts)
#########################################################

# 2 Count Repeated Numbers in a List (Another solution)
print("....Enter 10 numbers....")

numbers=[]
for i in range (10):
     numbers.append(int(input(f"Enter a number{i+1}: ")))

Number_Counts={}
for num in numbers:
    if num not in Number_Counts:
        Number_Counts[num]=1
    else:
        Number_Counts[num]+=1

print(Number_Counts)
#############################################################

# 3 Bonus task
test_tup=(1,3,14,15,2)
k=2
print(tuple(sorted(test_tup)[-k:]))
#############################################################

# 3 Bonus task (Another solution)
numbers=input("Enter numbers separated by space:").split()
Numbers=tuple((int(num) for num in numbers))
num=2
print(tuple(sorted(Numbers)[-num:]))


