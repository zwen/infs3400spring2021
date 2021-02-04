
## Assignment 03 - Coding Exercise

### Please read the programming requirements carefully, then code accodingly.

#### Q1. Enhance Q6 (code block 6) from the previous assignment, so that it can measure the total amount of time it took to guess the password. Hint: use the 'time' library. You can measure the current time right before the looping starts, then measure the current time again right after the looping ends. Variables to consider: startTime, finishTime, totalTime


#### Q2. Change the password to 980597, then run the code to measure the total time again. Please calculate what is the percentage change in time in finding the password this time? (percentage increase = ((newTotalTime - oldTotalTime)/newTotalTime)*100



#### Q3. Complete the following code block (three blanks inside) so that it can execute the following list of assignments:
- #### 1) receive user password input;
- #### 2) check to see if the password is correct. Only admit the user when the password matches with the password in file (aka. password variable);
- #### 3) If user enters a wrong password, ask three more times. If cannot answer within three times, say "You have used too many attempts today, please call us for login." If entered a correct password, then say "Welcome to the system."

```python
userName = "aaron"
password = "4356"

userNamefromInput = "aaron"

msg = "Hi, " + userNamefromInput + ", What is your password? "
passwordfromInput = input(msg)

promptCount = 0

while ____________(1)____________:  #looping condition.
    print("Looks like you entered a wrong password, please enter again.")
    passwordfromInput =  input("What is your password: ")
    _______(2)_________   #looping control variable

if ________(3)_________:
    print("You have used too many attempts. Please call us for login.")
else:
    print("Welcome to the system.")
```


#### Q4. Think about a way to use a brute-force approach to crack a password that is a combination of alphanumerics. Give me a list of functions or methods you potentially think that are useful in this case. Discuss, as best as you can, your approach to this problem. (Doesn't have to be perfect. We are not trained hackers anyway.)

```python
passphrase = "2a9b"
```
