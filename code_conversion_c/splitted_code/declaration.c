struct pass {
	char username[50];
	int date, month, year;
	char pnumber[15];
	char adharnum[20];
	char fname[20];
	char lname[20];
	char fathname[20];
	char mothname[20];
	char address[50];
	char typeaccount[20];
}

struct money {
	char usernameto[50];
	char userpersonfrom[50];
	long int money1;
}

struct userpass {
	char password[50];
}