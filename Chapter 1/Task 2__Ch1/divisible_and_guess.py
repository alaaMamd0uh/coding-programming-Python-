

# 1
while True :
 X=int(input("X= "))
 Y=int(input("Y= "))

 if Y>X:
    for i in range(X+1,Y,1):
      if i % 5== 0 and i%7==0:
        print(i,end=", ")
    break
 else:
    print("X is more than or equal to Y\nPlease try again")


# 2
import random
dice=random.randint(1,100)
count=0
print("Enter your num between 1 and 100")
while True:
 choice=int(input("Enter number:"))
 if choice<dice:
    count+=1
    print("Lower!")
 elif choice>dice:
    count+=1
    print("Higher!")
 elif choice==dice:
    count+=1
    print("Congratulations: total try = ",count)
    break
