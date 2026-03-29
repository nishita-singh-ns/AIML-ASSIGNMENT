

    password = input("Create password: ")

    if len(password) < 6:
        print("Password too short")
    elif password.islower() or password.isupper():
        print("Password must contain both uppercase and lowercase letters")

    elif password.isalpha():
        print("Password must contain at least one number")
    else:
        login = input("Enter password: ")

        if login == password:
            print("Login successful")
        else:
            print("Wrong password")


output:

    Create password:  Nishita07
    Enter password:  Nishita07

    Login successful
