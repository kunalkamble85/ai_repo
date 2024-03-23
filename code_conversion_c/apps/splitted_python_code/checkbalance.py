from clearscreen import clear_screen
import display

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
    display.display(username)