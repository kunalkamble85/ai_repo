from clearscreen import clear_screen
import checkbalance
import transfermoney
import logout
import login

def display(username):
    clear_screen()
    print(f"Hello {username}")
    with open("username.txt", "r") as fp:
        for line in fp.readlines():            
            if line.startswith(f"{username}"):
                userdata = line.split(":")
                print(f"WELCOME, {userdata[0]}")
                print("YOUR ACCOUNT INFO\n")
                print(f"NAME..{userdata[2]} {userdata[3]}")
                print(f"FATHER's NAME..{userdata[4]}")
                print(f"MOTHER's NAME..{userdata[5]}")
                print("ADDRESS..", userdata[6])
                print(f"ADHAR CARD NUMBER..{userdata[9]}")
                print(f"MOBILE NUMBER..{userdata[10]}")
                print(f"DATE OF BIRTH.. {userdata[8]}")
                print("ACCOUNT TYPE..", userdata[7])

    print("\nHOME")
    print("******")
    print("1....CHECK BALANCE")
    print("2....TRANSFER MONEY")
    print("3....LOG OUT\n")
    print("4....EXIT\n")

    choice = int(input("ENTER YOUR CHOICE: "))

    if choice == 1:
        checkbalance.checkbalance(username)
    elif choice == 2:
        transfermoney.transfermoney()
    elif choice == 3:
        logout.logout()
        login.login()
    elif choice == 4:
        exit(0)
    else:
        print("Invalid choice!")