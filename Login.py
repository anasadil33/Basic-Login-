
#user id and password stored in the system to compare
useridkey = '1234';
passwordkey = '1234';
#take input from the user 
username = str(input("Please Enter Username\n"));
if username == useridkey :                                   #if username matches, then proceed
    print("Please enter Password\n");
    password = str(input());
    if password2 == passwordkey :                            #if password matches then login successful or else invalid password
        print ('Password is correct\n');
        print("Login succesfull!\n");
    else :
        print("Wrong password detected.\n");
        print("Enter password again!\n");
else :                                                    # default case. 
    print("Enter correct username!");

    
