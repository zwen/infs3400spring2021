

## Assignment 01 - Coding Exercise

### Please use Anaconda/Spyder (or your favorite python editor) to run the following code. Then, answer the short questions. Try your best!


#### Q1. Please run the code block 1 and block 2 below. Are you getting the same results? What would .lower() achieve?

#Block 1
```python
string = "WELCOME"
print(string.lower())
```

#Block 2
```python
print("WELCOME".lower())
```

#### Q2. Please run the code block 3 below. What are you getting? What would .floor() and .ceil() achieve?

#Block 3
```python
import math
print(math.floor(4.3))
print(math.floor(4.8))
print(math.ceil(4.3))
print(math.ceil(4.8))
```

#### Q3. What are the similarities and dissimilarities between lower() vs. floor() and ceil()? (e.g., how they are invoked, what are the precursory tasks etc.)



#### Q4. Please run the code block 4. Print all variables (result1 through result4). What are you getting? (Note that I did not provide the print() function. You need to do it on your own.) Also, please use type() function to see what is the data type of all four variables.

#Block 4
```python
result1 = 1 == '1'
result2 = 1 == 1
result3 = 1 != '1'
result4 = 1 != 1
```

#### Q5. What do you think is the role of "a > b" in the block 5? What will be the outcome if the value of a is changed to 6?

#Block 5
```python
a = 3
b = 4

print(a>b)

if a > b:
    print("a is larger than b")
else:
    print("a is not larger than b")
```

#### Q6. Please run the following code. What do you think the program is hoping to achieve and why it will correctly find out the password? How long did your computer take to complete the code? 
#Block 6
```python
password = 9805
guess = 0

print(password != guess)

while guess != password:
    guess += 1

print("Password is ", guess)
```
