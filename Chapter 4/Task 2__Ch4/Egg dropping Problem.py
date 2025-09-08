
# egg task
import random


floors_number=int(input("Enter the floor number: "))
random_number = random.randint(1, floors_number)
print(f"target : {random_number}\n")

def linearSearchFloors(floorNum, target):
    steps = 0
    for i in range(1,floorNum+1):
        steps += 1
        if i == target:
            return steps, i

def binarySearchFloors(floorNum, target):
    steps = 0
    low=1
    high = floorNum
    while low <= high:
        steps += 1
        mid = (low + high) // 2

        if mid == target:
            return steps, mid
        elif mid < target:
            low = mid + 1
        else:
            high = mid - 1

    return steps, -1

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
linear_steps, linear_floor = linearSearchFloors(floors_number, random_number)
print(f"Linear Search\nSteps: {linear_steps}, floor: {linear_floor}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
binary_steps, binary_floor = binarySearchFloors(floors_number, random_number)
print(f"Binary Search\nSteps: {binary_steps}, Floor: {binary_floor}")

