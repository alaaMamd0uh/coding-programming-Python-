
def is_prime(n):
    check= False
    if n==1 or n<0:
        print(f"{n} is not a prime number")
    elif n > 1 :
        for i in range(2,n):
            if n%i==0:
                check = True
                break
        if check:
            print(f"{n} is not a prime number")
        else:
            print(f"{n} is a prime number")



def is_pronic(n):
    check= False
    for i in range(n):
        if i*(i+1)==n:
            check = True
            break
    if check:
        print(f"{n} is a Pronic number")
    else:
        print(f"{n} is not a pronic number")



def menu ():
 while True:
    print("[1] to check if a number is prime \n"
          "[2] to check if a number is pronic \n"
          "[3] to Exit\n")
    choice=int(input("Enter your choice: "))
    if choice == 1:
       is_prime(int(input("Enter a number to check if it is a prime number: ")))
    elif choice == 2:
       is_pronic(int(input("Enter a number to check if it is a pronic number: ")))
    elif choice == 3:
        print('ok, bye bye')
        break
    else:
        print("Invalid choice")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



menu()