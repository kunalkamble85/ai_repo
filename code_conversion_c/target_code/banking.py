import os

# Function to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Creating a structure to store data of the user
class User:
    def __init__(self):
        self.username = ""
        self.date = 0
        self.month = 0
        self.year = 0
        self.pnumber = ""
        self.adharnum = ""
        self.fname = ""
        self.lname = ""
        self.fathname = ""
        self.mothname = ""
        self.address = ""
        self.typeaccount = ""

# Structure to keep track of amount transfer
class Money:
    def __init__(self):
        self.usernameto = ""
        self.userpersonfrom = ""
        self.money1 = 0

# Driver Code
def main():
    print("WELCOME TO BANK ACCOUNT SYSTEM\n")
    print("**********************************")
    print("DEVELOPER-Kunal Kamble\n")

    print("1.... CREATE A BANK ACCOUNT")
    print("2.... ALREADY A USER? SIGN IN")
    print("3.... EXIT\n")

    choice = int(input("ENTER YOUR CHOICE: "))

    if choice == 1:
        account()
    elif choice == 2:
        login()
    elif choice == 3:
        exit(0)
    else:
        print("Invalid choice!")

# Function to create accounts of users
def account():
    print("!!!!!CREATE ACCOUNT!!!!!\n")

    u1 = User()

    u1.fname = input("FIRST NAME: ")
    u1.lname = input("\nLAST NAME: ")
    u1.fathname = input("\nFATHER's NAME: ")
    u1.mothname = input("\nMOTHER's NAME: ")
    u1.address = input("\nADDRESS: ")
    u1.typeaccount = input("\nACCOUNT TYPE: ")
    u1.date = int(input("\nDATE OF BIRTH (Date): "))
    u1.month = int(input("\nMONTH OF BIRTH (Month): "))
    u1.year = int(input("\nYEAR OF BIRTH (Year): "))
    u1.adharnum = input("\nADHAR NUMBER: ")
    u1.pnumber = input("\nPHONE NUMBER: ")
    u1.username = input("\nUSERNAME: ")
    password = input("\nPASSWORD: ")

    # Writing user data to file
    with open("username.txt", "a") as fp:
        fp.write(f"{u1.username} {password}\n")

    accountcreated()

# Successful account creation
def accountcreated():
    print("\nPLEASE WAIT....")
    print("YOUR DATA IS PROCESSING....\n")
    print("ACCOUNT CREATED SUCCESSFULLY....\n")

    input("Press enter to login")
    login()

# Login function to check the username of the user
def login():
    clear_screen()

    print("ACCOUNT LOGIN\n")
    print("***********************************************\n")

    username = input("USERNAME: ")
    password = input("PASSWORD: ")

    with open("username.txt", "r") as fp:
        lines = fp.readlines()
        for line in lines:
            if line.startswith(f"{username} {password}"):
                loginsu(username)
                display(username)
                return
        else:
            print("Invalid username or password.")
            input("Press enter to continue")

# Redirect after successful login
def loginsu(username):
    clear_screen()
    print("Fetching account details.....\n")

    input("LOGIN SUCCESSFUL....\nPress enter to continue")

# Display function to show the data of the user on screen
def display(username):
    clear_screen()

    with open("username.txt", "r") as fp:
        for line in fp:
            if line.startswith(f"{username} "):
                userdata = line.split()
                print(f"WELCOME, {userdata[0]} {userdata[1]}")
                print("YOUR ACCOUNT INFO\n")
                print(f"NAME..{userdata[0]} {userdata[1]}")
                print(f"FATHER's NAME..{userdata[2]}")
                print(f"MOTHER's NAME..{userdata[3]}")
                print(f"ADHAR CARD NUMBER..{userdata[4]}")
                print(f"MOBILE NUMBER..{userdata[5]}")
                print(f"DATE OF BIRTH.. {userdata[6]}-{userdata[7]}-{userdata[8]}\n")
                print("ACCOUNT TYPE..", userdata[9])

    print("\nHOME")
    print("******")
    print("1....CHECK BALANCE")
    print("2....TRANSFER MONEY")
    print("3....LOG OUT\n")
    print("4....EXIT\n")

    choice = int(input("ENTER YOUR CHOICE: "))

    if choice == 1:
        checkbalance(username)
    elif choice == 2:
        transfermoney()
    elif choice == 3:
        logout()
        login()
    elif choice == 4:
        exit(0)
    else:
        print("Invalid choice!")

# Function to transfer money from one user to another
def transfermoney():
    clear_screen()

    print("---- TRANSFER MONEY ----")
    print("========================\n")

    usernamet = input("FROM (your username): ")
    usernamep = input("TO (username of person): ")
    amount = int(input("ENTER THE AMOUNT TO BE TRANSFERRED: "))

    with open("mon.txt", "a") as fm:
        fm.write(f"{usernamet} {usernamep} {amount}\n")

    print("\nAMOUNT SUCCESSFULLY TRANSFERRED....\n")
    input("Press enter to continue")
    display(usernamet)

# Function to check balance in users account
def checkbalance(username):
    clear_screen()

    print("==== BALANCE DASHBOARD ====\n")
    print("***************************\n")
    print("S no.\tTRANSACTION ID\tAMOUNT\n")

    summoney = 0
    with open("mon.txt", "r") as fm:
        lines = fm.readlines()
        for line in lines:
            if line.startswith(username):
                userdata = line.split()
                print(f"{lines.index(line) + 1}\t{userdata[1]}\t\t{userdata[2]}")
                summoney += int(userdata[2])

    print("\nTOTAL AMOUNT")
    print(summoney)

    input("\nPress enter to continue")
    display(username)

# Logout function to bring user to the login screen
def logout():
    clear_screen()
    print("please wait, logging out")

    for _ in range(10):
        for _ in range(25000000):
            pass
        print(".")

    print("Sign out successfully..\n")
    input("press any key to continue..")

if __name__ == "__main__":
    main()
