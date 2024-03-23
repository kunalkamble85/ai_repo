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