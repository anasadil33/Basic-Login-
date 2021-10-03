

userid = '1234';
password = '1234';

username = str(input("Please Enter Username\n"));
if username == userid :
    print("Please enter Password\n");
    password2 = str(input());
    if password2 == password :
        print ('Password is correct\n');
        print("Login succesfull!\n");
    else :
        print("Enter password again!\n");
        print("Wrong password detected.\n");
else :
    print("Enter correct username!");

    