

class SIC_Store:
    def __init__(self,clothes_type,model_year,brand,price):
        self.clothes_type = clothes_type
        self.model_year = model_year
        self.brand = brand
        self.price =float(price)

    def discount (self,):
        if self.clothes_type.lower() == "shirt":
           return self.price-(40*100)/100
        elif self.clothes_type.lower() == "pants":
            return self.price-(30*100)/100
        elif self.clothes_type.lower() == "shoes":
            return self.price-(50*100)/100
        else:
            return  self.price

allItem={}
print("How many item do you have?")
num_of_item=int(input())
for i in range(num_of_item):
    clothesType=input(f"enter clothes type ({i+1})")
    modelYear=input(f"enter model year ({i+1})")
    brand = input(f"enter brand ({i+1})")
    price = input(f"enter price ({i+1})")
    obj = SIC_Store(clothesType,modelYear,brand,price)
    allItem[i]=obj
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
totalPrice = 0
for item in allItem:
    totalPrice += allItem[item].discount()
print(f"total price after discount = {totalPrice}")

