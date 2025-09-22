
change=int(input("Enter the coin: "))
lst=[500,100,50,10]

def coin_problem(amount,lst):
    result={}
    count = 0
    for value in lst:
        count=amount//value
        amount=amount%value
        result[value]=count

    return result


res=coin_problem(change,lst)
for coin,num in res.items():
    print(f"{coin}won: {num}")

