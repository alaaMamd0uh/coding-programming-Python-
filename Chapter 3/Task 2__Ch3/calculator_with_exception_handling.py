import json

with open("Users_Information.json", "r") as database:  # to open my json file
    data = json.load(database)

print("~~~~~~~~~~~~~~Welcome to SIC Bank Management System~~~~~~~~~~~~~~~")

def register_page():
    print("___________________Register page_________________________")
    name = input("Please enter your name: ")

    # Loop until the password is 6 characters
    while True:
        password = input("Please enter your password: ")
        if len(password) >= 6:
            break
        else:
            print("Password must be at least 6 characters!")

    phone_number = input("Please enter your phone number: ")

    # Loop until a valid email is entered
    while True:
        email = input("Please enter your email: ")
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email format!")

    # Loop until a valid gender is entered
    while True:
        gender = input("Please enter your gender (male/female): ").lower()
        if gender in ["male", "female"]:
            break
        else:
            print("Gender must be Male or Female!")

    age = input("Please enter your age: ")
    city = input("Please enter your city: ")

    user_id = len(data) + 1  # length of List + 1

    # dictionary to store user information
    userInfo = {
        "id": user_id,
        "name": name,
        "password": password,
        "phone_number": phone_number,
        "email": email,
        "gender": gender,
        "age": age,
        "city": city,
        "balance": 0,
    }

    data.append(userInfo)

    # Open the JSON file in write mode to save the updated list of users
    with open("Users_Information.json", "w") as database:
        json.dump(data, database)

    # print a success message showing the new user's ID
    print(f"Sign up successfully, your id is {userInfo['id']}")

def deposit(foundUser):
    deposited_amount = int(input("please enter the amount you want to deposit: "))
    foundUser['balance'] += deposited_amount
    print('Your new balance is ' + str(foundUser['balance']))

def withdraw(foundUser):
    withdrawn_amount = int(input("please enter the amount you want to withdraw: "))
    if withdrawn_amount <= foundUser['balance']:
        foundUser['balance'] -= withdrawn_amount
        print('Your new balance is ' + str(foundUser['balance']))
    else:
        print('insufficient balance')

def Transfer(foundUser):
    while True:
        receiver_account_id = int(
            input('please enter the id of the account you want to transfer money into it: '))
        transferred_amount = float(input('please enter the amount you want to transfer: '))
        if transferred_amount <= foundUser['balance']:
            for user in data:
                if user["id"] == receiver_account_id:
                    user["balance"] += transferred_amount
                    break
            foundUser['balance'] -= transferred_amount
            print(str(transferred_amount) + ' EGP has been transferred to account with id ' +
                  str(receiver_account_id) + ' successfully')
            print('Your new balance is ' + str(foundUser['balance']) + ' EGP')

        make_another_transaction = input("do you want to make another transaction? (yes/no) ").lower()
        if make_another_transaction == "yes":
            continue
        else:
            print('ok, bye bye')
            break

def Balance_Inquiry(foundUser):
    while True:
        user_balance_currency_choice = input(
            "please enter the currency you want to check your balance in:(EGP/USD/SAR) ").upper()
        if user_balance_currency_choice == "EGP":
            print('your balance is')
            print(str(foundUser['balance']) + " EGP")
        elif user_balance_currency_choice == "USD":
            print('your balance is')
            print(str(foundUser['balance'] / 30) + " USD")
        elif user_balance_currency_choice == 'SAR':
            print('your balance is')
            print(str(foundUser['balance'] / 9) + " SAR")

        make_another_transaction = input("do you want to make another transaction? (yes/no) ").lower()
        if make_another_transaction == "yes":
            continue
        else:
            print('ok, bye bye')
            break

def personal_info(foundUser):
    for key, value in foundUser.items():
        print(f"{key} : {value}")



def login():
    print("___________________Login page_________________________")
    try:
        check_id = int(input("Please enter your id: "))
        check_password = input("Please enter your password: ")

        foundUser = None  # variable to store the matched user

        for user in data:
            # check if both id and password match
            if user["id"] == check_id and user["password"] == check_password:
                foundUser = user
                break  # stop searching once found

        if foundUser:
            print(f"~~~~~~~~~~~~~~~Welcome Back {foundUser['name']}~~~~~~~~~~~~~~~~~~~~~")
            while True:
                choice = input("Here are our services, please choose one:\n"
                               "1. Deposit\n"
                               "2. Withdraw\n"
                               "3. Transfer\n"
                               "4. Balance Inquiry\n"
                               "5. Personal info\n"
                               "6. Exit\n")
                if choice == "1":
                    deposit(foundUser)
                elif choice == "2":
                    withdraw(foundUser)
                elif choice == "3":
                    Transfer(foundUser)
                elif choice == "4":
                    Balance_Inquiry(foundUser)
                elif choice == "5":
                    personal_info(foundUser)
                elif choice == "6":
                    confirm_exit = input("Are you sure you want to exit ? (yes/no) ")
                    if confirm_exit == "yes":
                        print("ok, bye bye")
                        break
                else:
                    print("please Enter valid choice")
        else:
            print("Invalid ID or Password")

    except IndexError:
        print("Error Account with this id doesn't exist")
    except ValueError:
        print("Error id must be a number")


while True:
    print("If you already have an account please Enter login")
    print("If you don't have an account please Enter register")
    user_choice = input().lower()

    if user_choice == "register":
        register_page()
    elif user_choice == "login":
        login()
    else:
        print("Please Enter login or register")
