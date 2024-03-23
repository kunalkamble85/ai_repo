from clearscreen import clear_screen
import display
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
    display.display(usernamet)