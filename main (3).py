'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("1. Add");
print("2. Subtract");
print("3. Times");
print("4. Divide");
print("5. Exit");
Answer = int(input("Enter Your Choice: "));
if (Answer>=1 and Answer<=4):
    print("Enter Two Numbers: ");
    NumOne = int (input());
    NumTwo = int (input());
    if Answer == 1:
        resource = NumOne + NumTwo;
        print("Result = ", resource);
        input('Press the ENTER key to continue')
    elif Answer == 2:
        resource = NumOne - NumTwo;
        print("Result = ", resource);
        input('Press the ENTER key to continue')
    elif Answer == 3:
        resource = NumOne * NumTwo;
        print("Result = ", resource);
        input('Press the ENTER key to continue')
    else:
        resource = NumOne / NumTwo;
        print("Result = ", resource);
        input('Press the ENTER key to continue')
elif Answer == 5:
    input('Press the ENTER key to continue')
    exit();
else:
    print("What You Have Inputed Is Incorrect");
