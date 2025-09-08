

def add(num1,num2):
    return num1 + num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Invalid Division by zero is not allowed")
def sub(num1,num2):
    return num1 - num2
def menu():
    n1 = int(input("please enter your first number: "))
    n2 = int(input("please enter your second number: "))
    print("1. addition \n"
          "2. multiplication \n"
          "3. division \n"
          "4. subtraction \n"
    )
    choice= int(input("please enter your choice: "))
    if choice == 1:
        add(n1, n2)
    elif choice == 2:
        mul(n1, n2)
    elif choice == 3:
        div(n1, n2)
    elif choice == 4:
        sub(n1, n2)
    else:
        print("Invalid choice")

menu()