from clearscreen import clear_screen
import loginsu
import display

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
            if line.startswith(f"{username}:{password}"):
                loginsu.loginsu(username)
                display.display(username)
                return
        else:
            print("Invalid username or password.")
            input("Press enter to continue")