from clearscreen import clear_screen

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