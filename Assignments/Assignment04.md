
## Assignment 04 - Coding Exercise

### Please read the programming requirements carefully, then code accodingly.

#### Q1. Please complete the Q4 from previous assignment based on the [class room discussion from 02/11/2021](https://github.com/zwen/infs3400spring2021/blob/main/In-Class%20Assignment/passwordFinder.py). You may choose to use whichever method you feel comfortable. But the dictionary approach is preferred whenever possible. Your program should satisfy the following requirements.
- You should use these variables and the initial values: ```password = "az6k"``` and ```key = ""```
- We will only consider alphanumeric key at this time.
- Please measure how long did it take to find the password using ```time.time()``` methods. Please report the time.
- You should measure time from the very beginning of your program, not just the search process. For example, if you prefer to generate a dictionary before loop it through, the dictionary generation time should also be considered.


#### Q2. Please extend the Q1. This time, your password should include all possible characters (special symbols and alphanumerics).
- You should use these variables and the initial values: ```password = "&z6!"``` and ```key = ""```
- Please measure how long did it take to find the password using ```time.time()``` methods. Please report the time.

#### Q3. So far, we have worked on brute-force cases where the length of the password is known before hand. Please extend/revise your Q2 so that it can crack any password with maximum length of 10.
- You should use these variables and the initial values: ```password = "a#&Jz6!"``` and ```key = ""``` (Note: since we do not know the length of the password, you should not use ```len(password)``` to define your loop iterations.)
- Please measure how long did it take to find the password using ```time.time()``` methods. Please report the time.
- (Update on 02/17/2021: You may or [may not be able to complete this problem in your human life](https://random-ize.com/how-long-to-hack-pass/?). At the bottom line, please complete the code. We will discuss more on this 02/18/2021 class.)



#### Q4. How would you implement a backdoor in an authentication process? Please implement this based on the Q3 from previous week. (I have posted the [full solution for the Assignment03-Q3](https://github.com/zwen/infs3400spring2021/blob/main/Assignments/Assignment03_Solution.py).)
- You will be able to get into the system with a master password ```'king'```, regardless of the actual password. 






(FYI: I suspect that the faster your computer's clock speed, the shorter the search time will be. If you have access to more than one computer, you can test this theory. But this is not part of your assignment.)
