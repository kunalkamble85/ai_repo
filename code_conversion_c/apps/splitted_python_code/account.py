from declaration import User
import accountcreated

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
    u1.password = input("\nPASSWORD: ")

    # Writing user data to file
    user_data = f"""{u1.username}:{u1.password}:{u1.fname}:{u1.lname}:{u1.fathname}:{u1.mothname}:{u1.address}:{u1.typeaccount}:{u1.date}-{u1.month}-{u1.year}:{u1.adharnum}:{u1.pnumber}"""
    with open("username.txt", "a") as fp:
        fp.write(f"{user_data}")

    accountcreated.accountcreated()