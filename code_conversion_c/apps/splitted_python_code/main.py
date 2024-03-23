import account
import login

# Driver Code
def main():
    print("\n\n\n**********************************")
    print("WELCOME TO BANK ACCOUNT SYSTEM\n")
    print("**********************************")
    print("DEVELOPER-Kunal Kamble\n")

    print("1.... CREATE A BANK ACCOUNT")
    print("2.... ALREADY A USER? SIGN IN")
    print("3.... EXIT\n")

    choice = int(input("ENTER YOUR CHOICE: "))

    if choice == 1:
        account.account()
    elif choice == 2:
        login.login()
    elif choice == 3:
        exit(0)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()