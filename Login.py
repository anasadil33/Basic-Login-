
#user id and password stored in the system to compare
userid = '1234';
password = '1234';
#take input from the user 
username = str(input("Please Enter Username\n"));
if username == userid :                                   #if username matches, then proceed
    print("Please enter Password\n");
    password2 = str(input());
    if password2 == password :                            #if password matches then login successful or else invalid password
        print ('Password is correct\n');
        print("Login succesfull!\n");
    else :
        print("Wrong password detected.\n");
        print("Enter password again!\n");
else :                                                    # default case. 
    print("Enter correct username!");

    
