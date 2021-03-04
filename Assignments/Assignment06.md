## Assignment 06 - Coding Exercise

### Please read the programming requirements carefully, then code accodingly.

#### Q1. Please complete the following backdoor problem (from ```assignment 04``` ```question 04```). Specifically, please create a ```checkPassword()``` function so that the complete program can work exactly the same as the previous one. (Hint:  Does the newly created function need to return anything?) (The solution for ```assignment 04``` can be [found here.](https://github.com/zwen/infs3400spring2021/blob/main/Assignments/Assignment_04_Q4_Solution.py))

- The newly created function must be placed before it is being invoked. There is already a placeholder for the function.
- Think about whether it should return anything or not. 

```python
userName = "aaron"
password = "4356"

userNamefromInput = "aaron"

msg = "Hi, " + userNamefromInput + ", What is your password? "
promptCount = 0

passwordfromInput = input(msg)

# New function will start here.


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
```
