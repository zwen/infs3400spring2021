userName = "aaron"
password = "4356"

userNamefromInput = "aaron"

msg = "Hi, " + userNamefromInput + ", What is your password? "
promptCount = 0

passwordfromInput = input(msg)

# New function will start here.
def checkPassword(InputPassword):
    if (InputPassword != password) and (promptCount < 3) and (InputPassword != "king"):
        return True
    else:
        return False
    
# New function will end here.


while checkPassword(passwordfromInput):
    print("Looks like you entered a wrong password, please enter again.")
    passwordfromInput =  input("What is your password: ")
    promptCount += 1
    print(promptCount)


if promptCount >= 3:
    print("You have used too many attempts. Please call us for login.")
else:
    print("Welcome to the system.")